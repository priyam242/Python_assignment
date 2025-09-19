# 13.Write a Python program to sort a dictionary (ascending /descending) by value.
count = int(input("Enter how many values you have enter = "))
lst = []
for i in range(count):
    key = input("enter the key = ")
    val = input("Enter the value = ")
    lst.append((key, val))

# Sort by value (ascending)
lst.sort(key=lambda x: x[1])
dis = dict(lst)
print("Ascending by value:", dis)

# Sort by value (descending)  
lst.sort(key=lambda x: x[1], reverse=True)
dis2 = dict(lst)
print("Descending by value:", dis2)