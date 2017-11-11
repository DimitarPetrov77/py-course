from sys import maxsize

n = int(input())

smallest = maxsize
for i in range(1, n+1):
    currentNum = int(input())
    if currentNum < smallest:
        smallest = currentNum

print(smallest)