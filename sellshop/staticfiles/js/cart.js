var CartLogic = {
    productManager(productId, quantity) {
        fetch('http://127.0.0.1:8000/en/api/cart-quantity/', {
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
                    cartItemManager()
                } else {
                    alert(data.message);
                }
            });
    }
}


let cart_body = document.getElementById("cart_body")



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
            let html = ''
            for (let i = 0; i < data.length; i++) {
                html += `
            <tr>
            <td class="td-img text-left">
            <a href="#"><img src="{% static 'img/cart/1.png' %}" alt="Add Product" /></a>
            <div class="items-dsc">
            <h5><a href="#">${data[i]['product']['product']['title']}</a></h5>
            <p class="itemcolor">Color : <span>${data[i]['product']['color']['title']}</span></p>
            <p class="itemcolor">Size   : <span>${data[i]['product']['size']['title']}</span></p>
            </div>
            </td>
            <td>$${parseFloat(data[i]['product']['product']['price']).toFixed(2)}</td>
            <td>
            <form action="#" method="POST">
            <div class="plus-minus">
            <a class="dec qtybutton">-</a>
            <input type="number" onchange="quantityChange()" data="${data[i]['product']['id']}" id="quantityItem" value="${data[i]['quantity']}" name="qtybutton" class="plus-minus-box">
            <a class="inc qtybutton">+</a>
            </div>
            </form>
            </td>
            <td>
            <strong>$${parseFloat(data[i]['product']['product']['price'] * data[i]['quantity']).toFixed(2)}</strong>
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

function quantityChange() {
    quantityInput = document.querySelectorAll(".plus-minus-box")
    quantityInput.forEach(item => {
        item.onchange = function () {
            const productId = this.getAttribute('data');
            quantity = item.value;
            CartLogic.productManager(productId, quantity);
        }
    })
}


