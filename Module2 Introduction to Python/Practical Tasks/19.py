# 19.Write a Python function that takes a list and returns a new list with unique elements of the first list. 
def check(lst):
    lst2 = []
    lst2 = set(lst)
    print("Original list = ",lst)
    print("New list With Unique values = ",lst2)


lst = []
num = int(input("Enter how many value you have enter = "))
for i in range(num):
    i = int(input(f"Enter any {i+1} value = "))
    lst.append(i)

check(lst)
