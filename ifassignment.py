height =float(input("enter height in meters"))
weight =float(input("enter weight in kilograms"))
bmi = weight/(height**2)

if bmi < 18.5:
    category ="underweight"
elif 18.5 <=bmi <25:
    category ="normalweight"
elif 25 <= bmi <29.9:
    category ="overweight"
else: category ="obesity"

