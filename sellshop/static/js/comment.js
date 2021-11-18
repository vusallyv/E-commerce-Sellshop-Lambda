url = location.href.split('/')
url = url[url.length - 2]
const CommentLogic = {
    commentPostManager(blogId, description, isMain, replyId) {
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
                'replyId': replyId
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
            total_comments = 0
            var comments = document.getElementById('comments')
            let main_comments = ''
            comments.innerHTML = ''
            for (let i = 0; i < data['comments'].length; i++) {
                total_comments += 1
                main_comments = `
                <div class="about-author comments">
                <div class="autohr-text">
                <img width="100px" src="${data['comments'][i]['user']['image']}" alt="" />
                <div class="author-des">
                <h4><a href="#">${data['comments'][i]['user']['username']}</a></h4>
                <span class="floatright"><a comment_id="${data['comments'][i]['id']}" class="replyButton" onmouseover="isReply()">Reply</a></span>
                <span>${data['comments'][i]['created_at'].split('T')[0]} ${data['comments'][i]['created_at'].split('T')[1].split('+')[0].substring(0, 8)}</span>
                <p>
                ${data['comments'][i]['description']}                                   
                </p>
                </div>
                </div>
                </div>
                `
                if (data['comments'][i]['replies'].length > 0) {
                    total_comments += 1
                    for (let j = 0; j < data['comments'][i]['replies'].length; j++) {
                        main_comments += `
                                <div class="about-author reply">
                                    <div class="autohr-text">
                                        <img width="100px" src="${data['comments'][i]['replies'][j]['user']['image']}" alt="" />
                                        <div class="author-des">
                                            <h4><a href="#">${data['comments'][i]['replies'][j]['user']['username']}</a></h4>
                                            <span class="floatright"></span>
                                            <span>${data['comments'][i]['replies'][j]['created_at'].split('T')[0]} ${data['comments'][i]['replies'][j]['created_at'].split('T')[1].split('+')[0].substring(0, 8)}</span>
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
            comment_length = document.getElementsByClassName('comment_length')
            if (total_comments > 1) {
                for (let i = 0; i < comment_length.length; i++) {
                    comment_length[i].innerText = `${total_comments} comments`
                }
            } else {
                for (let i = 0; i < comment_length.length; i++) {
                    comment_length[i].innerText = `${total_comments} comment`
                }
            }
            submit_comment.setAttribute('isMain', 'True');
            submit_comment.removeAttribute('replyId');
            document.getElementById('id_description').value = ''
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    commentManager()
});


const submit_comment = document.getElementById("submit_comment")

submit_comment.onclick = function () {
    let description = document.getElementById('id_description').value
    const blogId = this.getAttribute('data_id');
    let isMain = this.getAttribute('isMain');
    let replyId = this.getAttribute('replyId');
    CommentLogic.commentPostManager(blogId, description, isMain, replyId);
}

function isReply() {
    replyButton = document.getElementsByClassName('replyButton')
    for (let i = 0; i < replyButton.length; i++) {
        replyButton[i].onclick = function () {
            for (let j = 0; j < replyButton.length; j++) {
                replyButton[j].style.color = '#666'
            }
            if (submit_comment.getAttribute('isMain') != 'False') {
                replyButton[i].style.color = '#fe5858'
                submit_comment.setAttribute('isMain', 'False')
                submit_comment.setAttribute('replyId', this.getAttribute('comment_id'))
            } else {
                replyButton[i].style.color = '#666'
                submit_comment.setAttribute('isMain', 'True')
                submit_comment.removeAttribute('replyId')
            }
        }
    }
}