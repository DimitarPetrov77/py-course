from sys import maxsize

n = int(input())

# Get max size of int
biggest = -maxsize
sum = 0
for i in range(0, n):
    currentNum = int(input())
    if currentNum > biggest:
        biggest = currentNum
    sum += currentNum

sum -= biggest

if sum == biggest:
    print("Yes")
    print("Sum = " + str(sum))
else:
    print("No")
    print("Diff = " + str(abs(sum-biggest)))