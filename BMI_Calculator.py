Weight=float(input("enter your weight in Kg:"))

height=float(input("enter your height in meters:"))

bmi=Weight/(height**2)

print("your BMI is:",bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 24.9:
    print("Normal Weight")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")        

