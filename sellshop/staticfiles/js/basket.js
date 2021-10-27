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
				'product': productId,
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


const addToBasket = document.querySelectorAll('.add_to_cart');

addToBasket.forEach(item => {
	item.onclick = function () {
		const productId = this.getAttribute('data');
		BasketLogic.addProduct(productId);
		if (item.classList.contains("mdi-cart")){
			item.parentElement.style.background = "#fe5858 none repeat scroll 0 0"
			item.parentElement.style.color = "#fff"
		}else{
			item.style.background = "#fe5858 none repeat scroll 0 0"
			item.style.color = "#fff"
		}
	}
})