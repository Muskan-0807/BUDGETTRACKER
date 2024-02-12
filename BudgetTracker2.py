import csv
from collections import defaultdict

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def calculate_remaining_budget(self):
        total_income = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'income')
        total_expenses = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'expense')
        remaining_budget = total_income - total_expenses
        return remaining_budget

    def categorize_expenses(self):
        categories = defaultdict(float)
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                categories[transaction['category']] += transaction['amount']
        return categories

    def save_transactions_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['date', 'type', 'category', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction)

def main():
    budget_tracker = BudgetTracker()
    while True:
        print("\n1. Add Transaction")
        print("2. Calculate Remaining Budget")
        print("3. Categorize Expenses")
        print("4. Save Transactions to CSV")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter transaction date: ")
            transaction_type = input("Enter transaction type (income/expense): ")
            category = input("Enter transaction category: ")
            amount = float(input("Enter transaction amount: "))
            transaction = {'date': date, 'type': transaction_type, 'category': category, 'amount': amount}
            budget_tracker.add_transaction(transaction)
            print("Transaction added successfully!")

        elif choice == '2':
            remaining_budget = budget_tracker.calculate_remaining_budget()
            print(f"Remaining budget: rupee{remaining_budget}")

        elif choice == '3':
            categories = budget_tracker.categorize_expenses()
            print("Expense categories:")
            for category, amount in categories.items():
                print(f"{category}: rupee{amount}")

        elif choice == '4':
            filename = input("Enter filename to save transactions (e.g., transactions.csv): ")
            budget_tracker.save_transactions_to_csv(filename)
            print("Transactions saved to CSV!")

        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()