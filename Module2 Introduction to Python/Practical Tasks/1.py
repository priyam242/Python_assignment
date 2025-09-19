# --> 1. Write a python program to sum of the first n positive integers. 
count = int(input("Enter the number of values = "))
sum=0
for i in range(count):
    i = int(input(f"Enter the {i+1} value = "))
    sum = sum+i

print(f"The sum of {count} values = {sum}")