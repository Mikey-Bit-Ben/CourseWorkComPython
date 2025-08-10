import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def main():
    print("welcome to budget tracker")
    print("------------------------------")
    income = get_income()
    expenses = get_expenses()

    total_expenses = sum(expenses)
    remaining_budget = income - total_expenses
    print("------------------------------")
    print("budget summary")
    print(f"Total Income : ${income:,.2f}")
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Remaining Budget: ${remaining_budget:,.2f}")

    print("expense list:")
    for idx, expenses in enumerate(expenses, start=1):
        print(f"Expense {idx}: ${expenses:,.2f}")
    print("completed by John Benites")
def get_income():
    while True:
        try:
            income = input("Enter your monthly income: ")
            income = float(income)
            if income < 0:
                raise ValueError("Income cannot be negative.")
            return income
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")
def get_expenses():
    expences = []
    while True:
        try:
            expence = input("Enter an expense (or type 0 or 'done' to finish): ")
            if expence.lower() == 'done' or expence == '0':
                break
            expence = float(expence)
            if expence < 0:
                raise ValueError("Expense cannot be negative.")
            expences.append(expence)
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")
    return expences


if __name__ == "__main__":
    main()