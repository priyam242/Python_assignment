# 10.Write a Python program to get unique values from a list.
count = int(input("Enter the number of values which you have to enter = "))
lst_num = []
for i in range(count):
    i = int(input(f"Enter the {i+1} values = "))
    lst_num.append(i)

print("Original String = ",end=" ")
print(lst_num)
lst2 = set(lst_num)
print("list with Uniques values = ",end=" ")
print(lst2)