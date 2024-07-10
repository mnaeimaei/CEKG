import * as a3Module from "./A3_preview_Module.js";
import * as progressBarModule from "./A0_webSocketProgressBar_Module.js";

document.addEventListener('DOMContentLoaded', function () {

    console.log("Document 3 is ready!");
    console.log(a3Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(a3Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    a3Module.updateDropdownVisibility(a3Module.optionsToShow, a3Module.optionsToShowDefault);


    const ws = progressBarModule.setupWebSocketProgressBar(a3Module.progressBar);

    progressBarModule.handleFormSubmission(ws, a3Module.nextButton2FormSubmit, a3Module.form3);



});
