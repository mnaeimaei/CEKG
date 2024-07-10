import * as b19Module from "./B19_csv_DK7_Module.js";



document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b19Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b19Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b19Module.updateDropdownVisibility(b19Module.optionsToShow, b19Module.optionsToShowDefault);


    b19Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB19').submit(); // Submit the form
        });
    });
