let existingAccounts = {};
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

document.querySelector('.login-btn').addEventListener('click', function () {
    document.querySelector('.login-form').style.display = 'block';
});
document.querySelector('#user-login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    let email = document.querySelector('#user-email').value;
    let password = document.querySelector('#user-password').value;
    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }
    window.location.href = '/homepage'; 
});
