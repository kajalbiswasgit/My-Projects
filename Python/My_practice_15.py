# Create a dictionary with 3 products. Each product should itself be a dictionary with keys:
"""
id, name, price, stock, category.
Add a new product to the dictionary
Update stock when a product is purchased 
Apply a discount to one product (e.g., 15%).
Delete a product from the cart
Check if a product exists in the cart (CRUD → Read/Check)"""

cart= {
    "P1": {"id":101,"name":"mouse","price":120,"stock":2,"category":"Electronics"},
    "P2": {"id":102,"name":"keyboard","price":125,"stock":3,"category":"gaming"},
    "P3": {"id":103,"name":"laptop","price":115000,"stock":1,"category":"laptop"}
    }
updated_cart= cart ["P4"]= {"id":104,"name":"p6","price":11500,"stock":1,"category":"mobile"}
print (updated_cart)
updated_stock= cart ["P2"]["stock"] - 2
print ("P2 updated stock:",updated_stock)
discount= cart["P3"]["discount"]= 15
discounted_price= cart["P3"]["price"] - (cart["P3"]["price"]* cart ["P3"]["discount"]/ 100 )
print ("Discounted price is:",discounted_price)
del cart["P1"]
print ("P3 in cart:", "P3" in cart)