import * as b6Module from "./B6_csv_entityRel_Module.js";


document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b6Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b6Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b6Module.updateDropdownVisibility(b6Module.optionsToShow, b6Module.optionsToShowDefault);

    b6Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB6').submit(); // Submit the form
        });
    });
