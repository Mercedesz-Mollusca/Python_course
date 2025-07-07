print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age > 12:
        bill = 5
        print("Child tickets are 5 dollars.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7 dollars")
    else:
        bill =12
        print("Adult tickets are 12 dollars")
    wants_photo = input("Do you want to have a photo take? Type y for Yes or n for No.")
    if wants_photo == "y":
        #Add 3 dollar to their bill.
        bill += +3
    print(f"Your final bill is: {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
