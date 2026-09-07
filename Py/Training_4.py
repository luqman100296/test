x = 3
print(x == 3)
print(x != 3)

weight = int(input("Please enter your weight: "))
height = float(input("Please enter your height (in meter): "))

if weight >= 30:
    print("Weight Accepted")
else:
    print("Please Enter Valid Weight")

if height >= 1.0:
    print("Height Accepted")
else:
    print("Please Enter Valid Height")

BMI = weight/height**2

print(BMI)

if BMI <= 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal Weight")
elif BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")