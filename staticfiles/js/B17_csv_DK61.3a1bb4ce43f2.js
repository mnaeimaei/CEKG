import * as b17Module from "./B17_csv_DK61_Module.js";

document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b17Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b17Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b17Module.updateDropdownVisibility(b17Module.optionsToShow, b17Module.optionsToShowDefault);

    b17Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB17').submit(); // Submit the form
        });
    });
