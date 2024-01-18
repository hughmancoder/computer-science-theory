def simplify_debts(transactions):
    # Initialize a dictionary to store the net amount each person owes or is owed
    net_amounts = {}
    # Process each transaction
    for transaction in transactions.split('\n'):
        debtor, _, creditor, amount, _ = transaction.split()
        amount = int(amount)
        # Update the net amounts
        net_amounts[debtor] = net_amounts.get(debtor, 0) - amount
        net_amounts[creditor] = net_amounts.get(creditor, 0) + amount

    
    # Initialize a list to store the simplified transactions
    simplified_transactions = []
    
    # Process each person in the order they appear in the transactions
    for person in transactions.split():
        if person in net_amounts and net_amounts[person] > 0:
            # This person is owed money
            for debtor in net_amounts:
                if net_amounts[debtor] < 0:
                    # This person owes money
                    amount = min(net_amounts[person], -net_amounts[debtor])
                    if amount > 0:
                        # Add a transaction from the debtor to the creditor
                        simplified_transactions.append(f"{debtor} owes {person} {amount} dollars.")
                        # Update the net amounts
                        net_amounts[person] -= amount
                        net_amounts[debtor] += amount
    return '\n'.join(simplified_transactions)