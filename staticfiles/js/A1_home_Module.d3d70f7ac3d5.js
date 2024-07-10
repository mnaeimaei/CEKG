    const AllFormContainer = document.getElementById('allForm');

    export const MainDfgFormRadioButtons = document.querySelectorAll('#mainDfgDiv input[name="mainDfgMode"]');
    export const Dfg1FormRadioButtons = document.querySelectorAll('#dFG1Div input[name="dfg1Mode"]');
    export const Dfg2FormRadioButtons = document.querySelectorAll('#dFG2Div input[name="dfg2Mode"]');
    export const Dfg3FormRadioButtons = document.querySelectorAll('#dFG3Div input[name="dfg3Mode"]');
    export const Dfg4FormRadioButtons = document.querySelectorAll('#dFG4Div input[name="dfg4Mode"]');
    export const Dfg5FormRadioButtons = document.querySelectorAll('#dFG5Div input[name="dfg5Mode"]');
    export const Dfg6FormRadioButtons = document.querySelectorAll('#dFG6Div input[name="dfg6Mode"]');
    export const InputFormRadioButtons = document.querySelectorAll('#inputDiv input[name="inputMode"]');
    export const InputFormDFG6RadioButtons = document.querySelectorAll('#inputDivForDFG6 input[name="inputModeDFG6"]');
    export const ActivityFormRadioButtons = document.querySelectorAll('#activityDiv input[name="activityMode"]');
    export const ActivityFormRadioButtonsDFG6 = document.querySelectorAll('#activityDivDFG6 input[name="activityModeDFG6"]');
    export const nextButton1FormSubmit = document.querySelectorAll('#nextButton1Div input[name="nextButton1Mode"]');


    export const MainDfgDivContainer = document.getElementById('mainDfgDiv');
    export const Dfg1DivContainer = document.getElementById('dFG1Div');
    export const Dfg2DivContainer = document.getElementById('dFG2Div');
    export const Dfg3DivContainer = document.getElementById('dFG3Div');
    export const Dfg4DivContainer = document.getElementById('dFG4Div');
    export const Dfg5DivContainer = document.getElementById('dFG5Div');
    export const Dfg6ivContainer = document.getElementById('dFG6Div');
    export const InputDivContainer = document.getElementById('inputDiv');
    export const InputDivDfg6Container = document.getElementById('inputDivForDFG6');
    export const ActivityDivContainer = document.getElementById('activityDiv');

    export const ActivityDivContainerDFG6 = document.getElementById('activityDivDFG6');

    export const nextButton1DivContainer = document.getElementById('nextButton1Div');





    export const ActivityFormSCT_DistanceDiv = document.getElementById('activityFormSCT_DistanceDiv');
    



    function resetForm(divContainer) {
        const radioButtons = divContainer.querySelectorAll('input[type="radio"]');
        if (radioButtons) {
            radioButtons.forEach(function(element) {
                element.checked = false;
            });
        }
    }

    export { resetForm };



    function resetTextBoxes(divContainer) {
        const textBoxes = divContainer.querySelectorAll('input[type="text"]');
        textBoxes.forEach(function(textBox) {
            textBox.value = '';
        });
    }

    export { resetTextBoxes };


        function isAnyRadioButtonSelected(formContainer) {
        const radioButtons = formContainer.querySelectorAll('input[type="radio"]');
        return Array.from(radioButtons).some(radioButton => radioButton.checked);
    }

    export { isAnyRadioButtonSelected };

    function toggleFieldVisibility(fieldName, isVisible) {
        var field = document.querySelector('[name="' + fieldName + '"]');
        if (field) {
            if (isVisible) {
                field.style.display = 'block';
                field.setAttribute('required', ''); // Make it required when visible
            } else {
                field.style.display = 'none';
                field.removeAttribute('required'); // Remove required when hidden
                       }
                     }
           }
    export { toggleFieldVisibility };
