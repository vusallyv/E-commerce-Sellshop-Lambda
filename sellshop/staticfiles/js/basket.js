cart_items = document.getElementById("cart-items")

url = String(window.location.href).split("/")
function getProducts() {

    fetch('http://127.0.0.1:8000/en/api/carts/')
        .then(response => {
            return response.json()
        })
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                if (url[url.length-2] == 1) {
                    
                    console.log(data[0]['productversion'][0]);
                }
            }
            cart_items.innerHTML = `
                                    <i class="mdi mdi-cart"></i>
                                    ${data[0]['productversion'][0].length} items : <strong>$ </strong>
            `
        }).catch(error => {
            console.log(error);
        })

}

getProducts();