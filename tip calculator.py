bill = float(input("What is the bill?\n$"))

people = float(input("How many people were there?\n"))

tip = float(input("How much tip you'd like to give?\n%"))

total_bill = bill + (bill * tip/100)

print(f"Total bill with the tip is ${round(total_bill,2)}")

each_person = total_bill / people

print(f"Each person has to pay ${round(each_person,2)}")