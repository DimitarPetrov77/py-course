n = int(input())
i= 2
prime = True
while i <= n:
    if n % i == 0 and i != 1 and i != n:
        prime = False
        break
        i += 1
if n < 2:
    print('Not prime')
elif prime:
    print('Prime')
else:
    print('Not prime')