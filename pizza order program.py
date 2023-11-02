""" Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1 """

print("Welcome To Furkan's Pizza!")

bill=0

size = input("What kind of pizza do you want? S, M or L \n")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

add_pepperoni = input("Would you like to have pepperoni? Y or N\n")
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

extra_cheese = input ("Want some extra cheese? Y or N\n")
if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is: ${bill}.")