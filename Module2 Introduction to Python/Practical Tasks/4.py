# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
str1 = input("Enter the first string = ")
str2 = input("Enter the Second string = ")
print("\n")
print("Original First String = ",str1)
print("Original Second String = ",str2)
str3 = str1[0:2]
str4 = str2[0:2]
# print(str3)
# print(str4)
str5 = str1.replace(str3,str4)
str6 = str2.replace(str4,str3)
print("\n")
print("Swaped first two characters = ",str5)
print("Swaped first two characters = ",str6)
print("\n")
print("Final answer = ",str5,"_",str6)
print("\n")