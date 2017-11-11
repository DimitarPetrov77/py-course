n = int(input())
for i in range (0, n+1):
    print(' ', end='')
print('|')

for m in range (1, n+1):
    print(' ' * (n-1-m), end='')
    print('*' * (m+1), end='')
    print(' | ' * (n-m), end='')
    print('*' * (m+1))

