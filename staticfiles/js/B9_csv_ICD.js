import * as b9Module from "./B9_csv_ICD_Module.js";



document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b9Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b9Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b9Module.updateDropdownVisibility(b9Module.optionsToShow, b9Module.optionsToShowDefault);

    b9Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB9').submit(); // Submit the form
        });
    });
