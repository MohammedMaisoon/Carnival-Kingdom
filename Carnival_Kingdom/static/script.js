document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        try {
            const response = await fetch("/ticket_booking", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                alert("🎉 Your tickets have been booked successfully!");
                form.reset(); // Clears the form
            } else {
                alert("Error: " + result.error);
            }
        } catch (error) {
            console.error("Error:", error);
            alert("🎉 Your tickets have been booked successfully!");
        }
    });
});
