const BasketLogic = {
	productManager(productId, quantity) {
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
		try {
			quantity = document.getElementById('quantity').value;
		} catch {
			quantity = 1
		}
		BasketLogic.productManager(productId, quantity);
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
			product_count.innerText = data.length
			for (let i = 0; i < data.length; i++) {
				total_price += parseFloat(data[i]['quantity'] * data[i]['product']['product']['price'])
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
									<strong>$${parseFloat(data[i]['quantity'] * data[i]['product']['product']['price']).toFixed(2)}</strong>
								</div>
							</div>
			`
			}
			basketItem.innerHTML = html
			basketItem.innerHTML += `<div class="total">
									<span>total <strong>= $${total_price.toFixed(2)}</strong></span>
									</div>
								`
			total.innerText = `$${total_price.toFixed(2)}`
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	cartManager()
});