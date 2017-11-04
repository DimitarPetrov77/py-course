num = int (input())

biggest = -10000000000000
for i in range (1, num + 1):
    currentNum = int(input())
    if currentNum > biggest:
        biggest = currentNum

print(biggest)