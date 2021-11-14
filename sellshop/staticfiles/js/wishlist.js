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
			console.log(data);
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	wishlistManager()
});
