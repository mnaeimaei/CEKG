import * as b14Module from "./B14_csv_DK3_Module.js";


document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b14Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b14Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b14Module.updateDropdownVisibility(b14Module.optionsToShow, b14Module.optionsToShowDefault);

    b14Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB14').submit(); // Submit the form
        });
    });
