""" Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops. """

age_value = input("Provide Your Age :\n")

age = int(age_value)

weeks_in_years = 52

max_year= 90

remaining_weeks = (max_year - age) * weeks_in_years

print(f"You have {remaining_weeks} weeks left!")