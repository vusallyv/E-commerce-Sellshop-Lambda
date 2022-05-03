console.log("Sanity check from room.js.");

const roomName = JSON.parse(document.getElementById('roomName').textContent);

let chatLog = document.querySelector("#chatLog");
let chatMessageInput = document.querySelector("#chatMessageInput");
let chatMessageSend = document.querySelector("#chatMessageSend");

// focus 'chatMessageInput' when user opens the page
chatMessageInput.focus();

// submit if the user presses the enter key
chatMessageInput.onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter key
        chatMessageSend.click();
    }
};

// clear the 'chatMessageInput' and forward the message
chatMessageSend.onclick = function() {
    if (chatMessageInput.value.trim().length <= 0) return;
    chatSocket.send(JSON.stringify({
        "message": chatMessageInput.value,
    }));
    chatMessageInput.value = "";
};

deleteComment = function(comment) {
    chatMessageInput.value = "/del " + comment.getAttribute("comment_id");
    chatSocket.send(JSON.stringify({
        "message": chatMessageInput.value,
    }));
    chatMessageInput.value = "";
};

enableEditComment = function(comment) {
    commentInput = document.getElementById("edit" + comment.getAttribute("comment_id"));
    commentInput.disabled = false;
    commentInput.style.backgroundColor = "white";
    commentInput.style.border = "1px solid #ccc";
    commentInput.focus();
};

editComment = function(comment, event) {
    if (event.keyCode === 13) {  // enter key
        chatSocket.send(JSON.stringify({
            "message": comment.value,
            'type': 'edit_comment',
            'comment_id': comment.getAttribute("comment_id"),
        }));
    }
};

let chatSocket = null;

function connect() {
    chatSocket = new WebSocket("ws://" + window.location.host + "/ws/blog/" + roomName + "/");

    chatSocket.onopen = function(e) {
        console.log("Successfully connected to the WebSocket.");
    }

    chatSocket.onclose = function(e) {
        console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
        setTimeout(function() {
            console.log("Reconnecting...");
            connect();
        }, 2000);
    };
    
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);

        switch (data.type) {
            case "chat_message":
                is_request_user = request_user == data.user; 
                chatLog.innerHTML += `
                <div class="about-author comments" id="comment${data.id}">
                    <div class="autohr-text">
                      <img width="100px" src="${data.image}" alt="">
                      <div class="author-des">
                        <h4><a href="#">${data.user}</a></h4>
                        <span id="reply${data.id}" class="floatright"><a comment_id="">Reply</a></span>

                        ${is_request_user ? `<span onclick="enableEditComment(this)" class="floatright" comment_id="${data.id}"><a>Edit/</a></span>
                        <span id="delete${data.id}" onclick="deleteComment(this)" comment_id="${data.id}" class="floatright"><a >Delete/ </a></span>` : ''}
                        

                        <span>${data.created_at}</span>
                        <input comment_id="${data.id}" onkeyup="editComment(this, event)" id="edit${data.id}" type="text" disabled value="${data.message}" style="background-color: transparent; border: none;">
                      </div>
                    </div>
                  </div>
                `
                break;
            case "error":
                alert(data.message);
                break;
            case "comment_deleted":
                const comment = document.getElementById("comment" + data.id);
                comment.remove();
                break;
            case "edit_comment":
                editedComment = document.getElementById("edit" + data.id);
                editedComment.disabled = true;
                editedComment.style.backgroundColor = "transparent";
                editedComment.style.border = "none";
                editedComment.value = data.message;
                commentDate = document.getElementById("commentDate" + data.id)
                commentDate.innerHTML = data.updated_at;
                break;
            default:
                console.error("Unknown message type!");
                break;
        }

        // scroll 'chatLog' to the bottom
        chatLog.scrollTop = chatLog.scrollHeight;
    };

    chatSocket.onerror = function(err) {
        console.log("WebSocket encountered an error: " + err.message);
        console.log("Closing the socket.");
        chatSocket.close();
    }
}
connect();
