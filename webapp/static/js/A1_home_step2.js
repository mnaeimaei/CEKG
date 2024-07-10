import * as p1Module  from "./A1_home_Module.js";
import {InputDivDfg6Container, InputFormDFG6RadioButtons} from "./A1_home_Module.js";


document.addEventListener('DOMContentLoaded', function() {
    console.log("Document 2 is ready!");



    p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);
        });
    });


    p1Module.Dfg1FormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);

        });
    });


    p1Module.Dfg2FormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);

        });
    });


    p1Module.Dfg3FormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);

        });
    });

    p1Module.Dfg4FormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);

        });
    });

    p1Module.Dfg5FormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);

        });
    });


    p1Module.Dfg6FormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            // Reset other DFG forms when a new selection is made in formMainDFG
            p1Module.resetForm(p1Module.InputDivContainer);
            p1Module.resetForm(p1Module.InputDivDfg6Container);

        });
    });





    const checkAndDisplayFormInput = function() {
        let selectedMainDFGOption = null;
        p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
            if (radioButton.checked) {
                selectedMainDFGOption = radioButton.value;
            }
        });

        let displayState = 0;

        switch (selectedMainDFGOption) {
            case 'dfg1Mode':
                displayState = p1Module.isAnyRadioButtonSelected(p1Module.Dfg1DivContainer) ? 1 : 0;
                break;
            case 'dfg2Mode':
                displayState = p1Module.isAnyRadioButtonSelected(p1Module.Dfg2DivContainer) ? 1 : 0;
                break;
            case 'dfg3Mode':
                displayState = p1Module.isAnyRadioButtonSelected(p1Module.Dfg3DivContainer) ? 1 : 0;
                break;
            case 'dfg4Mode':
                displayState = p1Module.isAnyRadioButtonSelected(p1Module.Dfg4DivContainer) ? 1 : 0;
                break;
            case 'dfg5Mode':
                displayState = p1Module.isAnyRadioButtonSelected(p1Module.Dfg5DivContainer) ? 1 : 0;
                break;
            case 'dfg6Mode':
                displayState = p1Module.isAnyRadioButtonSelected(p1Module.Dfg6ivContainer) ? 2 : 0;
                break;
            default:
                displayState = 0;
        }

        // Handle display based on the displayState value
        if (displayState === 1) {
            p1Module.InputDivContainer.style.display = 'block';
            p1Module.InputDivDfg6Container.style.display = 'none'; // Ensure the other container is hidden
        } else if (displayState === 2) {
            console.log("Displaying InputDivContainer2");
            p1Module.InputDivContainer.style.display = 'none'; // Ensure the other container is hidden
            p1Module.InputDivDfg6Container.style.display = 'block';
        } else {
            console.log("Hiding both InputDivContainer and InputDivContainer2");
            p1Module.InputDivContainer.style.display = 'none';
            p1Module.InputDivDfg6Container.style.display = 'none';
        }
    };


    // Function to check if any radio button in a form is selected



    // Attach change event listener to all radio buttons in mainDFG and DFG forms
    p1Module.MainDfgFormRadioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', checkAndDisplayFormInput);
    });

    [p1Module.Dfg1DivContainer, p1Module.Dfg2DivContainer, p1Module.Dfg3DivContainer, p1Module.Dfg4DivContainer, p1Module.Dfg5DivContainer, p1Module.Dfg6ivContainer].forEach(function(formContainer) {
        const radioButtons = formContainer.querySelectorAll('input[type="radio"]');
        radioButtons.forEach(function(radioButton) {
            radioButton.addEventListener('change', checkAndDisplayFormInput);
        });
    });
});




