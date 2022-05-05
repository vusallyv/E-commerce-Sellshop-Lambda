console.log("Sanity check from room.js.");

const roomName = JSON.parse(document.getElementById('roomName').textContent);

let chatLog = document.querySelector("#chatLog");
let chatMessageInput = document.querySelector("#chatMessageInput");
let chatMessageSend = document.querySelector("#chatMessageSend");
let typingUsers = document.querySelector("#typing-users");
let onlineUsers = document.querySelector("#online-users");
// focus 'chatMessageInput' when user opens the page
chatMessageInput.focus();

// submit if the user presses the enter key
chatMessageInput.onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter key
        chatMessageSend.click();
    }
};

chatMessageInput.onfocus = () => {
    // if (!chatMessageInput.value == "") {
        chatSocket.send(JSON.stringify({
            action: "user_typing"
        }));
    // }
};

chatMessageInput.onfocusout = () => {
    chatSocket.send(JSON.stringify({
        action: "user_not_typing"
    }));
};


getComments = () => {
    fetch('/api/blogs/' + blogId)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            totalCommentCount = 0;
            chatLog.innerHTML = "";
            data.comments.forEach(comment => {
                totalCommentCount++;
                isRequestUser = requestUser == comment.user.username;
                chatLog.innerHTML += `
            <div class="about-author comments">
                <div class="autohr-text">
                    <img src="${comment.user.image}" width="100px" alt="" />
                    <div class="author-des">
                        <h4><a href="#">${comment.user.username} ${comment.is_edited ? `<span style="text-transform: lowercase; color: gray;"> (Edited at ${comment.updated_at})</span>` : ''}</a></h4>
                        <span class="floatright reply-button"><a>Reply</a></span>
                        ${isRequestUser ? `<span data-action="edit_comment" onclick="enableEditComment(this, event)" data-id="${comment.id}" class="floatright edit-button"><a>Edit/</a></span>
                        <span class="floatright" data-id="${comment.id}" onclick=deleteComment(this)><a >Delete/ </a></span>` : ''}
                        <span>${comment.created_at}</span>
                        <textarea id="edit${comment.id}" rows="3" cols="70" style="border: none; background-color: transparent; resize: none; overflow: auto;" disabled>${comment.description}</textarea>
                        
                        
                    </div>
                </div>
            </div>
                `
                comment.replies.forEach(reply => {
                    totalCommentCount++;
                    isRequestUser = requestUser == reply.user.username;
                    chatLog.innerHTML += `
                <div class="about-author reply">
                    <div class="autohr-text">
                        <img src="${reply.user.image}" width="100px" alt="" />
                        <div class="author-des">
                            <h4><a href="#">${reply.user.username} ${reply.is_edited ? `<span style="text-transform: lowercase; color: gray;"> (Edited at ${reply.updated_at})</span>` : ''}</a></h4>
                            ${isRequestUser ? `<span data-action="edit_comment" onclick="enableEditComment(this, event)" data-id="${reply.id}" class="floatright edit-button"><a>Edit</a></span>
                            <span class="floatright" data-id="${reply.id}" onclick=deleteComment(this)><a >Delete/ </a></span>` : ''}
                            <span>${reply.created_at}</span>
                            <textarea id="edit${reply.id}" rows="3" cols="70" style="border: none; background-color: transparent; resize: none; overflow: auto;" disabled>${reply.description}</textarea>
                        </div>
                    </div>
                </div>  
                `
                })
            });
            commentCount = document.querySelector("#comment-count");
            commentCount.innerHTML = totalCommentCount + " Comments";
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

enableEditComment = (e, event) => {
    console.log(e);
    let id = e.getAttribute('data-id');
    let action = e.getAttribute('data-action');
    commentTextarea = document.querySelector(`#edit${id}`);
    commentTextarea.removeAttribute('style');
    commentTextarea.removeAttribute('disabled');
    commentTextarea.focus();
    commentTextarea.onkeyup = function (event) {
        if (event.keyCode === 13) {  // enter key
            console.log('edit comment');
            chatSocket.send(JSON.stringify({
                action: action,
                description: commentTextarea.value,
                id: id
            }));
            chatMessageInput.value = "";
            return;
        }
    }
}

const removeAttributes = (element) => {
    for (let i = 0; i < element.attributes.length; i++) {
        if (element.attributes[i].name != 'id' && element.attributes[i].name != 'class' && element.attributes[i].name != 'type' && element.attributes[i].name != 'name' && element.attributes[i].name != 'placeholder' && element.attributes[i].name != 'rows' && element.attributes[i].name != 'value') {
            element.removeAttribute(element.attributes[i].name);
        }
    }
};


document.addEventListener("DOMContentLoaded", function () {
    getComments();
});

// clear the 'chatMessageInput' and forward the message
chatMessageSend.onclick = function () {
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

getTypingUsers = (data) => {
    typingUsers.innerHTML = "";
    data.users.forEach(user => {
        if (user != requestUser) {
            typingUsers.innerHTML += `${user} is typing...`;
        }
    });
}

getOnlineUsers = (data) => {
    onlineUsers.innerHTML = `<h4>Online Users</h4>
    <ul>`;
    data.users.forEach(user => {
        if (user != requestUser) {
            onlineUsers.innerHTML += `<li>${user}</li>`;
        }
    });
    onlineUsers.innerHTML += `</ul>`;
}


let chatSocket = null;

function connect() {
    chatSocket = new WebSocket("ws://" + window.location.host + "/ws/blog/" + roomName + "/");

    chatSocket.onopen = function (e) {
        console.log("Successfully connected to the WebSocket.");
    }

    chatSocket.onclose = function (e) {
        console.log("WebSocket connection closed unexpectedly. Trying to reconnect in 2s...");
        setTimeout(function () {
            console.log("Reconnecting...");
            connect();
        }, 2000);
    };

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        switch (data.type) {
            case "main_comment":
                getComments();
                break;
            // case "error":
            //     alert(data.message);
            //     break;
            case "delete_comment":
                getComments();
                break;
            case "edit_comment":
                getComments();
                break;
            case "user_typing":
                getTypingUsers(data);
                break;
            case "user_not_typing":
                getTypingUsers(data);
                break;
            case "user_join":
                getOnlineUsers(data);
                break;
            case "user_leave":
                getOnlineUsers(data);
                break;
            default:
                console.error("Unknown message type!");
                break;
        }

        // scroll 'chatLog' to the bottom
        chatLog.scrollTop = chatLog.scrollHeight;
    };

    chatSocket.onerror = function (err) {
        console.log("WebSocket encountered an error: " + err.message);
        console.log("Closing the socket.");
        chatSocket.close();
    }
}
connect();
