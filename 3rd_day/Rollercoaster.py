print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))

if height <= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age > 12:
        print("You will pay 5 dollars.")
    elif age <= 18:
        print("You will pay 5 dollars")
    else:
        print("You will pay 18 dollars")
else:
    print("Sorry you have to grow taller before you can ride.")
