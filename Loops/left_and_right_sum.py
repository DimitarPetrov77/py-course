n = int(input())
leftSum = 0
rightSum = 0
for i in range(1, n+1):
    currentNum = int(input())
    leftSum += currentNum

for n in range(1 , n+1):
    currentNum = int(input())
    rightSum += currentNum
    
if leftSum == rightSum:
    print('Yes, sum= ' + str(leftSum))
else:
    print('No, diff= ' + str(abs(leftSum-rightSum)))
