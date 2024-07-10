import * as b10Module from "./B10_csv_SctNode_Module.js";

document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b10Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b10Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b10Module.updateDropdownVisibility(b10Module.optionsToShow, b10Module.optionsToShowDefault);

    b10Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB10').submit(); // Submit the form
        });
    });
