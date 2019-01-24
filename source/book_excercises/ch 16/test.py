# code that tests the database and business layers

import db
from business import Product, LineItem, Cart

products = db.get_products()
product = products[1]
lineItem = LineItem(product, 2)
cart = Cart()
cart.addItem(lineItem)
print("Product:\t", product.name)
print("Price:\t", product.getDiscountPrice())
print("Price:\t", product.getDiscountPrice())
print("Quantity:\t", lineItem.quantity)
print("Total:\t", cart.getTotal())