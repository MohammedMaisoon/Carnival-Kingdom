document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("signupForm").addEventListener("submit", function (event) {
        let username = document.getElementById("username").value.trim();
        let email = document.getElementById("email").value.trim();
        let password = document.getElementById("password").value;
        let confirmPassword = document.getElementById("confirm-password").value;
        let termsChecked = document.getElementById("terms").checked;

        // Username validation
        if (username.length < 3) {
            alert("Username must be at least 3 characters long.");
            event.preventDefault(); // Prevent form submission
            return false;
        }

        // Email validation
        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            event.preventDefault();
            return false;
        }

        // Password validation (at least 6 characters)
        if (password.length < 6) {
            alert("Password must be at least 6 characters long.");
            event.preventDefault();
            return false;
        }

        // Confirm password validation
        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            event.preventDefault();
            return false;
        }

        // Terms and conditions validation
        if (!termsChecked) {
            alert("You must agree to the Terms and Conditions.");
            event.preventDefault();
            return false;
        }

        // If all validations pass, allow form submission
        alert("Sign-up successful! Welcome to Carnival Kingdom 🎉");
        return true;
    });
});
