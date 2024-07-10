import * as b15Module from "./B15_csv_DK4_Module.js";



document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b15Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b15Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b15Module.updateDropdownVisibility(b15Module.optionsToShow, b15Module.optionsToShowDefault);


    b15Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB15').submit(); // Submit the form
        });
    });
