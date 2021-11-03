cart_body = document.getElementById("cart_body")
function cartItemManager() {
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
            cart_body = ''
            let html = ''
            for (let i = 0; i < data.length; i++) {
                html += `
            <tr>
                <td class="td-img text-left">
                    <a href="#"><img src="{% static 'img/cart/1.png' %}" alt="Add Product" /></a>
                    <div class="items-dsc">
                        <h5><a href="#">men’s black t-shirt</a></h5>
                        <p class="itemcolor">Color : <span>Blue</span></p>
                        <p class="itemcolor">Size   : <span>SL</span></p>
                    </div>
                </td>
                <td>$56.00</td>
                <td>
                    <form action="#" method="POST">
                        <div class="plus-minus">
                            <a class="dec qtybutton">-</a>
                            <input type="text" value="02" name="qtybutton" class="plus-minus-box">
                            <a class="inc qtybutton">+</a>
                        </div>
                    </form>
                </td>
                <td>
                    <strong>$112.00</strong>
                </td>
                <td><i class="mdi mdi-close" title="Remove this product"></i></td>
            </tr>
			`
            }
            cart_body.innerHTML = html
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    cartItemManager()
});