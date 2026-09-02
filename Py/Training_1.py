

name = "Bob"
age = 10
weight = 20.5
is_female = False

print(name)
print(type(name))
print(age)
print(type(age))
print(weight)
print(type(weight))
print(is_female)
print(type(is_female))
print(name)

x = 20
y = 10

print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x // y) # Floor Division
print(x % y) # Modulus
print(x ** y) # Exponentiation

celsius = 25
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)

is_student = True
is_employed = False
has_license = True
age = 15
is_adult = age >=18
is_teenager = age >= 13 and age < 20
can_vote = is_adult and True
is_weekend = False
temperature = 32
is_hot = temperature > 30
is_eligible = is_adult and has_license and not is_employed

print(is_adult)
print(type(is_adult))
print(is_teenager)
print(can_vote)
print(is_eligible)