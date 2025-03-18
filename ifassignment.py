height = 1.50  # height in meters
weight = 57  # weight in kilograms
bmi = weight / (height ** 2)
category = ""

if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 25:
    category = "normal weight"
elif 25 <= bmi < 29.9:
    category = "overweight"
else:
    category = "obesity"

print(f"BMI: {bmi:.2f}, Category: {category}")

