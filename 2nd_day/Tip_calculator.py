print("Welcome to Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bills?"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_bill_per_person = round(bill_per_person, 2)
print(f"Each person should pay $ {final_bill_per_person} ")

