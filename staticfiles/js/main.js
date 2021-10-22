
// Delete confirm function
function confirmAction( ){
    const reqField = document.getElementById("article-confirm__title"); // geting title to confirm
    const inputField = document.getElementById("article-confirm__input"); // input that user entered
    const buttonField = document.getElementById("article-confirm__button"); // delete button
    const checkField = document.getElementById("checkconfirm"); // Check button
    console.log('title',reqField.innerHTML); // cheking data
    console.log('input',inputField.value); 
    if (reqField.innerHTML == inputField.value) {
    buttonField.disabled = false;
    buttonField.classList.remove("btn-outline-danger");
    buttonField.classList.add("btn-danger");
    inputField.disabled = true;
    checkField.disabled = true;
    }else{
        buttonField.disabled = true;
    };
};