import * as b8Module from "./B8_csv_Domain_Module.js";



document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b8Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b8Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b8Module.updateDropdownVisibility(b8Module.optionsToShow, b8Module.optionsToShowDefault);

    b8Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB8').submit(); // Submit the form
        });
    });
