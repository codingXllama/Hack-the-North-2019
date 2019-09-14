var loginButton = document.getElementById('login-btn');
var signupButton = document.getElementById('signup-btn');
var loginForm = document.getElementById('login-form');
var signupForm = document.getElementById('signup-form');

signupForm.style.display = 'none';
signupButton.style.fontWeight = '300';

loginButton.addEventListener('click', function () {
    loginForm.style.display = 'grid';
    loginButton.style.fontWeight = '800';
    signupForm.style.display = 'none';
    signupButton.style.fontWeight = '300';
})

signupButton.addEventListener('click', function () {
    loginForm.style.display = 'none';
    loginButton.style.fontWeight = '300';
    signupForm.style.display = 'grid';
    signupButton.style.fontWeight = '800';
})