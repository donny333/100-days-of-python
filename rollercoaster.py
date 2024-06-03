print("Welcome to Roller Coaster!")
height = int(input("What is your height in centimeters? "))

if height < 120:
    print("Sorry, you have to grow taller to ride a rollercoaster.")
else:
    print("You can ride a rollercoaster.")
    age = int(input("What is your age? "))
    price = 0
    if age >= 18:
        if age > 44 and age < 56:
            print("The ticket is free for you!")
        else:
            print("Price for the ticket is 12$")
            price += 12
    elif age < 12:
        print("Price for the ticket is 5$")
        price += 5
    else:
        print("Price for the ticket is 7$")
        price += 7

    photo_included = input("Do you need a photo? Y or N. ")
    if photo_included.lower() == "y":
        price += 3

    print(f"Total price is {price}$")