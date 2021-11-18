
const SubscriberLogic = {
    subscribeManager(email) {
        fetch(`http://127.0.0.1:8000/en/api/subscriber/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'email': email,
            })
        })
            .then(response => response.json())
            .then(data => {
                quantityAlert = document.getElementById('quantityAlert')
                if (data.success == false) {
                    quantityAlert.classList.remove("alert-success")
                    quantityAlert.classList.add("alert-danger")
                }else{
                    quantityAlert.classList.remove("alert-danger")
                    quantityAlert.classList.add("alert-success")
                }
                quantityAlert.style.display = 'block'
                quantityAlert.innerHTML = data.message
                setTimeout(() => {
                    quantityAlert.style.display = 'none'
                }, 2000);
            });
    }
}

subscriber_form = document.getElementById("subscriber_form")
subscriber_form.onclick = function () {
    const email = document.getElementById("id_email").value
    SubscriberLogic.subscribeManager(email);
}


email = document.getElementById("id_email")
email.onkeyup = function () {
    subscriber_form = document.getElementById("subscriber_form")
    if (email.value != '') {
        subscriber_form.disabled = false
    } else {
        subscriber_form.disabled = true
    }
}


const ConcactLogic = {
    contactManager(name, email, message) {
        fetch(`http://127.0.0.1:8000/en/api/contact/`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'name': name,
                'email': email,
                'message': message,
            })
        })
            .then(response => response.json())
            .then(data => {
                quantityAlert = document.getElementById('quantityAlert')
                if (data.success == false) {
                    quantityAlert.classList.remove("alert-success")
                    quantityAlert.classList.add("alert-danger")
                }else{
                    quantityAlert.classList.remove("alert-danger")
                    quantityAlert.classList.add("alert-success")
                }
                quantityAlert.style.display = 'block'
                quantityAlert.innerHTML = data.message
                setTimeout(() => {
                    quantityAlert.style.display = 'none'
                }, 2000);
            });
    }
}

contact_form = document.getElementById("contact_form")
contact_form.onclick = function () {
    const email = document.getElementById("contactEmail").value
    const name = document.getElementById("id_name").value
    const message = document.getElementById("id_message").value
    ConcactLogic.contactManager(name, email, message);
}