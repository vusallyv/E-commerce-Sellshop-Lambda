function wishlistManager() {
	fetch(`http://127.0.0.1:8000/en/api/wishlist/`, {
		method: 'GET',
		credentials: 'include',
		headers: {
			'Content-Type': 'application/json',
			'Authorization': `Bearer ${localStorage.getItem('token')}`
		}
	})
		.then(response => response.json())
		.then(data => {
			wishlist_tbody = document.getElementById('wishlist_tbody');
			if (wishlist_tbody) {
				wishlist_tbody.innerHTML = '';
			}
			id_arr = []
			for (let i = 0; i < data['product'].length; i++) {
				id_arr.push(data['product'][i]['id'])
				if (wishlist_tbody) {

					wishlist_tbody.innerHTML += `
						<tr>
					<td class="td-img text-left">
					<a href="#"><img style="width: 83px; height: 108px;" src="${data['product'][i]['images']['image']}" alt="Add Product" /></a>
					<div class="items-dsc">
					<h5><a href="#">${data['product'][i]['product']['title']}</a></h5>
					<p class="itemcolor">Color : <span>${data['product'][i]['color']['title']}</span></p>
					<p class="itemcolor">Size   : <span>${data['product'][i]['size']['title']}</span></p>
					</div>
					</td>
					<td>$ ${data['product'][i]['product']['price']}</td>
					<td>${data['product'][i]['quantity'] > 0 ? `In Stock` : 'Expired'}</td>
					<td>
					<div class="submit-text">
					<a data="${data['product'][i]['id']}" onmouseover="addtoCartFromWishlist()" class="add_to_cart">add to cart</a>
					</div>
					</td>
					<td><i class="mdi mdi-close removeFromWishlist" data="${data['product'][i]['id']}" onmouseover="removeFromWishlist()" title="Remove this product"></i></td>
					</tr>
					`;
				}
			}
			for (let i = 0; i < add_to_wishlist.length; i++) {
				if (id_arr.includes(parseInt(add_to_wishlist[i].getAttribute('data')))) {
					if (add_to_wishlist[i].parentElement.tagName == 'DIV') {
						add_to_wishlist[i].style.backgroundColor = "green";
						add_to_wishlist[i].style.color = "white";
					} else {
						add_to_wishlist[i].parentElement.style.backgroundColor = "green";
						add_to_wishlist[i].parentElement.style.color = "white";
					}
				} else {
					if (add_to_wishlist[i].parentElement.tagName == 'DIV') {
						add_to_wishlist[i].style.backgroundColor = "";
						add_to_wishlist[i].style.color = "";
					} else {
						add_to_wishlist[i].parentElement.style.backgroundColor = "";
						add_to_wishlist[i].parentElement.style.color = "";
					}
				}
			}

		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	wishlistManager()
});

function addtoCartFromWishlist() {
	const addToBasket = document.querySelectorAll('.add_to_cart');
	addToBasket.forEach(item => {
		item.onclick = function () {
			if (item.classList.contains('disabled') == false) {
				if (item.tagName == 'A') {
					item.style.backgroundColor = "green";
					item.style.color = "white";
					item.innerText = "Added to cart"
					item.classList.add('disabled')
					setTimeout(() => {
						item.style.background = "";
						item.style.color = "";
						item.innerText = "Add to cart"
						item.classList.remove('disabled')
					}, 1000);
				} else {
					item.parentElement.style.backgroundColor = "green";
					item.style.color = "white";
					item.classList.add('disabled')
					setTimeout(() => {
						item.parentElement.style.background = "";
						item.style.color = "";
						item.classList.remove('disabled')
					}, 1000);
				}
				const productId = this.getAttribute('data');
				template = "product_list.html"
				try {
					quantity = document.getElementById('quantity').value;
				} catch {
					quantity = 1
				}
				BasketLogic.productManager(productId, quantity, template);


			}
		}
	})
}

function removeFromWishlist() {
	var removeFromWishlist = document.querySelectorAll('.removeFromWishlist');
	for (let i = 0; i < removeFromWishlist.length; i++) {
		removeFromWishlist[i].onclick = function () {
			const productId = this.getAttribute('data');
			WishlistLogic.wishlistPostManager(productId);
		}
	}
}

