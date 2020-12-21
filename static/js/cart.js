let addToCartButtons = document.getElementsByClassName('update-cart');

for (let button of addToCartButtons) {
    button.addEventListener('click', () => {
        let productId = button.dataset.product
        let action = button.dataset.action

        console.log('productId:' + productId, 'action:' + action)
        if (user === "AnonymousUser") {
            console.log('Not Logged')
        } else {
            updateOrderUser(productId, action)
        }
    })

}

function updateOrderUser(productId, action) {
    console.log(user, 'sending data...')

    let url = '/order/update/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data:'+data)
            location.reload()
        })
}
