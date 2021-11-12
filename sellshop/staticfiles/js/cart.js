var CartLogic = {
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
                    alert("Product quantity changed")
                    cartManager()
                    cartItemManager()
                } else {
                    alert(data.message);
                }
            });
    }
}


let cart_body = document.getElementById("cart_body")
let product_table = document.getElementById("product_table")

url = location.origin + '/en/api/cart-item/';
function cartItemManager() {
    fetch(url, {
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
                if (data[i]['quantity'] > 0 && data[i]['is_ordered'] == false) {
                    html += `
            <tr>
            <td class="td-img text-left">
            <a href="#"><img style="height: 7rem;" src="${data[i]['product']['images']['image']}" alt="Add Product" /></a>
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
            <input type="number" onmouseover="quantityChange()" data="${data[i]['product']['id']}" min="1" max="${data[i]['product']['quantity']}" id="quantityItem" value="${data[i]['quantity']}" name="qtybutton" class="plus-minus-box">
            <a class="inc qtybutton">+</a>
            </div>
            </form>
            </td>
            <td>
            <strong>$${parseFloat(data[i]['product']['product']['price'] * data[i]['quantity']).toFixed(2)}</strong>
            </td>
            <td><i data="${data[i]['product']['id']}" class="mdi mdi-close remove_from_cart" onmouseover="removeFromCart()" title="Remove this product"></i></td>
            </tr>
			`
                }
            }
            cart_body.innerHTML = html
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    cartItemManager()
});

function quantityChange() {
    quantityInput = document.querySelectorAll(".plus-minus-box")
    for (let i = 0; i < quantityInput.length; i++) {
        quantityInput[i].onchange = function () {
            const productId = this.getAttribute('data');
            quantity = quantityInput[i].value;
            template = "cart.html"
            CartLogic.productManager(productId, quantity, template);
        }
    }

}


