var myInput = document.getElementById("reset_password");
var mypasswordAgain = document.getElementById("reset_password_again");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var passwordAgain = document.getElementById("lengthPasswordAgain");

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
    document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
    document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }

    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    // Validate length
    if (myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }

    mypasswordAgain.onfocus = function() {
        document.getElementById("passwordAgainMessage").style.display = "block";
    }

    mypasswordAgain.onkeyup = function() {
        //alert(myInput.value + ' ' + mypasswordAgain.value);
        if (myInput.value == mypasswordAgain.value) {
            lengthPasswordAgain.classList.remove("invalid");
            lengthPasswordAgain.classList.add("valid");
            document.getElementById("lengthPasswordAgain").innerHTML = "Password Match";
        } else {
            lengthPasswordAgain.classList.remove("valid");
            lengthPasswordAgain.classList.add("invalid");
            document.getElementById("lengthPasswordAgain").innerHTML = "Password does not match";
        }
    }
}