# 15.Given a number n, write a python program to make and print the list of Fibonacci series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output : First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13
num = int(input("Enter the range = "))
num1=0
num2=1
print("Fibonnaci series = ",end=" ")
for i in range(num+1):
    if i==0:
        print("0",end=" ")
    elif i==1:
        print("1",end=" ")
    else:
        num3 = num1+num2
        print(num3,end=" ")
        num1=num2
        num2=num3