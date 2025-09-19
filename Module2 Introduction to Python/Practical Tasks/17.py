# 17.Write a python program using function to find the sum of odd series and even series :
# Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
# Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n

end = int(input("Enter the ending number = "))
sum=0
sum2=0

print("\nEven number series = ")
for i in range(1,end+1):
    if i%2==0:
        sum=sum+i
        print(i,end=" ")


print("\n\nOdd number series = ")
for i in range(1,end+1):
    if i%2!=0:
        sum2=sum2+i
        print(i,end=" ")
print("\n\nSum of the Even number series = ",sum)
print("\nSum of the Odd number series = ",sum2)