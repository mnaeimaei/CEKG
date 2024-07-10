import * as b18Module from "./B18_csv_DK62_Module.js";



document.addEventListener('DOMContentLoaded', function() {

    console.log("Document 3 is ready!");
    console.log(b18Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b18Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b18Module.updateDropdownVisibility(b18Module.optionsToShow, b18Module.optionsToShowDefault);

    b18Module.nextButton2FormSubmit.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB18').submit(); // Submit the form
        });
    });
