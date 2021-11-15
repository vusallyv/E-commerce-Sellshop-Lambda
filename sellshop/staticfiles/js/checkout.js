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
            product_table.innerHTML = `
            <thead>
                <tr>
                    <th>Product</th>
                    <td>Total</td>
                </tr>
            </thead>
            `
            if (data.length > 0 && data[0]['is_ordered'] == false) {

                for (let i = 0; i < data.length; i++) {
                    html += `
                    <tr>
                    <th>${data[i]['quantity']} x Black Men's T-Shirt S</th>
                    <td>$${parseFloat(data[i]['quantity'] * data[i]['product']['product']['price']).toFixed(2)}</td>
                    </tr>`
                    subtotal += parseFloat(data[i]['quantity'] * data[i]['product']['product']['price'])
                }
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
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    checkoutManager()
});


country = document.getElementsByName('country')[0]
country.onchange = function () {
    CityLogic.cityManager(country.options[country.selectedIndex].text)
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


const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
// var stripe = Stripe("{{ STRIPE_PUBLIC_KEY }}");
var checkoutButton = document.getElementById("checkout-button");
checkoutButton.addEventListener("click", function () {
    company_name = document.getElementById("id_company_name").value;
    country = document.getElementById("id_country").options[country.selectedIndex].text;
    city = document.getElementById("id_city")
    city = city.options[city.selectedIndex].text;
    address = document.getElementById("id_address").value;
    CheckoutLogic.checkoutPostManager(company_name, country, city, address)
});

const CheckoutLogic = {
    checkoutPostManager(company_name, country, city, address) {
        fetch(`${location.origin}/en/api/checkout/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'company_name': company_name,
                'country': country,
                'city': city,
                'address': address
            })
        })
            .then(response => response.json())
            .then(data => {
                // window.location.href = 'https://checkout.stripe.com/pay/cs_test_a1XIJK0w127JUygn3OKd4zc17fwrnF6M8l6gv5HuEKMWWb9T0t7TwMNneJ#fidkdWxOYHwnPyd1blpxYHZxWjA0T3NWb3NPVHRuNjZXSFxxdmFNNEp9Q05DZml0aHVwMm5yMXNDZ2hNUnZNfHAyMW0xbGs3Smx3SWtcUUdNc3dPUGZOdnNMa25xbXNKdkRffGN8N21gPU5cNTVWfzdBYVFiUicpJ2N3amhWYHdzYHcnP3F3cGApJ2lkfGpwcVF8dWAnPyd2bGtiaWBabHFgaCcpJ2BrZGdpYFVpZGZgbWppYWB3dic%2FcXdwYHgl'
                fetch("http://127.0.0.1:8000/en/order/payment/", {
                    method: "POST",
                    credentials: 'include',
                    headers: {
                        'X-CSRFToken': csrftoken,
                        'Authorization': `Bearer ${localStorage.getItem('token')}`,
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': 'http://127.0.0.1:8000',
                        'Access-Control-Allow-Credentials': true,
            },
                })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (session) {
                        return stripe.redirectToCheckout({ sessionId: session.id });
                    })
                    .then(function (result) {
                        // If redirectToCheckout fails due to a browser or network
                        // error, you should display the localized error message to your
                        // customer using error.message.
                        if (result.error) {
                            alert(result.error.message);
                        }
                    })
                    .catch(function (error) {
                        console.error("Error:", error);
                    });
            });
    }
}
