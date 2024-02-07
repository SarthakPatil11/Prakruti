function generateOTP() {
    let otp = "";
    for (let i = 0; i < 6; i++) {
        otp += Math.floor(Math.random() * 10);
    }
    return otp;
}

function sendmail() {
    var email = document.getElementById("input_ForgetPasswordEmail").value;

    otp = generateOTP();
    emailBody = "This is your OTP : " + otp;
    Email.send({
        SecureToken: "8f05dc42-76d3-41bf-ba0a-07da1b89f398", //add your token here
        To: email,
        From: "getyourprakruti@gmail.com",
        Subject: "This is the subject",
        Body: emailBody,
    })
        .then((message) => {
            alert("Email has been sent successfully!!!" + message);
            document.getElementById("verify").style.display = "block";
            document.getElementById("OTPbtn").style.display = "none";
            $("#div_GetOTP").collapse("toggle");
            document.getElementById("verify").onclick = function () { verifyOTP(otp, email) };
        })
        .catch((error) => {
            alert(error);
        });
}

function verifyOTP(otp, email) {
    var spanWrongOTP = document.getElementById("span_msgWrongOTP");
    var Ch_otp1 = document.getElementById("otp1").value;
    var Ch_otp2 = document.getElementById("otp2").value;
    var Ch_otp3 = document.getElementById("otp3").value;
    var Ch_otp4 = document.getElementById("otp4").value;
    var Ch_otp5 = document.getElementById("otp5").value;
    var Ch_otp6 = document.getElementById("otp6").value;
    var Ch_OTP = Ch_otp1 + Ch_otp2 + Ch_otp3 + Ch_otp4 + Ch_otp5 + Ch_otp6;
    if (Ch_OTP === otp) {
        $("#div_ForgetPassModal").modal("hide");
        $("#div_ChangePassModal").modal("show");
        document.getElementById('input_chPassMail').value = email;
        spanWrongOTP.style.display = "none";
    } else {
        spanWrongOTP.style.display = "block";
    }
}

function clickEvent(prev, first, last) {
    if (first.value.length) {
        document.getElementById(last).focus();
    } else if (first.value.length == 0) {
        document.getElementById(prev).focus();
    }
}