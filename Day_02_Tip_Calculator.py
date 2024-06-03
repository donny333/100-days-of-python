print("Welcome to Tip Calculator!")
bill = float(input("What is your total bill? "))
tip_rate = input("What is your tip rate? 10, 12, or 15? ")
people = int(input("How many people will split the bill? "))

total_bill = bill * float(f"1.{tip_rate}")
each_person_bill = total_bill / people

print(f"Each person should pay: ${each_person_bill:.2f}")