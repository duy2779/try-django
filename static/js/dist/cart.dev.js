"use strict";

var addToCartButtons = document.getElementsByClassName('update-cart');
var _iteratorNormalCompletion = true;
var _didIteratorError = false;
var _iteratorError = undefined;

try {
  var _loop = function _loop() {
    var button = _step.value;
    button.addEventListener('click', function () {
      var productId = button.dataset.product;
      var action = button.dataset.action;
      console.log('productId:' + productId, 'action:' + action);

      if (user === "AnonymousUser") {
        console.log('Not Logged');
      } else {
        console.log(user, 'sending data...');
      }
    });
  };

  for (var _iterator = addToCartButtons[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
    _loop();
  }
} catch (err) {
  _didIteratorError = true;
  _iteratorError = err;
} finally {
  try {
    if (!_iteratorNormalCompletion && _iterator["return"] != null) {
      _iterator["return"]();
    }
  } finally {
    if (_didIteratorError) {
      throw _iteratorError;
    }
  }
}