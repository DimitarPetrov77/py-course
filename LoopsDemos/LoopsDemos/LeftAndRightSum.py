n = int(input())

leftSum = 0
rightSum = 0

for i in range(1, 2*n+1):
    currentNum = int(input())
    if i <= n:
        leftSum += currentNum
    else:
        rightSum += currentNum

if leftSum == rightSum:
    print("Yes, sum = " + str(leftSum))
else:
    print("No, diff = " + str(abs(leftSum-rightSum)))