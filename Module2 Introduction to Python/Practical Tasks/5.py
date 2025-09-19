# 5. Write a Python program to add 'ing' at the end of a given string (length shouldbeat least 3). If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged
str = input("Enter any verb = ")
len1 = len(str)
if len1>=3:
    if str.endswith("ing"):
        print(f"{str}ly")
    else:
        print(f"{str}ing")
else:
    print(str)