const AllFormContainer = document.getElementById('allForm2');

export const fileSourceForm = document.querySelectorAll('#fileSourceDiv input[name="browsingMethodMode"]');
export const fileNameForm = document.querySelector('#fileNameDiv input[name="fileNameMode"]');
export const fileLocationForm = document.querySelector('#locationDiv input[name="locationTextMode"]');

export const fileKeyForm = document.querySelector('#serviceDiv input[name="serviceKeyTextMode"]');
export const nextButton2FormSubmit = document.querySelector('#nextButton2Div input[name="nextButton1Mode"]');





export const fileSourceDivContainer = document.getElementById('fileSourceDiv');
export const fileNameDivContainer = document.getElementById('fileNameDiv');
export const fileLocationDivContainer = document.getElementById('locationDiv');

export const fileKeyDivContainer = document.getElementById('serviceDiv');
export const nextButton2DivContainer = document.getElementById('nextButton2Div');



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


function isTextBoxFilled(formContainer) {
    const textInputs = formContainer.querySelectorAll('input[type="text"]');
    return Array.from(textInputs).some(input => input.value.trim() !== '');
}


export { isTextBoxFilled };


function toggleSubmitButton() {
        if (textBox.value.trim() === '') {
            // If the text box is empty, hide the submit button
            submitButton.style.display = 'none';
        } else {
            // If the text box is not empty, show the submit button
            submitButton.style.display = '';
        }
    }
export { toggleSubmitButton };

 export   const configElement = document.getElementById('config');
 export   const gDefaultFileName = configElement.getAttribute('data-g-filename');
 export   const gDefaultKey = configElement.getAttribute('data-g-key');
 export   const lDefaultFileName = configElement.getAttribute('data-l-filename');
 export   const lDefaultLocation = configElement.getAttribute('data-l-key');


 export const progressBar = document.getElementById('progressBar');

 export const progressBarContainerDiv = document.querySelector('#progressBarContainer');


export const form2 = document.getElementById('allForm2');
