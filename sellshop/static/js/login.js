const LoginLogic = {
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
                if (data.access) {
                    localStorage.setItem('token', data.access);
                } else {
                    alert(data.detail);
                }
            })
    }
}


const submit = document.getElementById('sbmt');
const form = document.getElementById("login_form")
submit.onclick = function () {
    const username = document.querySelector('#id_username').value;
    const password = document.querySelector('#id_password').value;
    LoginLogic.fetchToken(username, password);
    setInterval(form.submit(), 1000);
}

// const rgstr = document.getElementById('rgstr');
// rgstr.onclick = function () {
//     const username = document.querySelector('#username').value;
//     const email = document.querySelector('#email').value;
//     const phone_number = document.querySelector('#id_phone_number').value;
//     const password = document.querySelector('#password').value;
//     const password_confirmation = document.querySelector('#id_confirm_password').value;
//     console.log('ok');
//     RegisterLogic.createUser(username, email, phone_number, password, password_confirmation);
// }

// const RegisterLogic = {
//     createUser(username, email, phone_number, password, password_confirmation) {
//         fetch('http://127.0.0.1:8000/en/api/user/create/', {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({
//                 "username": username,
//                 "email": email,
//                 "phone_number": phone_number,
//                 "password": password,
//                 "password_confirmation": password_confirmation,
//             })
//         })
//             .then(response => response.json())
//             .then(data => {
//                 if (data.access) {
//                     localStorage.setItem('token', data.access);
//                     window.location.href = "http://127.0.0.1:8000/en/core/index/"
//                 } else {
//                     alert(data);
//                 }
//             })
//     }
// }
