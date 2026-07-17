def items_to_stock(inventory, threshold):
    items_to_stock=[]
    for item, stock in inventory.items():
        if stock < threshold:
            items_to_stock.append(item)
    return items_to_stock
inventory={
     "apple": 10,
     "banana": 5,
     "orange": 2,
    "grape": 8,

}
print(items_to_stock(inventory, 6))