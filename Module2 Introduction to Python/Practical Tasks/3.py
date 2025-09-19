# 3. Write a Python program to count the occurrences of each word in a given sentence.
str = input("Enter the string  = ")
str1 = str.split(" ")
for i in str1:
    print(i,"=",len(i))