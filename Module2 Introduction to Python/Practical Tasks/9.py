# 9. Write a Python program to find the second smallest number in a list. 
lst_num = []
count = int(input("Enter how many values you have enter = "))
for i in range(count):
    i = int(input(f"Enter {i+1} value = "))
    lst_num.append(i)

print("Original List =", lst_num)

sorted_list = sorted(lst_num)
print("Sorted List =", sorted_list)


unique_sorted = sorted(set(lst_num))

if len(unique_sorted) < 2:
    print("There is no second smallest distinct number in the list.")
else:
    print("Second Smallest distinct value =", unique_sorted[1])