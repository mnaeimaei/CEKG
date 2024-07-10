import * as a4Module from "./B4_csv_EventLog_Module.js";





document.addEventListener('DOMContentLoaded', function () {

    console.log("Document event Log is ready!");
    console.log(a4Module.optionsToShowB41);
    console.log(a4Module.optionsToShowB42);
    console.log(a4Module.buttonToShowB41);
    console.log(a4Module.buttonToShowB42);






    a4Module.updateDropdownVisibility(a4Module.buttonToShowB41, a4Module.optionsToShowB41,a4Module.buttonToShowB42,a4Module.optionsToShowB42);


    a4Module.nextButton2FormSubmit.addEventListener('click', function (event) {
        event.preventDefault();  // Prevent the default form submission
        document.getElementById('allFormB4').submit(); // Submit the form
    });

});