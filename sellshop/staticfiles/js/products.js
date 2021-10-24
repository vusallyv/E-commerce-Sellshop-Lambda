products = document.getElementById("products")

function getProducts() {

    fetch('http://127.0.0.1:8000/en/api/products/')
        .then(response => {
            return response.json()
        })
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                let html = `
                        <div class="col-xs-12 hidden-sm col-md-4">
                            <div class="single-product">
                                <div class="product-img">
                                    <a href="#">                                                        
                                        <img style="width: 270px; height: 340.25px;" src="" alt="Product Title" />
                                    </a>
                                    <div class="actions-btn">
                                        <a href="#"><i class="mdi mdi-cart"></i></a>
                                        <a href="#" data-toggle="modal" data-target="#quick-view"><i class="mdi mdi-eye"></i></a>
                                        <a href="#"><i class="mdi mdi-heart"></i></a>
                                    </div>
                                </div>
                                <div class="product-dsc">
                                    <p>
                                        <a href="#">${data[i]['title']}</a>
                                    </p>
                                    <div class="ratting">
                                        <i class="mdi mdi-star"></i>
                                        <i class="mdi mdi-star"></i>
                                        <i class="mdi mdi-star"></i>
                                        <i class="mdi mdi-star-half"></i>
                                        <i class="mdi mdi-star-outline"></i>
                                    </div>
                                    <span>$ ${data[i]['price']}</span>
                                </div>
                            </div>
                        </div>
                    `
                products.innerHTML += html

            }
        }).catch(error => {
            console.log(error);
        })

}

getProducts()