async function register() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    const response = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const result = await response.json();
    alert(result.message);
}

async function otpLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    const response = await fetch('/otp-login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const result = await response.json();
    alert(result.message);
}

async function faceLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    const response = await fetch('/face-login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const result = await response.json();
    alert(result.message);
}
