height = input("Please provide your height in centimeters\n")
weight = input("Please provide your weight in kg\n")

h = float(height)

w = float(weight)

BMI = (w/(h**2))

BMI_int = int(BMI)

print(BMI_int)