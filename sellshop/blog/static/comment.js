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
getComments = () => {
    fetch('/api/blogs/' + blogId)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            chatLog.innerHTML = "";
            data.comments.forEach(comment => {
                console.log(requestUser, comment.user.username);
                isRequestUser = requestUser == comment.user.username; 
                chatLog.innerHTML += `
            <div class="about-author comments">
                <div class="autohr-text">
                    <img src="${comment.user.image}" width="100px" alt="" />
                    <div class="author-des">
                        <h4><a href="#">${comment.user.username}</a></h4>
                        <span class="floatright reply-button"><a>Reply</a></span>
                        ${isRequestUser ? `<span class="floatright"><a>Edit/</a></span>
                        <span class="floatright" data-id="${comment.id}" onclick=deleteComment(this)><a >Delete/ </a></span>` : ''}
                        <span>${comment.updated_at}</span>
                        <p>${comment.description}</p>
                    </div>
                </div>
            </div>
                `
                comment.replies.forEach(reply => {
                    isRequestUser = requestUser == reply.user.username; 
                    chatLog.innerHTML += `
                <div class="about-author reply">
                    <div class="autohr-text">
                        <img src="${reply.user.image}" width="100px" alt="" />
                        <div class="author-des">
                            <h4><a href="#">${reply.user.username}</a></h4>
                            ${isRequestUser ? `<span class="floatright"><a>Edit</a></span>
                            <span class="floatright" data-id="${comment.id}" onclick=deleteComment(this)><a >Delete/ </a></span>` : ''}
                            <span>${reply.updated_at}</span>
                            <p>${reply.description}</p>
                        </div>
                    </div>
                </div>  
                `
                })
            });
            removeAttributes(chatMessageSend);
            removeAttributes(chatMessageInput);
        });
};

deleteComment = (e) => {
    console.log(e);
    chatMessageInput.value = "";
    let id = e.getAttribute('data-id');
    chatMessageInput.value = "/del " + id;
    chatMessageSend.setAttribute('action', 'delete_comment');
    chatMessageSend.click();
};

const removeAttributes = (element) => {
    console.log(element.attributes);
    for (let i = 0; i < element.attributes.length; i++) {
        console.log(element.attributes[i].name);
        if (element.attributes[i].name != 'id' && element.attributes[i].name != 'class' && element.attributes[i].name != 'type' && element.attributes[i].name != 'name' && element.attributes[i].name != 'placeholder' && element.attributes[i].name != 'rows' && element.attributes[i].name != 'value') {
            element.removeAttribute(element.attributes[i].name);
        }
    }
};


document.addEventListener("DOMContentLoaded", function() {
    getComments();
});

// clear the 'chatMessageInput' and forward the message
chatMessageSend.onclick = function() {
    if (chatMessageInput.value.trim().length <= 0) return;
    if (chatMessageSend.getAttribute('action') == 'delete_comment') {
        console.log('chatMessageInput.value');
        chatSocket.send(JSON.stringify({
            action: "delete_comment",
            description: chatMessageInput.value
        }));
        chatMessageInput.value = "";
        return;
    }
    chatSocket.send(JSON.stringify({
        description: chatMessageInput.value,
        action: "main_comment"
    }));
    chatMessageInput.value = "";
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
            case "main_comment":
                console.log(data);
                getComments();
                break;
            // case "error":
            //     alert(data.message);
            //     break;
            case "delete_comment":
                console.log(data);
                getComments();
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
