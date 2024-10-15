import expense_tracker as et
import expense as e

def main():
    tracker = et.ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Remove Expense")
        print("6. Total Monthly Spending")
        print("7. Generate Expense Report for a Time Period")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.display_categories()
            category_choice = input("Enter expense category ID or type 'new' to add a new category: ")
            if category_choice.lower() == "new":
                new_category_name = input("Enter new category name: ")
                category = tracker.add_category(new_category_name)
            else:
                category_id = int(category_choice)
                category = tracker.get_category_by_id(category_id)
                if not category:
                    print("Invalid category ID. Please try again.")
                    continue
            date = input("Enter expense date (YYYY-MM-DD): ")
            expense = e.Expense(amount, description, category, date)
            tracker.add_expense(expense)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            category = input("Enter category to filter expenses: ")
            tracker.view_expenses_by_category(category)

        elif choice == "4":
            tracker.calculate_total_expenses()

        elif choice == "5":
            index = int(input("Enter the number of the expense to remove: "))
            tracker.removeExpense(index)

        elif choice == "6":
            year = int(input("Enter the year(YYYY): "))
            month = int(input("Enter the month(MM): "))
            tracker.total_monthly_spending(year, month)
        elif choice == "7":
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            tracker.generate_report(start_date, end_date)
        elif choice == "8":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()