document.addEventListener("DOMContentLoaded", function () {
    fetch('/dashboard')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert("Unauthorized access. Please log in.");
                window.location.href = "login.html"; // Redirect to login page
                return;
            }

            const tableBody = document.getElementById("dashboard-data");
            tableBody.innerHTML = "";

            data.forEach(item => {
                let row = `<tr>
                    <td>${item.full_name}</td>
                    <td>${item.email}</td>
                    <td>${item.num_tickets}</td>
                    <td>${item.visit_date}</td>
                    <td>${item.ticket_type}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Error fetching data:", error));
});
