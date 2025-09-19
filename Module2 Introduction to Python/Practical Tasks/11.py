# 11.Write a Python program to unzip a list of tuples into individual lists. 
tpl = [(1,'a'),(2,'b'),(3,'c')]
lst1 = [t[0] for t in tpl]
lst2 = [t[1] for t in tpl]
print("numeric list = ",lst1)
print("String list = ",lst2)
