n = int(input())

for i in range (1, n+1):
    print(' ' * (n-i), end='')
    print('* ' * (i))

for m in range (1, n):
    print(' ' * m, end="")
    print('* ' * (n-m))
