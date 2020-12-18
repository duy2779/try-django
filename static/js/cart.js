let addToCartButtons = document.getElementsByClassName('update-cart');

for (let button of addToCartButtons) {
    button.addEventListener('click', () => {
        let productId = button.dataset.product
        let action = button.dataset.action

        console.log('productId:' + productId, 'action:' + action)
        if (user === "AnonymousUser") {
            console.log('Not Logged')
        }else{
            console.log(user, 'sending data...')
        }
    })

}
