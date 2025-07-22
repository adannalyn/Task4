from budget import Budget
import budget_utils

budget = Budget()

while True:
    print("\n---- KodeCamp's Budget Tracker ----")
    print("1. Add Transaction")
    print("2. List Transaction")
    print("3. Show totals by Category")
    print("4. Exit")
    choice = input("Enter your choice (1 - 4) ").strip()

    if choice == '1':
        cat = input("Enter Category: ").strip().title()
        amt = input("Enter Amount: ").strip()
        budget.add_transaction(cat, amt)
        print("Transaction added.")

    elif choice == '2':
        budget.list_transactions()

    elif choice == '3':
        grouped = budget_utils.group_by_category(budget.transactions)
        totals = budget_utils.calculate_totals(budget.transactions)
        print("\nTotals by Category:")
        for cat, total in totals.items():
            print(f"{cat}: ${total:.2f}")

    elif choice == '4':
        print("Records saved! Goodbye.")
        break
    else:
        print("Please enter a valid number between 1 and 4.")
