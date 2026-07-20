def order_summary(orders):
    summary = {} 
    # Loop through each customer
    for customer, order_list in orders.items():
        total_spent = 0.0  
        # Nested loop: go through each item in the customer's orders
        for order in order_list:
            price = order["price"]
            quantity = order["quantity"]
            total_spent += price * quantity
        summary[customer] = total_spent
    return summary
def top_spender(orders):
    if not orders:
        return None  # No customers 
    summary = order_summary(orders) 
    # Find the customer with the highest total
    max_spent = -1
    top_customer = None
    
    for customer, amount in summary.items():
        if amount > max_spent:
            max_spent = amount
            top_customer = customer
    
    return top_customer
orders = {
    "Alice": [
        {"item": "pen", "price": 1.5, "quantity": 3}
    ],
    "Bob": [
        {"item": "book", "price": 12, "quantity": 1},
        {"item": "pen", "price": 1.5, "quantity": 2}
    ]
}

summary = order_summary(orders)
print("Order Summary:", summary)


print("Top Spender:", top_spender(orders))
