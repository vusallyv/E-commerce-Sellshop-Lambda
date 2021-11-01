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
					alert(data.message)
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
		for (let i = 0; i < addToBasket.length; i++) {
			if (addToBasket[i].getAttribute("data") == item.getAttribute("data") && (addToBasket[i].classList.contains("added") == false && addToBasket[i].parentElement.classList.contains("added") == false)) {
				if (addToBasket[i].parentElement.nodeName == "DIV") {
					addToBasket[i].style.background = "#fe5858 none repeat scroll 0 0"
					addToBasket[i].style.color = "#fff"
					addToBasket[i].innerText = "remove from cart"
					addToBasket[i].classList.add("added")
				} else {
					addToBasket[i].parentElement.style.background = "#fe5858 none repeat scroll 0 0"
					addToBasket[i].parentElement.style.color = "#fff"
					addToBasket[i].parentElement.classList.add("added")
				}
			}
			else if (addToBasket[i].getAttribute("data") == item.getAttribute("data") && (addToBasket[i].classList.contains("added") | addToBasket[i].parentElement.classList.contains("added"))) {
				if (addToBasket[i].parentElement.nodeName == "DIV") {
					addToBasket[i].style.background = ""
					addToBasket[i].style.color = ""
					addToBasket[i].innerText = "add to cart"
					addToBasket[i].classList.remove("added")
				} else {
					addToBasket[i].parentElement.style.background = ""
					addToBasket[i].parentElement.style.color = ""
					addToBasket[i].parentElement.classList.remove("added")
				}
			}
		}
		BasketLogic.productManager(productId);
	}
})

mdi_close = document.getElementsByClassName('mdi-close')
product_count = document.getElementById("product_count")
basketItem = document.getElementById("cartdrop")
total = document.getElementById("total")

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
			console.log(data);
			product_count.innerText = data['products'].length
			html = ''
			total_price = 0
			for (let i = 0; i < data['products'].length; i++) {
				total_price += parseFloat(data['products'][i]['price'])
				html += `
							<div class="sin-itme clearfix">
								<a data="${data['products'][i]['id']}" class="add_to_cart"> <i class="mdi mdi-close"></i> </a>
								<a class="cart-img" href="{% url 'cart' %}"><img src='{% static "img/cart/2.png" %}'
										alt="" /></a>
								<div class="menu-cart-text">
									<a href="#">
										<h5>${data['products'][i]['title']}</h5>
									</a>
									<span>Color : ${data['products'][i]['color']}</span>
									<span>Size : ${data['products'][i]['size']}</span>
									<strong>$${data['products'][i]['price']}</strong>
								</div>
							</div>
			`
			}
			basketItem.innerHTML = html
			basketItem.innerHTML += `<div class="total">
									<span>total <strong>= $${total_price}</strong></span>
									</div>
								`
			total.innerText = `$${total_price}`
			id_arr = []
			for (let i = 0; i < data['products'].length; i++) {
				id_arr.push(data['products'][i]['product'])
			}
			console.log(id_arr);
			for (let i = 0; i < addToBasket.length; i++) {
				if (id_arr.includes(parseInt(addToBasket[i].getAttribute("data")))) {
					if (addToBasket[i].parentElement.nodeName == "DIV") {
						addToBasket[i].style.background = "#fe5858 none repeat scroll 0 0"
						addToBasket[i].style.color = "#fff"
						addToBasket[i].innerText = "remove from cart"
						addToBasket[i].classList.add("added")
					} else {
						addToBasket[i].parentElement.style.background = "#fe5858 none repeat scroll 0 0"
						addToBasket[i].parentElement.style.color = "#fff"
						addToBasket[i].parentElement.classList.add("added")
					}
				}
			}
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	cartManager()
});