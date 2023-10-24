function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            //Does the cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');
let btns = document.querySelectorAll(".pricing-box-alt button")
let btnRemove = document.querySelectorAll(".shoppingCartTable button")

btns.forEach(btn => {
    btn.addEventListener("click", addToCart)
});

btnRemove.forEach(btn => {
    btn.addEventListener("click", removeFromCart)
});

function addToCart(e) {
    let productId = e.target.value
    let url = "/add_to_cart/"
    let data = { id: productId }

    fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("num_of_items").innerHTML = data
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })
    alert('If you are logged in, the item is added to cart!')
}

function removeFromCart(e) {
    let productId = e.target.value
    let url = "/remove_from_cart/"
    let data = { id: productId }

    fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })
    alert('Item removedd from cart! Refresh cart to view update')
}

function cartPaymentConfirmation(e) {
    let cartId = e.target.value
    let url = "/confirm_payment/" + cartId

    let data = { id: cartId }

    fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })
    alert('Payment Confirmed!')
}



// Automatic Slideshow - change image every 4 seconds
var myIndex = 0;

function toggleMenu() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

//* Loop through all dashboard side navigation dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dashboard-dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}
