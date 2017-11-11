n = int(input())

print('*' * (n*2),end='')
print(' ' * n,end='')
print('*' * (n*2))
for i in range (0, n-2):
    print('*', end='')
    print('/' * (n*2-2), end='')
    print('*')

print('*' * (n * 2), end='')
print(' ' * n, end='')
print('*' * (n * 2))
