print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percent tip would you like to give? 10, 12 or 15? "))
person=int(input("How many people to split the bill? "))
new_tip=tip/100
new_bill=bill*new_tip
total=bill+new_bill
print(f"Each person should pay ${total}")