# 1. Sum of two numbers
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} + {b} = {a+b}")
"""

# 2. Odd or Even checker
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")
    
"""

# 3. Factorial Calculation

"""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"{num}! = {factorial(num)}")

"""


# 4. Fibonacci Sequence
"""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n ==1 :
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    

terms = int(input("Upto which term: "))
for i in range(terms):
    print(fibonacci(i) , end=" ")

"""

