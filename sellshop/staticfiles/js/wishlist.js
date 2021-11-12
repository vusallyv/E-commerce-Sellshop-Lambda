url = location.origin + '/en/api/wishlist/';
console.log(url);


function wishlistManager() {
	fetch(`${url}`, {
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
		});
}


window.addEventListener('DOMContentLoaded', (event) => {
	wishlistManager()
});
