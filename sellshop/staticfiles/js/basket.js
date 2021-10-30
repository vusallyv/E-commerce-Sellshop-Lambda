const BasketLogic = {
	productManager(productId) {
		console.log(localStorage.getItem('token'));
		fetch('http://127.0.0.1:8000/en/api/cart/', {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
			body: JSON.stringify({
				'product': productId,
			})
		})
			.then(response => response.json())
			.then(data => {
				if (data.success) {
					console.log(data.message)
					cartManager()



				} else {
					alert(data.message);
				}
			});
	}
}




const addToBasket = document.querySelectorAll('.add_to_cart');

addToBasket.forEach(item => {
	item.onclick = function () {
		const productId = this.getAttribute('data');
		BasketLogic.productManager(productId);
		for (let i = 0; i < addToBasket.length; i++) {
			if (addToBasket[i].getAttribute("data") == item.getAttribute("data")) {
				if (addToBasket[i].parentElement.nodeName == "DIV") {
					addToBasket[i].style.background = "#fe5858 none repeat scroll 0 0"
					addToBasket[i].style.color = "#fff"
					addToBasket[i].innerText = "remove from cart"
				} else {
					addToBasket[i].parentElement.style.background = "#fe5858 none repeat scroll 0 0"
					addToBasket[i].parentElement.style.color = "#fff"
				}
			}
		}
	}
})

product_count = document.getElementById("product_count")

function cartManager() {
	fetch('http://127.0.0.1:8000/en/api/cart/', {
		method: 'GET',
		credentials: 'include',
		headers: {
			'Content-Type': 'application/json',
			'Authorization': `Bearer ${localStorage.getItem('token')}`
		}
	})
		.then(response => response.json())
		.then(data => {
			console.log(data['products'].length);
			product_count.innerText = data['products'].length
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
    cartManager()
});