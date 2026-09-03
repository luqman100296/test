
# name = input("enter your name: ")

# height = float(input("Enter your height in meters: "))

# #Input Validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("Please enter a positive number.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# #Output Validation
# print(f"Hello, {name}!")
# print(f"Your height is {height} meters.")
# print(f"Your age is {age}.")

# Figure1 = int(input("Enter a number for Figure 1: "))
# Figure2 = int(input("Enter a number for Figure 2: "))
# Operation = input("Enter an operation (+, -, *, /): ")

# if Operation == "+":
#     result = Figure1 + Figure2
# elif Operation == "-":
#     result = Figure1 - Figure2
# elif Operation == "*":
#     result = Figure1 * Figure2
# elif Operation == "/":
#     if Figure2 != 0:
#         result = Figure1 / Figure2
#     else:
#         result = "Error: division by zero"
# else:
#     result = "Invalid operation"

# print("Result:", result)

score = 0
options = ["A", "B", "C", "D"]

# Question 1
print("1) What is the capital of France?")
print("A) Jakarta  B) Las Vegas  C) Paris  D) London")
answer = ""
while answer not in options:
    answer = input("Choose an answer (A, B, C, D): ").upper()
    if answer not in options:
        print("Invalid choice, try again.")
if answer == "C":
    score += 1

# Question 2
print("2) What is 5 + 3?")
print("A) 6  B) 8  C) 20  D) 11")
answer = ""
while answer not in options:
    answer = input("Choose an answer (A, B, C, D): ").upper()
    if answer not in options:
        print("Invalid choice, try again.")
if answer == "B":
    score += 1

# Question 3
print("3) What is Luqman's favourite food?")
print("A) Nasi Goreng  B) Pizza  C) Sushi  D) Steak")
answer = ""
while answer not in options:
    answer = input("Choose an answer (A, B, C, D): ").upper()
    if answer not in options:
        print("Invalid choice, try again.")
if answer == "D":
    score += 1

print("Total correct:", score)