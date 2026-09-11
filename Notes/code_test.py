# Write a function double(n) that returns n * 2. Then write quadruple(n) that calls double twice inside it and returns the result. Call quadruple(5) and print it.

def double(n):
    return n * 2

def quadruple(n):
    return double(n) * 2

result = quadruple(5)
print(result)

# Write a function is_even(n) that returns True if n % 2 == 0, else False. Then write describe_number(n) that calls is_even(n) and prints "<n> is even" or "<n> is odd" based on the result. Call describe_number(7).

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def describe_number(n):
    if is_even(n) == True:
        print(f"{n} is even")
    else: 
        print(f"{n} is odd")

describe_number(7)