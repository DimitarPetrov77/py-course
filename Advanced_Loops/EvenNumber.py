while True:
    try:
        n = int(input())
        if n % 2 == 0:
            break
    except:
        print('Invalid number!')
print('Even number entered: ' + str(n))


