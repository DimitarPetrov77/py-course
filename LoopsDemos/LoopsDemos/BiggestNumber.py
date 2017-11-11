import sys

num = int(input())

biggest = -sys.maxsize

for index in range(1, num+1):
    currentNum = int(input())
    if currentNum > biggest:
        biggest = currentNum

print(biggest)