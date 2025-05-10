// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");

    // Form validation function
    loginForm.addEventListener("submit", function (event) {
        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();
        const rememberMe = document.getElementById("rememberMe").checked;

        // Validate Username (at least 3 characters)
        if (username.length < 3) {
            alert("Username must be at least 3 characters long.");
            event.preventDefault(); // Stop form submission

            return false;
        }

        // Validate Password (at least 6 characters)
        if (password.length < 6) {
            alert("Password must be at least 6 characters long.");
            event.preventDefault();
            return false;
        }

        // Remember Me checkbox (Optional)
        if (rememberMe) {
            alert("We'll remember you next time!");
        }

        // Success Message (If all validations pass)
        alert("Login successful! Welcome back to Carnival Kingdom 🎪");
        return true;
        
    });
    // if (username === "mohamedkaamil" && password === "12345") {
    //     // Redirect to the user dashboard or another page
    //     window.location.href = "dashboard.html"; // Change to the correct page URL
    // } else {
    //     alert("Invalid username or password!");
    // }
    
});
