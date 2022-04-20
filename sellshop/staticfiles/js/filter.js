category_name = document.getElementsByName('category_name')

category_name.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('category_name') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&category_name=${element.innerText}`;
            } else {
                window.location.href += `?category_name=${element.innerText}`;
            }
        } else {
            window.location.href = window.location.href.replace(/category_name=.*?(&|$)/, `category_name=${element.innerText}$1`);
        }
    })
});


subcategory_name = document.getElementsByName('subcategory_name')

subcategory_name.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('subcategory_name') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&subcategory_name=${element.innerText}`;
            } else {
                window.location.href += `?subcategory_name=${element.innerText}`;
            }
        } else {
            window.location.href = window.location.href.replace(/subcategory_name=.*?(&|$)/, `subcategory_name=${element.innerText}$1`);
        }
    })
});


size = document.getElementsByName('size')

size.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('size') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&size=${element.innerText}`;
            } else {
                window.location.href += `?size=${element.innerText}`;
            }
        } else {
            window.location.href = window.location.href.replace(/size=.*?(&|$)/, `size=${element.innerText}$1`);
        }
    })
});

color = document.getElementsByName('color')

color.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('color') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&color=${element.getAttribute('color')}`;
            } else {
                window.location.href += `?color=${element.getAttribute('color')}`;
            }
        } else {
            window.location.href = window.location.href.replace(/color=.*?(&|$)/, `color=${element.getAttribute('color')}$1`);
        }
    })
});


brand = document.getElementsByName('brand')


brand.forEach(element => {
    element.addEventListener('click', function () {
        if (window.location.href.includes('brand') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&brand=${element.innerText}`;
            } else {
                window.location.href += `?brand=${element.innerText}`;
            }
        } else {
            window.location.href = window.location.href.replace(/brand=.*?(&|$)/, `brand=${element.innerText}$1`);
        }
    })
});


first_last = document.getElementsByClassName('first-last')

for (let i = 0; i < first_last.length; i++) {
    first_last[i].addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${first_last[i].getAttribute('page')}`;
            } else {
                window.location.href += `?page=${first_last[i].getAttribute('page')}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${first_last[i].getAttribute('page')}$1`);
        }
    })
}

page_num = document.getElementsByClassName('page_num')


for (let i = 0; i < page_num.length; i++) {
    page_num[i].addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${page_num[i].innerText}`;
            } else {
                window.location.href += `?page=${page_num[i].innerText}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${page_num[i].innerText}$1`);
        }
    })
}

previous = document.getElementById('previous')
if (previous) {
    previous.addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${previous.getAttribute('page')}`;
            } else {
                window.location.href += `?page=${previous.getAttribute('page')}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${previous.getAttribute('page')}$1`);
        }
    })
}

next = document.getElementById('next')
if (next) {
    next.addEventListener('click', function () {
        if (window.location.href.includes('page') == false) {
            if (window.location.href.includes('?')) {
                window.location.href += `&page=${next.getAttribute('page')}`;
            } else {
                window.location.href += `?page=${next.getAttribute('page')}`;
            }
        } else {
            window.location.href = window.location.href.replace(/page=.*?(&|$)/, `page=${next.getAttribute('page')}$1`);
        }
    })
}
try {
    filterURL = window.location.href.split('?')[1].split('&')
    for (let i = 0; i < filterURL.length; i++) {
        if (window.location.href.includes(filterURL[i])) {
            console.log(filterURL[i]);
            for (let j = 0; j < subcategory_name.length; j++) {
                if (subcategory_name[j].innerText == filterURL[i].split('=')[1]) {
                    subcategory_name[j].style.color = '#fe5858';
                }
            }
            for (let j = 0; j < brand.length; j++) {
                if (brand[j].innerText == filterURL[i].split('=')[1]) {
                    brand[j].style.color = '#fe5858';
                }
            }
            for (let j = 0; j < size.length; j++) {
                if (size[j].innerText == filterURL[i].split('=')[1]) {
                    size[j].style.color = '#ffffff';
                    size[j].style.background = '#fe5858 none repeat scroll 0 0';
                }
            }
            if (filterURL[i].split('=')[0] == 'min_price') {
                min_price.value = filterURL[i].split('=')[1]
            }
            if (filterURL[i].split('=')[0] == 'max_price') {
                max_price.value = filterURL[i].split('=')[1]
            }
        }
    }
} catch (error) {
}



min_price = document.getElementById('min_price')
min_price.addEventListener('change', function () {
    console.log('salam');
    if (window.location.href.includes('min_price') == false) {
        if (window.location.href.includes('?')) {
            window.location.href += `&min_price=${min_price.value}`;
        } else {
            window.location.href += `?min_price=${min_price.value}`;
        }
    } else {
        window.location.href = window.location.href.replace(/min_price=.*?(&|$)/, `min_price=${min_price.value}$1`);
    }
})


max_price = document.getElementById('max_price')
max_price.addEventListener('change', function () {
    if (window.location.href.includes('max_price') == false) {
        if (window.location.href.includes('?')) {
            window.location.href += `&max_price=${max_price.value}`;
        } else {
            window.location.href += `?max_price=${max_price.value}`;
        }
    } else {
        window.location.href = window.location.href.replace(/max_price=.*?(&|$)/, `max_price=${max_price.value}$1`);
    }
})
