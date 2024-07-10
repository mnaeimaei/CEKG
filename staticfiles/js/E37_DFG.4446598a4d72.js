
import * as dfgModule from "./E37_DFG_Module";

dfgModule.startButton.addEventListener('click', function (event) {




    event.preventDefault();  // Prevent the default form submission
    document.getElementById('allFormDFG').submit(); // Submit the form
});
