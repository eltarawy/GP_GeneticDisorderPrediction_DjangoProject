document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const btn = document.getElementById("btn");

    btn.addEventListener("click", function (event) {
        // Prevent the default form submission
        event.preventDefault();

        // Call your custom validation function
        if (validateForm()) {
            // If validation passes, submit the form
            form.submit();
        }
    });

    function validateForm() {
        // Implement your custom validation logic here
        // Return true if the form is valid, false otherwise

        // Example: Check if the age is a positive number
        const ageInput = document.querySelector("input[name='a']");
        const ageValue = parseInt(ageInput.value, 10);

        if (isNaN(ageValue) || ageValue <= 0) {
            alert("Please enter a valid age.");
            return false;
        }

        // Add more validation logic as needed

        return true;  // Form is valid
    }
});
