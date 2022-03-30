//cart working
if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", ready);
} else {
    ready();
}

function ready() {
    const removeCartButton = document.getElementsByClassName("btn-remove");
    console.log(removeCartButton);
    for (var i = 0; i < removeCartButton.length; i++) {
        const btn = removeCartButton[i];
        btn.addEventListener("click", removeCartItem);
    }
    const quantityInput = document.getElementsByClassName("item-quantity");
    for (var i = 0; i < quantityInput.length; i++) {
        const input = quantityInput[i];
        input.addEventListener("change", changedQunatity);
    }

    const addToCart = document.getElementsByClassName("btn-add-to-cart");
    addToCart.addEventListener("click", addToCartChange(event));
}

// const buy = document.getElementsByClassName('buy-now')[0].addEventListener('click', buyClicked)

function buyClicked() {
    alert("You placed your order");
    const cartContent = document.getElementsByClassName("cart-content");
    while (cartContent.hasChildNodes()) {
        cartContent.removeChild(cartContent.firstChild);
    }
    updateTotal();
}

//Add to Cart function
function addToCartChange(event) {
    let btn = event.target;
    let btnParent = btn.parentElement;
    // let grandElement = btn.parentElement.parentElement;
    let itemName = btnParent.children[1].innerText;
    let itemPrice = btnParent.children[2].innerText;
    let itemImage = btnParent.children[0].src;
    let info = "added to cart!!";
    alert(itemName + " " + info);
    console.log(itemName, itemPrice, itemImage);

    addProductToCart(itemName, itemPrice, itemImage);
    updateTotal();
    return;
}

function addProductToCart(itemName, itemPrice, itemImage) {
    const shopBox = document.createElement("div");
    const cartItems = document.getElementsByClassName("cart-content")[0];
    shopBox.classList.add("cartBox");
    const cartItemNames = document.getElementsByClassName("food-name");
    for (var i = 0; i < cartItemNames.length; i++) {
        alert("You added this item to the cart!!");
        return;
    }

    const cartContentBox = `
 <img  style="${itemImage}" alt="cart-items" >
   <div style="margin-left:100px">
      <p class="food-name">${itemName}</p>
      <p class="item-price">USH ${itemPrice}</p>
      <input  type='number' value='1' class='item-quantity'/>
   </div>


    <button  style="margin-left:100px" class="btn-remove" type="button">Remove</button>
`;
    shopBox.innerHTML = cartContentBox;
    console.log(shopBox);
    shopBox
        .getElementsByClassName("btn-remove")[0]
        .addEventListener("click", removeCartItem);
    shopBox
        .getElementsByClassName("item-quantity")[0]
        .addEventListener("change", changedQunatity);
}

//change qunatity
function changedQunatity(event) {
    const input = event.target;
    if (isNaN(input.value) || input.value < 0) {
        input.value = 1;
    }
    updateTotal();
}

//remove cart item
function removeCartItem(event) {
    const buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();
    updateTotal();
}

function updateTotal() {
    const cartContent = document.getElementsByClassName("cart-content")[0];
    const cartBoxes = document.getElementsByClassName("cartBox");
    let total = 0;
    for (var i = 0; i < cartBoxes.length; i++) {
        const cartbox = cartBoxes[i];
        const itemPrice = cartbox.getElementsByClassName("item-price")[0];
        const itemQuantity = cartbox.getElementsByClassName("item-quantity")[0];
        const quantity = itemQuantity.value;
        const price = parseFloat(itemPrice.innerText.replace("USH", ""));
        total = total + price * quantity;
        document.getElementsByClassName("total-price")[0].innerText = "USH" + total;
    }
}