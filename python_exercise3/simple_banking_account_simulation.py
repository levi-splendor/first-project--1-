def process_transactions(starting_balance, transactions):
    balance = starting_balance
    failed_transactions = []
    
    for transaction in transactions:
        t_type = transaction["type"]
        amount = transaction["amount"]
        
        if t_type == "deposit":
            balance += amount
            
        elif t_type == "withdrawal":
            if balance >= amount:
                balance -= amount
            else:
                # Insufficient funds → record as failed
                failed_transactions.append(transaction)
        # Ignore unknown transaction types
    
    return {
        "final_balance": balance,
        "failed_transactions": failed_transactions
    }


# Example for testing
if __name__ == "__main__":
    transactions = [
        {"type": "deposit", "amount": 1000},
        {"type": "withdrawal", "amount": 300},
        {"type": "withdrawal", "amount": 800},
        {"type": "deposit", "amount": 200},
        {"type": "withdrawal", "amount": 500}
    ]
    
    result = process_transactions(500, transactions)
    result=process_transactions(1000, transactions)
    print(result)