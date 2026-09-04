
# # # name = input("enter your name: ")

# # # height = float(input("Enter your height in meters: "))

# # # #Input Validation
# # # while True:
# # #     try:
# # #         age = int(input("Enter your age: "))
# # #         if age > 0:
# # #             break
# # #         else:
# # #             print("Please enter a positive number.")
# # #     except ValueError:
# # #         print("Invalid input. Please enter a valid number.")

# # # #Output Validation
# # # print(f"Hello, {name}!")
# # # print(f"Your height is {height} meters.")
# # # print(f"Your age is {age}.")

# # # Figure1 = int(input("Enter a number for Figure 1: "))
# # # Figure2 = int(input("Enter a number for Figure 2: "))
# # # Operation = input("Enter an operation (+, -, *, /): ")

# # # if Operation == "+":
# # #     result = Figure1 + Figure2
# # # elif Operation == "-":
# # #     result = Figure1 - Figure2
# # # elif Operation == "*":
# # #     result = Figure1 * Figure2
# # # elif Operation == "/":
# # #     if Figure2 != 0:
# # #         result = Figure1 / Figure2
# # #     else:
# # #         result = "Error: division by zero"
# # # else:
# # #     result = "Invalid operation"

# # # print("Result:", result)

# # # score = 0
# # # options = ["A", "B", "C", "D"]

# # # # Question 1
# # # print("1) What is the capital of France?")
# # # print("A) Jakarta  B) Las Vegas  C) Paris  D) London")
# # # answer = ""
# # # while answer not in options:
# # #     answer = input("Choose an answer (A, B, C, D): ").upper()
# # #     if answer not in options:
# # #         print("Invalid choice, try again.")
# # # if answer == "C":
# # #     score += 1

# # # # Question 2
# # # print("2) What is 5 + 3?")
# # # print("A) 6  B) 8  C) 20  D) 11")
# # # answer = ""
# # # while answer not in options:
# # #     answer = input("Choose an answer (A, B, C, D): ").upper()
# # #     if answer not in options:
# # #         print("Invalid choice, try again.")
# # # if answer == "B":
# # #     score += 1

# # # # Question 3
# # # print("3) What is Luqman's favourite food?")
# # # print("A) Nasi Goreng  B) Pizza  C) Sushi  D) Steak")
# # # answer = ""
# # # while answer not in options:
# # #     answer = input("Choose an answer (A, B, C, D): ").upper()
# # #     if answer not in options:
# # #         print("Invalid choice, try again.")
# # # if answer == "D":
# # #     score += 1

# # # print("Total correct:", score)

# # age = 18 

# # if age >= 18:
# #     print("You are an adult.")
# # else:
# #     print("You are a minor.")

# # score = 20

# # if score >= 90:
# #     grade = "A"
# # elif score >= 80:
# #     grade = "B"
# # elif score >= 70:
# #     grade = "C"
# # else:
# #     grade = "Failure to Humanity"

# # print(f"Your grade is: {grade}")

# # user_age = int(input("Enter your age: "))
# # has_license = input("Do you have license (True or False): ")

# # if user_age >= 18 and has_license == "True":
# #     print("You are allowed to drive")
# # else:
# #     print("You are not allowed to drive")

# weight = float(input("Enter Your Weight (KG): "))
# height = float(input("Enter Your Height (Meter): "))

# BMI = (weight/height**2)

# if BMI <= 18.5:
#     print("Congratulations, you're a model.")
# elif BMI <= 24.9:
#     print("You are a basic.")
# elif BMI <= 29.9:
#     print("Beware bro, dangerous dy.")
# else:
#     print("Go cucuk Ozempic.")


password = "1234"
attempts = 0

while attempts < 3:
    guess = input("Enter password: ")
    if guess == password:
        print("Access granted")
        break
    attempts += 1
    print("Wrong password")

if attempts == 3:
    print("Account locked")