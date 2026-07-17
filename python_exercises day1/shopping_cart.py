def cart_total(cart):
    total = 0.0                      # Start with total = 0
    
    for item in cart:                # Loop through each item in the cart
        price = cart[item]["price"]
        quantity = cart[item]["quantity"]
        
        if quantity > 0:             # Skip if quantity is 0
            total += price * quantity   
    
    return total

cart = {
    "apple": {"price": 0.5, "quantity": 4},
    "bread": {"price": 2.5, "quantity": 2},
    "milk": {"price": 1.2, "quantity": 3},
    "banana": {"price": 0.3, "quantity": 0}   # This will be skipped
}

print(cart_total(cart))