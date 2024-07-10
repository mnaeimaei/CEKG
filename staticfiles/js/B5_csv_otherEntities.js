import * as b5Module from "./B5_csv_otherEntities_Module.js";


document.addEventListener('DOMContentLoaded', function () {

    console.log("Document 3 is ready!");
    console.log(b5Module.optionsToShow);

    console.log("Document 4 is ready!");
    console.log(b5Module.optionsToShowDefault);

    // Function to show/hide dropdowns

    b5Module.updateDropdownVisibility(b5Module.optionsToShow, b5Module.optionsToShowDefault);


    b5Module.nextButton2FormSubmit.addEventListener('click', function (event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB5').submit(); // Submit the form
    });
});
