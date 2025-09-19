#  18. Python Program to Find Factorial of Number Using Recursion
def factorial(num): 
    if num == 0 or num == 1:   
        return 1
    else: 
        return num * factorial(num - 1)  


num = int(input("Enter any value = "))
print(f"{factorial(num)} is factorial of {num}")