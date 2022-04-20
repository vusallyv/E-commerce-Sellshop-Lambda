url = location.href.split('/')
url = url[url.length - 2]
const ReviewLogic = {
    reviewPostManager(productId, review, rating) {
        fetch(`${location.origin}/en/api/productversions/${url}/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'productId': productId,
                'review': review,
                'rating': rating,
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    reviewManager()
                } else {
                    alert(data.message);
                }
            });
    }
}


function reviewManager() {
    fetch(`${location.origin}/en/api/productversions/${url}/`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            let reviews = document.getElementById('reviews');
            total_review = 0
            reviews.innerHTML = '';
            for (let i = 0; i < data['review'].length; i++) {
                total_review += data['review'][i]['rating']
                reviews.innerHTML += `
                                <div class="info-reviews review-text tab-pane fade in active" >
                                    <div class="about-author">
                                        <div class="autohr-text">
                                            <img style="width: 90px; height: 100px;" src="${data['review'][i]['user']['image']}"
                                            <div class="author-des">
                                                <h4><a href="#">${data['review'][i]['user']['username']}</a></h4>
                                                ${data['review'][i]['rating'] == 0.5 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star-half"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    </span>` : ''}
                                                ${data['review'][i]['rating'] == 1 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    </span>` : ''}
                                                ${data['review'][i]['rating'] == 1.5 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-half"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    </span>` : ''}
                                                ${data['review'][i]['rating'] == 2 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    </span>` : ''}
                                                ${data['review'][i]['rating'] == 2.5 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-half"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    </span>` : ''}
                                                ${data['review'][i]['rating'] == 3 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-outline"></i>
                                                    <i class="mdi mdi-star-outline"></i></span>` : ''}
                                                ${data['review'][i]['rating'] == 3.5 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-half"></i>
                                                    <i class="mdi mdi-star-outline"></i></span>` : ''}
                                                ${data['review'][i]['rating'] == 4 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-outline"></i></span>` : ''}
                                                ${data['review'][i]['rating'] == 4.5 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star-half"></i></span>` : ''}
                                                ${data['review'][i]['rating'] == 5 ? `
                                                    <span class="floatright ratting">
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    <i class="mdi mdi-star"></i>
                                                    </span>` : ''}
                                                <span>${data['review'][i]['created_at']}</span>
                                                <p>${data['review'][i]['review']}</p>
                                            </div>
                                        </div>
                                    </div>
                                    <hr/>
                                </div>
                `;
            }
            if (data['review'].length == 0) {
                data['review'].length = 1
            }
            total_rating = document.getElementById("total_rating")
            total_rating.innerHTML = `
            <p> ${(total_review / data['review'].length).toFixed(2)} Rating </p>
            ${total_review / data['review'].length >= 0 && total_review / data['review'].length < 0.5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            </span>` : ''}
        ${total_review / data['review'].length >= 0.5 && total_review / data['review'].length < 1 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star-half"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            </span>` : ''}
        ${total_review / data['review'].length >= 1 && total_review / data['review'].length < 1.5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            </span>` : ''}
        ${total_review / data['review'].length >= 1.5 && total_review / data['review'].length < 2 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-half"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            </span>` : ''}
        ${total_review / data['review'].length >= 2 && total_review / data['review'].length < 2.5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i>
            </span>` : ''}
        ${total_review / data['review'].length >= 2.5 && total_review / data['review'].length < 3 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-half"></i>
            <i class="mdi mdi-star-outline"></i>
            <i class="mdi mdi-star-outline"></i></span>` : ''}
        ${total_review / data['review'].length >= 3 && total_review / data['review'].length < 3.5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-outline"></i></span>` : ''}
        ${total_review / data['review'].length >= 3.5 && total_review / data['review'].length < 4 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-half"></i>
            <i class="mdi mdi-star-outline"></i></span>` : ''}
        ${total_review / data['review'].length >= 4 && total_review / data['review'].length < 4.5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-outline"></i></span>` : ''}
        ${total_review / data['review'].length >= 4.5 && total_review / data['review'].length < 5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star-half"></i>
            </span>` : ''}
        ${total_review / data['review'].length == 5 ? `
            <span class="floatright ratting">
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            <i class="mdi mdi-star"></i>
            </span>` : ''}
            `
            let review = document.getElementById('id_review')
            review.value = '';
            submit_review.removeAttribute('rating');
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    reviewManager()
});


const submit_review = document.getElementById("submit_review")

submit_review.onclick = function () {
    let review = document.getElementById('id_review').value
    const productId = this.getAttribute('data_id');
    rating = submit_review.getAttribute('rating');
    if (review != '' && rating) {
        ReviewLogic.reviewPostManager(productId, review, rating);
    } else {
        alert("Please write your review and rate")
    }
}

mdi_stars = document.getElementsByClassName("mdi-stars")

for (let i = 0; i < mdi_stars.length; i++) {
    mdi_stars[i].onclick = function () {
        for (let j = 0; j < mdi_stars.length; j++) {
            mdi_stars[j].style.color = "#666666"
        }
        mdi_stars[i].style.color = "red"
        submit_review.setAttribute('rating', i + 1)
    }
}