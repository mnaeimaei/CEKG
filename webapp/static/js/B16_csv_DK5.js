import * as b16Module from "./B16_csv_DK5_Module.js";


document.addEventListener('DOMContentLoaded', function() {


    console.log("Document 3 is ready!");
    console.log(b16Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b16Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b16Module.updateDropdownVisibility(b16Module.optionsToShow, b16Module.optionsToShowDefault);

    b16Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB16').submit(); // Submit the form
        });
    });
