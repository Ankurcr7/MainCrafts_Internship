# 1. Sum of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} + {b} = {a+b}")


# 2. Odd or Even checker

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")
    


# 3. Factorial Calculation


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"{num}! = {factorial(num)}")




# 4. Fibonacci Sequence

def fibonacci(n):
    if n <= 0:
        return 0
    elif n ==1 :
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    

terms = int(input("Upto which term: "))
for i in range(terms):
    print(fibonacci(i) , end=" ")



# 5. String Reverse 

print(f"Reversed string: {input("Enter a string: ")[::-1]}")



# 6. Palindrome check

word= input("Enter a word: ")
reverse_word = word[::-1]

if word == reverse_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not palindrome")



# 7. Leap year check


year = int(input("Enter a year: "))

if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year} is a leap year") 
        
else:
    print(f"{year} is not a leap year")



# 8. Armstrong number


def armstrong(n, order) -> bool:
    sum = 0
    for i in str(n):
        sum += int(i) ** order
    return sum == n

num = int(input("Enter a number: "))
order = len(str(num))

if armstrong(num, order):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

