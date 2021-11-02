const BasketLogic = {
	productManager(productId, quantity) {
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
				'quantity': quantity,
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
		try{
			quantity = document.getElementById('quantity').value;
		}catch{
			quantity = 1
		}
		BasketLogic.productManager(productId, quantity);
		// for (let i = 0; i < addToBasket.length; i++) {
		// 	if (addToBasket[i].getAttribute("data") == item.getAttribute("data") && (addToBasket[i].classList.contains("added") == false && addToBasket[i].parentElement.classList.contains("added") == false)) {
		// 		if (addToBasket[i].parentElement.nodeName == "DIV") {
		// 			addToBasket[i].style.background = "#fe5858 none repeat scroll 0 0"
		// 			addToBasket[i].style.color = "#fff"
		// 			addToBasket[i].innerText = "remove from cart"
		// 			addToBasket[i].classList.add("added")
		// 		} else {
		// 			addToBasket[i].parentElement.style.background = "#fe5858 none repeat scroll 0 0"
		// 			addToBasket[i].parentElement.style.color = "#fff"
		// 			addToBasket[i].parentElement.classList.add("added")
		// 		}
		// 	}
		// 	else if (addToBasket[i].getAttribute("data") == item.getAttribute("data") && (addToBasket[i].classList.contains("added") | addToBasket[i].parentElement.classList.contains("added"))) {
		// 		if (addToBasket[i].parentElement.nodeName == "DIV") {
		// 			addToBasket[i].style.background = ""
		// 			addToBasket[i].style.color = ""
		// 			addToBasket[i].innerText = "add to cart"
		// 			addToBasket[i].classList.remove("added")
		// 		} else {
		// 			addToBasket[i].parentElement.style.background = ""
		// 			addToBasket[i].parentElement.style.color = ""
		// 			addToBasket[i].parentElement.classList.remove("added")
		// 		}
		// 	}
		// }
	}
})

mdi_close = document.getElementsByClassName('mdi-close')
product_count = document.getElementById("product_count")
basketItem = document.getElementById("cartdrop")
total = document.getElementById("total")

function cartManager() {
	fetch('http://127.0.0.1:8000/en/api/cart-item/', {
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
			html = ''
			total_price = 0
			product_count.innerText = data.length
			for (let i = 0; i < data.length; i++) {
				total_price += parseFloat(data[i]['quantity']*data[i]['product']['product']['price'])
				html += `
							<div class="sin-itme clearfix">
								<a data="${data[i]['product']['id']}" class="add_to_cart"> <i class="mdi mdi-close"></i> </a>
								<a class="cart-img" href="{% url 'cart' %}"><img src='${data[i]['product']['main_image']}'
										alt="" /></a>
								<div class="menu-cart-text">
									<a href="http://127.0.0.1:8000/en/product/single-product/${data[i]['product']['id']}">
										<h5>${data[i]['quantity']} x ${data[i]['product']['product']['title']}</h5>
									</a>
									<span>Color : ${data[i]['product']['color']['title']}</span>
									<span>Size : ${data[i]['product']['size']['title']}</span>
									<strong>$${data[i]['quantity']*data[i]['product']['product']['price']}</strong>
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
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	cartManager()
});