import * as LoginModule from "./A00_Login_Module.js";

document.addEventListener('DOMContentLoaded', function() {
    console.log("Login is ready!");

    // Form submission handler
    document.getElementById('allForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get username and password from input fields
        const username = LoginModule.userNameBox.value;
        const password = LoginModule.passWordBox.value;

            console.log(username);
    console.log(password);

        // Basic validation

        console.log(username);
        console.log(password);
        // Check if username and password are both 'testbpm'
        if ((username === 'testbpm') && (password === 'testbpm')) {

            console.log('User is successfully logged in.');
            // Here, you might redirect the user or change the state of your application
            // window.location.href = '/home'; // Redirect to another page

        document.getElementById('allForm').submit(); // Submit the form


        } else {
            window.alert('Invalid username or password.');
            console.log('Failed login attempt.');
        }
    });



});
