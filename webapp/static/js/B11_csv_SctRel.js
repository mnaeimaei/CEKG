import * as b11Module from "./B11_csv_SctRel_Module.js";


document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b11Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b11Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b11Module.updateDropdownVisibility(b11Module.optionsToShow, b11Module.optionsToShowDefault);

    b11Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB11').submit(); // Submit the form
        });
    });
