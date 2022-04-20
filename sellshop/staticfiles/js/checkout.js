let product_table = document.getElementById("product_table")

function checkoutManager() {
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
            let subtotal = 0
            let html = ''
            if (product_table) {

                product_table.innerHTML = `
                <thead>
                <tr>
                <th>Product</th>
                <td>Total</td>
                </tr>
                </thead>
                `
            }
            if (data.length > 0 && data[0]['is_ordered'] == false) {

                for (let i = 0; i < data.length; i++) {
                    html += `
                    <tr>
                    ${data[i]['product']['quantity'] == 0 ? `
                    <th><span style="text-decoration: line-through">${data[i]['quantity']} x Black Men's T-Shirt S</span> Expired </th>` : `<th>${data[i]['quantity']} x Black Men's T-Shirt S</th>`}
                    <td>$${parseFloat(data[i]['quantity'] * data[i]['product']['product']['price'] * (100 - data[i]['coupon_discount']) / 100).toFixed(2)}</td>
                    </tr>`
                    subtotal += parseFloat(data[i]['quantity'] * data[i]['product']['product']['price'] * (100 - data[i]['coupon_discount']) / 100)
                }
                if (product_table) {

                    product_table.innerHTML += html
                    product_table.innerHTML += `
                <tr>
                <th>Cart Subtotal</th>
                <td>$${subtotal.toFixed(2)}</td>
                </tr>
                <tr>
                <th>Shipping and Handing</th>
                <td>$15.00</td>
                </tr>
                <tfoot>
                <tr>
                <th>Order total</th>
                <td>$${(subtotal + 15).toFixed(2)}</td>
                </tr>
                </tfoot>
                `
                }
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    checkoutManager()
});


country = document.getElementsByName('country')[0]
country.onchange = function () {
    if (country.value != '') {
        CityLogic.cityManager(country.options[country.selectedIndex].text)
    } else {
        document.getElementById('id_city').innerHTML = ''
    }
}


var CityLogic = {
    cityManager(country) {
        fetch('http://127.0.0.1:8000/en/api/country/', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'country': country,
            })
        })
            .then(response => response.json())
            .then(data => {
                city = document.getElementsByName('city')[0]
                city.disabled = false
                city.innerHTML = ''
                for (let i = 0; i < data[0]['city'].length; i++) {
                    city.innerHTML += `<option value="${data[0]['city'][i]['id']}">${data[0]['city'][i]['city']}</option>`
                }
            });
    }
}
