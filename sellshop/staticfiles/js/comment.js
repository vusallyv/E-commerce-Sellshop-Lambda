url = `${location.origin}/en/blog/single-blog/1/`.split('/')
url = url[url.length - 2]
const CommentLogic = {
    commentPostManager(blogId, description, isMain) {
        fetch(`${location.origin}/en/api/blogs/${url}/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'blogId': blogId,
                'isMain': isMain,
                'description': description,
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    commentManager()
                } else {
                    alert(data.message);
                }
            });
    }
}


function commentManager() {
    fetch(`${location.origin}/en/api/blogs/${url}/`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            var comments = document.getElementById('comments')
            let main_comments = ''
            comments.innerHTML = ''
            console.log(data)
            for (let i = 0; i < data['comments'].length; i++) {
                // <h4 id="comment_length">${data['comments'].length} comments</h4>
                main_comments = `
                                <div class="about-author comments">
                                <div class="autohr-text">
                                    <img src="${data['comments'][i]['user']['image']}" alt="" />
                                    <div class="author-des">
                                    <h4><a href="#">${data['comments'][i]['user']['username']}</a></h4>
                                    <span class="floatright"><a href="#">Reply</a> / <a href="#">Hide</a></span>
                                    <span>${data['comments'][i]['created_at']}</span>
                                    <p>
                                    ${data['comments'][i]['description']}                                   
                                    </p>
                                    </div>
                                </div>
                                </div>
                `
                if (data['comments'][i]['replies'].length > 0) {
                    for (let j = 0; j < data['comments'][i]['replies'].length; j++) {
                        main_comments += `
                                <div class="about-author reply">
                                    <div class="autohr-text">
                                        <img src="${data['comments'][i]['replies'][j]['user']['image']}" alt="" />
                                        <div class="author-des">
                                            <h4><a href="#">${data['comments'][i]['replies'][j]['user']['username']}</a></h4>
                                            <span class="floatright"><a href="#">Hide</a></span>
                                            <span>${data['comments'][i]['replies'][j]['created_at']}</span>
                                            <p>${data['comments'][i]['replies'][j]['description']}
                                            </p>
                                        </div>
                                    </div>
                                </div>
                    `
                    }
                }
                comments.innerHTML += main_comments
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    commentManager()
});


const submit_comment = document.getElementById("submit_comment")
let description = document.getElementById('id_description')

submit_comment.onclick = function () {
    description = submit_comment.parentElement.parentElement.parentElement.children[2].children[0].children[0].value
    const blogId = this.getAttribute('data_id');
    console.log(description);
    let isMain = "True"
    CommentLogic.commentPostManager(blogId, description, isMain);
}