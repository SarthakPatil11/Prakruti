// Transfer blog details.
function passBlogDetails(who) {
  document.getElementById("BType").innerHTML = document.getElementById("Btype" + who).innerHTML;
  document.getElementById("Btitle").innerHTML = document.getElementById("title" + who).innerHTML;
  document.getElementById("Content").innerHTML = document.getElementById("content" + who).innerHTML;
}

// Transfer product details
function passProductDetails(who) {
  console.log(who);
  document.getElementById("PName").innerHTML = document.getElementById("name" + who).innerHTML;
  document.getElementById("PImage").src = document.getElementById("pimage" + who).src;
  document.getElementById("PDesc").innerHTML = document.getElementById("desc" + who).value;
  document.getElementById("PContents").innerHTML = document.getElementById("cont" + who).value;
  document.getElementById("Price").innerHTML = document.getElementById("price" + who).value;
  document.getElementById("Quantity").innerHTML = document.getElementById("quantity" + who).value;
  document.getElementById("buy_now").value = who;
  document.getElementById("cart").value = who;
}

// data tranfer Edit Details
function passEditUserDetails() {
  var Fname = document.getElementById("Fname");
  var Mname = document.getElementById("Mname");
  var Lname = document.getElementById("Lname");
  var Email = document.getElementById("Email");
  var Phone = document.getElementById("Phone");
  var Age = document.getElementById("Age");
  var Gender = document.getElementById("Gender");
  var Prakruti = document.getElementById("Prakruti");
  var Img = document.getElementById("Img");
  var gender = document.getElementById("gender").innerHTML;

  Fname.value = document.getElementById("fname").innerHTML;
  Mname.value = document.getElementById("mname").innerHTML;
  Lname.value = document.getElementById("lname").innerHTML;
  Email.value = document.getElementById("email").innerHTML;
  Phone.value = document.getElementById("phone").innerHTML;
  Img.src = document.getElementById("dp").src
  Age.value = parseInt(document.getElementById("age").innerHTML);
  Prakruti.innerHTML = document.getElementById("prakruti").innerHTML;
  if (gender == "male") {
    Gender.value = "1";
  } else if (gender == "female") {
    Gender.value = "2";
  } else if (gender == "other") {
    Gender.value = "3";
  } else {
    Gender.value = "0";
  }
}