
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
                }
                quantityAlert.style.display = 'block'
                quantityAlert.innerHTML = data.message
                setTimeout(() => {
                    quantityAlert.style.display = 'none'
                }, 1000);
            });
    }
}

subscriber_form = document.getElementById("subscriber_form")
subscriber_form.onclick = function () {
    const email = document.getElementById("id_email").value
    SubscriberLogic.subscribeManager(email);
}

id_email = document.getElementById("id_email")
id_email.onkeyup = function () {
    subscriber_form = document.getElementById("subscriber_form")
    if (id_email.value != '') {
        subscriber_form.disabled = false
    } else {
        subscriber_form.disabled = true
    }
}