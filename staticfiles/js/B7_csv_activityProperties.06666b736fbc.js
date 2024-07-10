import * as b7Module from "./B7_csv_activityProperties_Module.js";

document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b7Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b7Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b7Module.updateDropdownVisibility(b7Module.optionsToShow, b7Module.optionsToShowDefault);

    b7Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB7').submit(); // Submit the form
        });
    });
