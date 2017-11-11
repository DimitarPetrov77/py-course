n = int(input())

print('+ ', end='')
print('- ' * (n-2), end='')
print('+')

for i in range(0, n-2):
    print('| ', end='')
    print('- ' * (n - 2), end='')
    print('|')
print('+ ', end='')
print('- ' * (n-2), end='')
print('+')
