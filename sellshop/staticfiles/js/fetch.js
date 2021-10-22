let createCommentForm = document.getElementById('create-comment-form');

async function createComment(commentData) {
    let response = await fetch('http://localhost:8000/en/blog/single-blog/1/', {
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(commentData),
    })
    return response.json();
}
createCommentForm.addEventListener('submit', async function (e) {
    console.log("OK");
    e.preventDefault();
    let commentContent = createCommentForm.description.value;
    let commentData = {
        'content': commentContent
    }
    await createComment(commentData);
});



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}