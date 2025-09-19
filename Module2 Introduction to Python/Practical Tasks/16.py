# 16.Counting the frequencies in a list using a dictionary in Python. Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

lst1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

if not lst1:
    print("no element is present")
else:
    freq_dict = {}
    for i in lst1:
        freq_dict[i] = freq_dict.get(i, 0) + 1
    
    for key, value in freq_dict.items():
        print(key, "-->", value)