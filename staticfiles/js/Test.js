function handleFormSubmission(ws,nextButton2FormSubmit, formName) {
    nextButton2FormSubmit.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // WebSocket connection must be established and listening before the form is submitted
        if (ws.readyState === WebSocket.OPEN) {
            console.log("WebSocket.OPEN");
            formName.submit(); // Submit the form
        } else {
            console.log("WebSocket.else");
            ws.onopen = function () {
            formName.submit(); // Submit the form
            };
        }
    });
}