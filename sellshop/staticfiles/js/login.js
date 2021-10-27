const LoginLogic = {
    'url': `${location.origin}/api/token/`,

    fetchToken(username, password) {
        fetch(this.url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                'username': username,
                'password': password
            })
        }).then(response => response.json()).then(data => {
            localStorage.setItem('data', data);
            console.log(data);
            if (data.access) {
                localStorage.setItem('token', data.access);
            } else {
                alert(data.message);
            }
        })
    }
}


    const submit = document.getElementById('sbmt');

    submit.onclick = function () {
        const username = document.querySelector('#id_username').value;
        const password = document.querySelector('#id_password').value;
        LoginLogic.fetchToken(username, password);
        setInterval(form.submit(), 1000);
    }
