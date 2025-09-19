# --> 2. Write a Python program to count occurrences of a substring in a string.
main_str = input("Enter the main string = ")  # like: "abababab"
sub_str = input("Enter the Sub string = ")      # like: "aba"

count = 0
n = len(sub_str)

for i in range(len(main_str) - n + 1):    # (8-3+1) = 6 mean i will itreate = 6 times  0 to 5
    if main_str[i:i+n] == sub_str:         # it will be check the string like [0:3] = [aba]bababa == aba
        count += 1                          # aba = aba
                                             # if its geeting true than count + 1

print(f"{sub_str} substring is {count} times occurrences in the main string")