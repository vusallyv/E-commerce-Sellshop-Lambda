const BasketLogic = {
	productManager(productId, quantity, template) {
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
				'template': template,
			})
		})
			.then(response => response.json())
			.then(data => {
				if (data.success) {
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
		template = "product.html"
		try {
			quantity = document.getElementById('quantity').value;
		} catch {
			quantity = 1
		}
		BasketLogic.productManager(productId, quantity, template);
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
			html = ''
			total_price = 0
			let count = 0
			for (let i = 0; i < data.length; i++) {
				total_price += parseFloat(data[i]['quantity'] * data[i]['product']['product']['price'])
				if (data[i]['quantity'] > 0) {
					count += 1
					html += `
					<div class="sin-itme clearfix">
					<a data="${data[i]['product']['id']}" class="remove_from_cart" onclick="removeFromCart()"> <i class="mdi mdi-close"></i> </a>
					<a class="cart-img" href="{% url 'cart' %}"><img src='${data[i]['product']['main_image']}'
					alt="" /></a>
					<div class="menu-cart-text">
					<a href="http://127.0.0.1:8000/en/product/single-product/${data[i]['product']['id']}">
					<h5>${data[i]['quantity']} x ${data[i]['product']['product']['title']}</h5>
					</a>
					<span>Color : ${data[i]['product']['color']['title']}</span>
					<span>Size : ${data[i]['product']['size']['title']}</span>
					<strong>$${parseFloat(data[i]['quantity'] * data[i]['product']['product']['price']).toFixed(2)}</strong>
					</div>
					</div>
					`
				}
			}
			basketItem.innerHTML = html
			basketItem.innerHTML += `<div class="total">
			<span>total <strong>= $${total_price.toFixed(2)}</strong></span>
			</div>
			`
			total.innerText = `$${total_price.toFixed(2)}`
			product_count.innerText = count
			try {
				cartItemManager()
			} catch {
			}
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	cartManager()
});

function removeFromCart() {
	var remove_from_cart = document.getElementsByClassName("remove_from_cart")
	for (let i = 0; i < remove_from_cart.length; i++) {
		productId = remove_from_cart[i].getAttribute('data');
	}
	quantity = 1
	template = "remove.html"
	BasketLogic.productManager(productId, quantity, template);
}
