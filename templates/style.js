document.getElementById('loginForm').addEventListener('submit', function(e){e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;


    const validUsername = 'admin';
    const validPassword = '1234';

   

    if (username === validUsername && password === validPassword){
        localStorage.setItem('loggedIn', 'true');
        window.location.href = "app.html";
    }

    else {
        document.getElementById('error').innerText = 'Invalid username or password!';
    }

});
