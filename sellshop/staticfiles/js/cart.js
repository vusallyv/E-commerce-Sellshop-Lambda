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
                    quantityAlert = document.getElementById('quantityAlert')
                    quantityAlert.style.display = 'block'
                    quantityAlert.innerHTML = 'Product quantity changed'
                    setTimeout(() => {
                        quantityAlert.style.display = 'none'
                    }, 1000);
                    cartManager()
                    cartItemManager()
                } else {
                    alert(data.message);
                }
            });
    }
}

var CouponLogic = {
    couponManager(code) {
        fetch('http://127.0.0.1:8000/en/api/coupon/', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'code': code,
            })
        })
            .then(response => response.json())
            .then(data => {
                quantityAlert = document.getElementById('quantityAlert')
                quantityAlert.style.display = 'block'
                quantityAlert.innerHTML = data.message
                if (data.success) {
                    quantityAlert.classList.add('alert-success')
                    quantityAlert.classList.remove('alert-danger')
                } else {
                    quantityAlert.classList.add('alert-danger')
                    quantityAlert.classList.remove('alert-success')
                }
                setTimeout(() => {
                    quantityAlert.style.display = 'none'
                }, 1000);
                cartManager()
                cartItemManager()
            });
    }
}

coupon_button = document.getElementById('coupon_button')
coupon_button.onclick = function () {
    coupon_code = document.getElementById('coupon_code').value
    CouponLogic.couponManager(coupon_code)
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
            console.log(data);
            let html = ''
            cont_ship = document.getElementById('cont_ship')
            if (data.length > 0) {
                cont_ship.style.display = 'block'
            } else {
                cont_ship.style.display = 'none'
            }
            total_price = 0
            total_products = document.getElementById("total_products")
            for (let i = 0; i < data.length; i++) {
                if (data[i]['quantity'] > 0 && data[i]['is_ordered'] == false) {
                    total_price += parseFloat(data[i]['quantity'] * data[i]['product']['product']['price'] * (100 - data[i]['coupon_discount']) / 100)
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
            <td>$${(parseFloat(data[i]['product']['product']['price'] * parseFloat((100 - data[i]['coupon_discount'])) / 100)).toFixed(2)}</td>
            <td>
            <form action="#" method="POST">
            <div class="plus-minus" onmouseover="quantityInputChange()">
            <a class="dec qtybutton">-</a>
            <input type="number" onmouseover="quantityChange()" data="${data[i]['product']['id']}" min="1" max="${data[i]['product']['quantity']}" value="${data[i]['quantity']}" name="qtybutton" class="plus-minus-box">
            <a class="inc qtybutton">+</a>
            </div>
            </form>
            </td>
            <td>
            <strong>$${(parseFloat(data[i]['product']['product']['price'] * data[i]['quantity'] * parseFloat((100 - data[i]['coupon_discount']))) / 100).toFixed(2)}</strong>
            </td>
            <td><i data="${data[i]['product']['id']}" class="mdi mdi-close remove_from_cart" onmouseover="removeFromCart()" title="Remove this product"></i></td>
            </tr>
			`
                }
            }
            cart_body.innerHTML = html
            total_products.children[0].innerHTML = `
                        <tr>
                            <th>Shipping and Handing</th>
                            <td>$15.00</td>
                        </tr>
                        <tr>
                            <th>Cart Subtotal</th>
                            <td>$${total_price.toFixed(2)}</td>
                        </tr>
                        `
            total_products.children[1].innerHTML = `
                <tr>
                    <th class="tfoot-padd">Order total</th>
                    <td class="tfoot-padd">$${(total_price + 15).toFixed(2)}</td>
                </tr>`
            if (data.length == 0) {
                total_products.style.display = 'none'
            }

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


function quantityInputChange() {
    dec = document.getElementsByClassName("dec")
    inc = document.getElementsByClassName("inc")
    qtybutton = document.getElementsByName("qtybutton")
    for (let i = 0; i < dec.length; i++) {
        dec[i].onclick = function () {
            if (qtybutton[i].value > 1) {
                qtybutton[i].value--;
                const productId = qtybutton[i].getAttribute('data');
                quantity = qtybutton[i].value;
                template = "cart.html"
                CartLogic.productManager(productId, quantity, template);
            }
        }
    }
    for (let j = 0; j < inc.length; j++) {
        inc[j].onclick = function () {
            if (qtybutton[j].value < parseInt(qtybutton[j].getAttribute('max'))) {
                qtybutton[j].value++;
                const productId = qtybutton[j].getAttribute('data');
                quantity = qtybutton[j].value;
                template = "cart.html"
                CartLogic.productManager(productId, quantity, template);
            }
        }
    }

}