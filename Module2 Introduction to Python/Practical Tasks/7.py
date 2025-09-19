# 7. Program to find Greatest Common Divisor of two numbers. For example, the GCD of 20 and 28 is 4 and
# the GCD of 98 and 56 is 14.

num1 = int(input("Enter the first value = "))
num2 = int(input("Enter the Second value = "))
gcd = 0
if num1<num2:
    num3 = num1
else:
    num3 = num2
for i in range(1,num3//2):
    if (num1%i==0 and num2%i==0):
        gcd=i

print(f"The GCD of {num1} and {num2} = {gcd}")