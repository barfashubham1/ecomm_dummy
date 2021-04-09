var updateButtons = document.getElementsByClassName('update-cart');
var updateWishList = document.getElementsByClassName('update-wishlist');
// var sum=0

for (var i = 0; i < updateButtons.length; i++) {

    updateButtons[i].addEventListener("click", function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:' + productId + ' action:' + action + ' by ' + user);

        if (user === "AnonymousUser") {
            console.log("user not logged");

        } else {
            updateUserCart(productId, action);
        }

    });

}
for (var i = 0; i < updateWishList.length; i++) {

    updateWishList[i].addEventListener("click", function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:' + productId + ' action:' + action + ' by ' + user);

        if (user === "AnonymousUser") {
            console.log("user not logged");

        } else {
            updateWishlist(productId, action);
        }

    });

}

function updateUserCart(productId, action) {
    // console.log('User is logged in, sending data...')

    var url = 'update_item/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            if (action = "add_cart") {
                alert("item added to the cart")
            }
            location.reload()

        });
}

function updateWishlist(productId, action) {
    // console.log('User is logged in, sending data...')

    var url = 'update_wishlist/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'productId': productId,
                'action': action
            })
        })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            if (action = "update_wishlist") {
                alert("item added to the wishlist")
            }
            location.reload()

        });
}


// var a = document.getElementsByClassName('unit_total');

// for(var i=0;i<a.length;i++){
//     sum+=a[i].innerHTML;
// }
// document.getElementsByClassName('total').text=sum;