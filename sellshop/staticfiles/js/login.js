const LoginLogic = {
    url: `${location.origin}/api/token/`,

    fetchToken(username, password) {
        fetch('http://127.0.0.1:8000/en/api/token/', {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                "username": username,
                "password": password
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(username, password);
            console.log(data);
            if (data.access) {
                localStorage.setItem('token', data.access);
            } else {
                alert(data.detail);
    }
}) }
}


    const submit = document.getElementById('sbmt');
    const form = document.getElementById("login_form")
    submit.onclick = function () {
        const username = document.querySelector('#id_username').value;
        const password = document.querySelector('#id_password').value;
        LoginLogic.fetchToken(username, password);
        setInterval(form.submit(), 1000);
    }


function testCard(token) {
    fetch('http://127.0.0.1:8000/en/api/cart/', {
        method: 'POST',
        headers : {
            'Authorization' : `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
}