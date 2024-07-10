import * as startModule from "./A000_Directory_Module.js";

document.addEventListener('DOMContentLoaded', function() {
    console.log("Login is ready!");

    // Form submission handler
    startModule.startButton.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allForm').submit(); // Submit the form


        });



});
