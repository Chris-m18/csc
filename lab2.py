num = int(input("enter a number: "))

factorial = 1

if num < 0:
    print("sorry, factorial does not exist for negative numbers ")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
        print("The factorial of", num, "is", factorial)

n = int(input('Enter n:  '))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1
    print("The sum is ", sum)
