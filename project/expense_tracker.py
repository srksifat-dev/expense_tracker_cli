from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []

    def display_categories(self):
        if not self.categories:
            print("\nNo categories available. You can add a new category.")
        else:
            print("\n--- Categories ---")
            for category in self.categories:
                print(f"{category['id']}. {category['name']}")
            print()

    def add_category(self, new_category_name):
        new_id = len(self.categories) + 1
        new_category = {'id': new_id, 'name': new_category_name}
        self.categories.append(new_category)
        print(f"Category '{new_category_name}' added with ID {new_id}.")
        return new_category

    def get_category_by_id(self, category_id):
        for category in self.categories:
            if category['id'] == category_id:
                return category
        return None

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Expense {expense.description} added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
        else:
            print("\n--- Expenses ---")
            for idx,expense in enumerate(self.expenses,1):
                print(f"{idx}. {expense}")

    def calculate_total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        print(f"\nTotal Expenses: {total:.2f}\n")

    def view_expenses_by_category(self,category):
        filtered_expenses = [expense for expense in self.expenses if expense.category['name'] == category]
        if not filtered_expenses:
            print(f"No expenses found in category '{category}'.")
        else:
            print(f"\n--- Expenses in {category} ---")
            for idx, expense in enumerate(filtered_expenses, 1):
                print(f"{idx}. {expense}")
    
    def removeExpense(self,index):
        if 0 <= (index - 1) < len(self.expenses):
            removed = self.expenses.pop(index - 1)
            print(f"Expense {removed.description} removed successfully!")
        else:
            print("Invalid expense number")

    def total_monthly_spending(self,year,month):
        monthly_expenses = [expense.amount for expense in self.expenses if expense.date.year == year and expense.date.month == month]
        total = sum(monthly_expenses)
        print(f"Total monthly spending for {year}-{month}: {total:.2f}")

    def generate_report(self,start_date,end_date):
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date,'%Y-%m-%d')
        report_expenses = [expense for expense in self.expenses if start <= expense.date <= end]

        if not report_expenses:
            print(f"No expenses found between {start_date} and {end_date}.")
        else:

            print("\n--- Expense Report from {start_date} to {end_date} ---")
            for idx, expense in enumerate(report_expenses, 1):
                print(f"{idx}. {expense}")
            total = sum(expense.amount for expense in report_expenses)
            print(f"\nTotal Spending: {total:.2f}\n")

