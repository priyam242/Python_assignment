# 14.Write a Python program to find the highest 3 values in a dictionary.
count = int(input("Enter how many values you have enter = "))
lst = []
for i in range(count):
    key = input("enter the key = ")
    val = int(input("Enter the value = "))
    lst.append((key, val))

# Sort by value (descending)  
lst.sort(key=lambda x: x[1], reverse=True)
top_3 = lst[:3]
dis = dict(lst)
print("Dictionary = ",dis)
for key,val in top_3:
        print(f"{key} : {val},",end=" ")
