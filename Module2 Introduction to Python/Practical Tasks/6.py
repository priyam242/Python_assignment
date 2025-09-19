# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
# Get input from user
str = input("Enter a string: ")

# Find where 'not' and 'poor' appear
not_ = str.find('not')
poor = str.find('poor')

# Check conditions and replace if needed
if not_ != -1 and poor != -1 and not_ < poor:
    # Replace 'not...poor' with 'good'
    result = str[:not_] + 'good' + str[poor+4:]
    print(result)
else:
    # Print original string if condition not met
    print(str)