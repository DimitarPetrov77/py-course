import math

figure = str(input())
if figure == 'square':
    a = float(input())
    print(round((a * a), 3))
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(round((a * b), 3))
elif figure == 'circle':
    r = float(input())
    print(round((math.pi * r * r), 3))
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    print(round(((a * h) / 2), 3))
