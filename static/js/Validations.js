var btnSubmit = document.getElementById("btn_Submit");
//email input_Phone valid
function validate_email(input_Email) {
  email = document.getElementById(input_Email);
  var validRegex =
    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (validRegex.test(email.value)) {
    $.ajax({
      type: "GET",
      url: "/mailCheck/",
      data: { email: email.value },
      success: function callback(response) {
        /* do whatever with the response */
        if (response == "True") {
          btnSubmit.disabled = true;
          document.getElementById("signup_email_exist").style.display = "block";
          email.style.border = "1px solid red";
        } else {
          btnSubmit.disabled = false;
          document.getElementById("signup_email_exist").style.display = "none";
          email.style.border = "none";
        }
        console.log(response);
      },
    });
  } else {
    email.style.border = "1px solid red";
    btnSubmit.disabled = true;
  }
}

function validate_UName() {
  var userName = document.getElementById('input_UserName').value;
  // console.log(uname);
  $.ajax({
    type: "GET",
    url: "/unameCheck/",
    data: { uname: userName },
    success: function callback(response) {
      /* do whatever with the response */
      if (response == 'True') {
        btnSubmit.disabled = true;
        document.getElementById("div_msgUserNameExist").style.display = "block";
      } else {
        btnSubmit.disabled = false;
        document.getElementById("div_msgUserNameExist").style.display = "none";
      }
    },
  });
}

function validate_phone() {
  input_Phone = document.getElementById("input_Phone");
  var validRegex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
  if (validRegex.test(input_Phone.value)) {
    input_Phone.style.border = "none";
    document.getElementById("div_msgPhoneNumber").style.display = "none";
    btnSubmit.disabled = false;
  } else {
    input_Phone.style.border = "1px solid red";
    document.getElementById("div_msgPhoneNumber").style.display = "block";
    btnSubmit.disabled = true;
  }
}

function validate_pass(inputPassword) {
  var msgPassNotMatch = document.getElementById("div_msgPassNotMatch");
  var msgPassRules = document.getElementById("div_msgPassRules");
  
  var input_Password = document.getElementById(inputPassword);
  
  msgPassNotMatch.style.display = "none";
  var validRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$/;
  if (validRegex.test(input_Password.value)) {
    input_Password.style.border = "none";
    msgPassRules.style.display = "none";
    btnSubmit.disabled = false;
  } else {
    input_Password.style.border = "1px solid red";
    msgPassRules.style.display = "block";
    btnSubmit.disabled = true;
  }
}

function validate_cpass(inputPassword, inputConfirmPassword) {
  var msgPassNotMatch = document.getElementById("div_msgPassNotMatch");
  
  var input_Password = document.getElementById(inputPassword);
  var input_ConfirmPassword = document.getElementById(inputConfirmPassword);
  
  if (input_Password.value != "") {
    input_ConfirmPassword.style.border = "none";
    if (input_ConfirmPassword.value === input_Password.value) {
      msgPassNotMatch.style.display = "none";
      btnSubmit.disabled = false;
    } else {
      msgPassNotMatch.style.display = "block";
      btnSubmit.disabled = true;
    }
  } else {
    input_ConfirmPassword.style.border = "1px solid red";
    btnSubmit.disabled = true;
  }
}

function validateImage() {
  var input_File = document.getElementById("input_File");
  var img_DP = document.getElementById("img_DP");
  if (input_File) {
    var filePath = input_File.value;
    // Allowing file type
    var allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;

    if (!allowedExtensions.exec(filePath)) {
      alert("Invalid file type");
      input_File.value = "";
      img_DP.src = "";
      btnSubmit.disabled = true;
    } else {
      // Image preview
      if (input_File.files && input_File.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
          img_DP.src = e.target.result;
        };
        reader.readAsDataURL(input_File.files[0]);
        btnSubmit.disabled = false;
      }
    }
  } else {
    console.log(input_File);
  }
}

function validateAge() {
  age = document.getElementById("input_Age");
  if (age.value > 0) {
    age.style.border = "none";
    btnSubmit.disabled = false;
  } else {
    age.value = "";
    age.placeholder = "Invalid Age";
    age.style.border = "1px solid red";
    btnSubmit.disabled = true;
  }
}

function validateGender() {
  gender = document.getElementById("input_Gender");
  if (gender.value > 0) {
    console.log("valid Gender");
    gender.style.border = "none";
    btnSubmit.disabled = false;
  } else {
    console.log("Invalid Gender");
    gender.value = "0";
    gender.style.border = "1px solid red";
    btnSubmit.disabled = true;
  }
}