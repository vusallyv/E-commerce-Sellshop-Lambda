main_comments = document.getElementById("main_comments")
comment_length = document.getElementById("comment_length")
replies = document.getElementById("replies")

url = window.location.href
function getProducts() {

    fetch('http://127.0.0.1:8000/en/api/comments/')
        .then(response => {
            return response.json()
        })
        .then(data => {
            console.log(data);
            // for (let i = 0; i < data.length; i++) {
            //     comment_length.innerText = `${data[i]['blogs_comment'].length} comments`
            //     if (data[i]["id"] == url[url.length - 2]) {
            //         for (let j = 0; j < data[i]['blogs_comment'].length; j++) {
            //             if ((data[i]['blogs_comment'][j]['reply']) == null) {

            //                 console.log(data[i]['blogs_comment'][j]);


            //                 main_comment = `<div class="about-author comments">
            //                                     <div class="autohr-text">
            //                                         <img style="width: 90px; height: 100px;" src="{% static 'img/blog/author1.png' %}" alt="" />
            //                                         <div class="author-des">
            //                                             <h4>
            //                                             <a href="#">${data[i]['blogs_comment'][j]['user']}</a>
            //                                             </h4>
            //                                             <span class="floatright"><a href="#">Reply</a> / <a href="#">Hide</a></span>
            //                                             <span>${data[i]['blogs_comment'][j]['created_at']}</span>
            //                                             <p>${data[i]['blogs_comment'][j]['description']}</p>
            //                                         </div>
            //                                     </div>
            //                                 </div>
            //                 `
            //                 main_comments.innerHTML += main_comment
            //             }
            //             else {
            //                 reply = `<div class="about-author reply">
            //                             <div class="autohr-text">
            //                                 <img style="width: 90px; height: 100px;" src="{% static 'img/blog/author1.png' %}" alt="" />
            //                                 <div class="author-des">
            //                                     <h4>
            //                                     <a href="#">${data[i]['blogs_comment'][j]['user']}</a>
            //                                     </h4>
            //                                     <span class="floatright"><a href="#">Hide</a></span>
            //                                     <span>${data[i]['blogs_comment'][j]['created_at']}</span>
            //                                     <p>${data[i]['blogs_comment'][j]['description']}</p>
            //                                 </div>
            //                             </div>
            //                         </div>
            //                     `

            //               replies.innerHTML += reply
            //             }

            //         }

            //     }

            // }
        }).catch(error => {
            console.log(error);
        })

}

getProducts()