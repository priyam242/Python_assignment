# 8. Write a Python program to check whether a list contains a sublist. 
lst=[1,2,3,4,5,[5,4,6]]
flag=0
for i in lst:
    if isinstance(i,list):
        print("It contains list ")
        flag=0
        break
    else:
        flag=1

if flag:
    print("It donesn't contains list ")


