//this function create a span tag and give attributes for styling
function createSpan(text){
        const main_div = document.querySelector(`input.${text}`).parentElement;
        const error_span = document.createElement("span");
        error_span.setAttribute("class", "error-span");
        error_span.setAttribute("id", `error-${text}`)
        main_div.appendChild(error_span);
        return error_span;   
}

//function to validate name input
function nameValidation(text){
    let valid = true;
    const pattern = /[a-zA-Z]/;
    const name = document.querySelector(`input.${text}`);
    let error_span = document.querySelector(`span#error-${text}`);
    //only create span tag if there doesn't already exists
    //this is to avoid showing multiple success message
    if (error_span == null){
        error_span  = createSpan(text);
        error_span.innerText = "Invalid Name: Name must be between 3 and 25 characters";
    }
    else{
        if (name.value == "" || name.value.length < 3 || name.value.length > 25 || !pattern.test(name.value)){
            name.style.border = "2px solid red";
            error_span.style.display = "block";
            valid = false;
        }
        else{
            error_span.style.display = "none";
            name.style.border = "2px solid green";
            valid = true;
            error_span.remove();
        }
    }
    //make first letter of the name capital
    name.value = name.value.charAt(0).toUpperCase() + name.value.slice(1);
    return valid;
}

//function to validate input email
function validateEmail(text){
    //email regular expression pattern
    const pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let valid = true;
    const email = document.querySelector(`input.${text}`);
    let error_span = document.querySelector(`span#error-${text}`);
    //only create span tag if there doesn't already exists
    //this is to avoid showing multiple success message
    if (error_span == null){
        error_span  = createSpan(text);
        error_span.innerText = "Invalid Email";
    }
    else{
        if (email.value === "" || !pattern.test(email.value)){
            email.style.border = "2px solid red";
            error_span.style.display = "block";
            valid = false;  
        }
        else{
            error_span.style.display = "none";
            email.style.border = "2px solid green";
            valid = true;
            error_span.remove(); 
        }   
    }
    return valid;
}

function validateDateofBirth(text){
    let valid = true;
    const dob = document.querySelector(`input.${text}`);
    //making the input date data as a date format
    let dobDate = new Date(dob.value);
    //calculating difference between now and the date entered date of birth
    let diff = Date.now() - dobDate.getTime();
    let ageDate = new Date(diff)
    let age = Math.abs(ageDate.getUTCFullYear() - 1970);
    let error_span = document.querySelector(`span#error-${text}`);
    //only create span tag if there doesn't already exists
    //this is to avoid showing multiple success message
    if (error_span == null){
        error_span  = createSpan(text);
        error_span.innerText = "This position is for age above 18";
    }
    else{
        if (dob.value == "" ||age >=18 && age <=85){
            error_span.style.display = "none";
           dob.style.border = "2px solid green";
           valid = true;
           error_span.remove()
           
        }
        else{
            dob.style.border = "2px solid red";
            error_span.style.display = "block";
            valid = false;   
        }
    }
    return valid;
}

//function to validate frontend phone number
function validatePhoneNumber(text){
    let valid = true;
    const pattern = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/; //phone number pattern
    const phoneNumber = document.querySelector(`input.${text}`);
    let error_span = document.querySelector(`span#error-${text}`);
    //only create span tag if there doesn't already exists
    //this is to avoid showing multiple success message
    if (error_span == null){
        error_span  = createSpan(text);
        error_span.innerText = "Invalid Phone number";
    }
    else{
        if (phoneNumber.value == "" ||!pattern.test(phoneNumber.value)){
            phoneNumber.style.border = "2px solid red";
            error_span.style.display = "block";
            valid = false;  
        }
        else{
            error_span.style.display = "none";
            phoneNumber.style.border = "2px solid green";
            valid = true;
            error_span.remove();
        }
    }
    return valid;
}

//function to show success message
function showMesage(){
    const msg = document.querySelector("div.success-msg");
    msg.style.display = "block";
}

//function to remove success message when clicking the close button
function removeMsg(){
    const msg = document.querySelector("div.success-msg");
    msg.style.display = "none";
}
