#investment input validation and question
investment = input("Enter the investment amount (must be greater than 0 and less than 50000): ")
if investment.isdigit():
    investment = int(investment)
    while True:
        if investment <= 0 or investment >= 50000:
            print("The investment amount must be greater than 0 and less than $50,000.")
            investment = input("Please enter a valid investment amount: ")
            if investment.isdigit():
                investment = int(investment)
        else:
            break
#interrest rate input validation and question
interestrate = input("Enter the interest rate (must be greater than 0 and less than 15): ")
if interestrate.isdigit():
    interestrate = int(interestrate)
    while True:
        if interestrate <= 0 or interestrate >= 15:
            print("The interest rate must be greater than 0 and less than 15%.")
            interestrate = input("Please enter a valid interest rate: ")
            if interestrate.isdigit():
                interestrate = int(interestrate)
        else:
            break
investmentyears = input("Enter the number of years (must be greater than 0): ")
if investmentyears.isdigit():
    investmentyears = int(investmentyears)
    while True:
        if investmentyears <= 0:
            print("The number of years must be greater than 0.")
            investmentyears = input("Please enter a valid number of years: ")
            if investmentyears.isdigit():
                investmentyears = int(investmentyears)
        else:
            break
else:
    # Handles negative numbers or non-digit input
    while True:
        try:
            investmentyears = int(input("Enter the number of years (must be greater than 0): "))
            if investmentyears > 0:
                break
            else:
                print("The number of years must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
months = investmentyears * 12
monthlyinterest = interestrate / 12 / 100
total = 0.0
for monnths in range(1,months + 1):
    total += investment
    interest = round(total * monthlyinterest, 2)
    total += interest
    if monnths % 12 == 0:
        print(f"Total after {monnths // 12} year(s): ${round(total, 2)}")

print("Summary:")
print("years calcualted : " + str(investmentyears))
print("interest rate : " + str(interestrate) + "%")
print("investment amount : $" + str(investment))
print("Total amount after compouding interest: $" + str(round(total, 2)))
print("completed by, John benites")