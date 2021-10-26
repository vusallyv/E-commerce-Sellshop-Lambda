const BasketLogic = {
	url: `${location.origin}/api/cart/`,

	addProduct(productId) {
		console.log(localStorage.getItem('token'));
		fetch(`${this.url}`, {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${localStorage.getItem('token')}`
			},
			body: JSON.stringify({
				'product_id': productId,
			})
		}).then(response => response.json()).then(data => {
			if (data.success) {
				console.log(data.message)
			} else {
				alert(data.message);
			}
		});
	}
}


const addToBasket = document.getElementById('add_basket');
addToBasket.onclick = function () {
	const productId = this.getAttribute('data');
	BasketLogic.addProduct(productId);
}