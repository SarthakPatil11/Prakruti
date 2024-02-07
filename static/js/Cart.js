function ChangeQuantity(id) {
    inputQuantity = document.getElementById('input_Quantity' + id).value;
    document.getElementById("div_QuantityPrice" + id).innerHTML =
        inputQuantity * document.getElementById("pprice" + id).value;
    calc()
}

function chng(id, who) {
    var ch = document.getElementById(id);
    var divTotalPrice = document.getElementById("div_TotalPrice");
    var divQuantityPrice = document.getElementById("div_QuantityPrice" + id);
    var ProductNumber = document.getElementById("label_TotalProducts");
    if (who) {
        if (ch.checked) {
            divTotalPrice.innerHTML = parseInt(divTotalPrice.innerHTML) + parseInt(divQuantityPrice.innerHTML);
            ProductNumber.innerHTML = parseInt(ProductNumber.innerHTML) + 1;
        } else {
            divTotalPrice.innerHTML = parseInt(divTotalPrice.innerHTML) - parseInt(divQuantityPrice.innerHTML);
            ProductNumber.innerHTML = parseInt(ProductNumber.innerHTML) - 1;
        }
    }
    else {
        if (ch.checked) {
            divTotalPrice.innerHTML = parseInt(divTotalPrice.innerHTML) + parseInt(divQuantityPrice.innerHTML);
        }
    }
}

function adM() {
    document.getElementById("div_Cart").style.marginTop = "100px";
}