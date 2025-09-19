# 12.Write a Python program to convert a list of tuples into a dictionary
count = int(input("Enter how many values you have enter = "))
tpl = []
for i in range(count):
    key = input("enter the key = ")
    val = input("Enter the value = ")
    tpl.append((key,val))

dis = dict(tpl)
print("Dictionary = ",dis)