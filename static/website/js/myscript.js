$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]; 
    console.log("pid =", id);

    $.ajax({
        type: "GET",
        url: "/pluscart",
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log("data =", data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            
        }
    });
});

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]; 
    console.log("pid =", id);

    $.ajax({
        type: "GET",
        url: "/minuscart", // Ensure this is the correct endpoint
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log("data =", data);
            
            // Update the quantity only if it's greater than 1
            if (data.quantity > 0) {
                eml.innerText = data.quantity;
            }
            
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        },
        error: function(error) {
            console.error('Error updating quantity:', error);
        }
    });
});


$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this 

    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            prod_id: id
        },
        success: function(data) {
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    });
});


$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();

    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            window.location.href = 'http://localhost:8000/productdetail/${id}'
            
        }
    });
});

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();

    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            window.location.href = 'http://localhost:8000/productdetail/${id}'
            
        }
    });
});


