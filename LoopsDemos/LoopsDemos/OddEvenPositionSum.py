n = int(input())

oddSum = 0
evenSum = 0

for i in range(1, n+1):
    currentNum = int(input())
    if i % 2 == 0:
        evenSum += currentNum
    else:
        oddSum += currentNum

if evenSum == oddSum:
    print("Yes")
    print("Sum = " + str(evenSum))
else:
    print("No")
    print("Diff = " + str(abs(evenSum-oddSum)))