function payWithPaystack() {
    var amountPayable = 12000; //parseInt(document.getElementById("total").value);
    //amountPayable *= 100;

    var handler = PaystackPop.setup({ 
        key: 'pk_live_0c6a1af1c9d2a714927a32c65b20f515b2a48311', //put your public key here
        email: 'info@galleria.com.ng', //put your customer's email here
        amount: amountPayable, //370000, //amount the customer is supposed to pay
        metadata: {
            custom_fields: [
                {
                    display_name: "Mobile Number",
                    variable_name: "mobile_number",
                    value: "+234807067317495" //customer's mobile number
                }
            ]
        },
        callback: function (response) {
            //after the transaction have been completed
            //make post call  to the server with to verify payment 
            //using transaction reference as post data
            $.post("verify.php", {reference:response.reference}, function(status){
                if(status == "success")
                    //successful transaction
                    alert('Transaction was successful');
                else
                    //transaction failed
                    alert(response);
            });
        },
        onClose: function () {
            //when the user close the payment modal
            alert('Transaction cancelled');
        }
    });
    handler.openIframe(); //open the paystack's payment modal
}

function justShout(){
    alert("Just Shouting");
}