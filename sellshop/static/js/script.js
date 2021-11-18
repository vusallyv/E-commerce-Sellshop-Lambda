size = document.getElementsByName('size')
for (let i = 0; i < size.length; i++) {
    if (size[i].classList.contains("active") && window.location.href.includes(`size=${size[i].innerText}`)) {
        size[i].style.background = "#fe5858 none repeat scroll 0 0";
        size[i].style.borderColor = "transparent";
        size[i].style.color = "#fff";
        size[i].addEventListener("click", function () {
            current_url = window.location.href
            url_arr = current_url.split("?")
            url_filters = url_arr[1].split("&")
            new_arr = []
            for (let j = 0; j < url_filters.length; j++) {
                if (url_filters[j].includes(`size=${size[i].innerText}`) == false) {
                    new_arr.unshift(url_filters[j])
                }
            }
            window.location.href = `?${new_arr.join('&')}`;
        });
    }
}

brand = document.getElementsByName('brand')
for (let i = 0; i < brand.length; i++) {
    if (brand[i].classList.contains("active") && window.location.href.includes(`brand=${brand[i].innerText}`)) {
        brand[i].style.color = "#fe5858"
        brand[i].addEventListener("click", function () {
            current_url = window.location.href
            url_arr = current_url.split("?")
            url_filters = url_arr[1].split("&")
            new_arr = []
            for (let j = 0; j < url_filters.length; j++) {
                if (url_filters[j].includes(`brand=${brand[i].innerText}`) == false) {
                    new_arr.unshift(url_filters[j])
                }
            }
            window.location.href = `?${new_arr.join("&")}`;
        });
    }
}



category_name = document.getElementsByName('category_name')
for (let i = 0; i < category_name.length; i++) {
    if (category_name[i].classList.contains("active") && window.location.href.includes(`category=${category_name[i].innerText}`)) {
        category_name[i].style.color = "#fe5858"
        category_name[i].addEventListener("click", function () {
            current_url = window.location.href
            url_arr = current_url.split("?")
            url_filters = url_arr[1].split("&")
            new_arr = []
            for (let j = 0; j < url_filters.length; j++) {
                if (url_filters[j].includes(`category=${category_name[i].innerText}`) == false) {
                    new_arr.unshift(url_filters[j])
                }
            }
            window.location.href = `?${new_arr.join("&")}`;
        });
    }
}



subcategory_name = document.getElementsByName('subcategory_name')
for (let i = 0; i < subcategory_name.length; i++) {
    if (subcategory_name[i].classList.contains("active")) {
        subcategory_name[i].style.color = "#fe5858"
        subcategory_name[i].addEventListener("click", function () {
            current_url = window.location.href
            url_arr = current_url.split("?")
            url_filters = url_arr[1].split("&")
            new_arr = []
            for (let j = 0; j < url_filters.length; j++) {
                if (url_filters[j].includes(`subcategory=${subcategory_name[i].innerText}`) == false) {
                    new_arr.unshift(url_filters[j])
                }
            }
            window.location.href = `?${new_arr.join("&")}`;
        });
    }
}