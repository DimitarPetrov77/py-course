n = int(input())

oddSum = 0
oddMin = 1000000000.0
oddMax = -1000000000.0

evenSum = 0
evenMin = 1000000000.0
evenMax = -1000000000.0

for i in range(1, n+1):
    currentNum = float(input())
    if i % 2 == 0:
        evenSum += currentNum
        if currentNum > evenMax:
            evenMax = currentNum
        if currentNum < evenMin:
            evenMin = currentNum
    else:
        oddSum += currentNum
        if currentNum > oddMax:
            oddMax = currentNum
        if currentNum < oddMin:
            oddMin = currentNum

if evenMax == -1000000000.0:
    evenMax = 0

if evenMin == 1000000000.0:
    evenMin = 0

if oddMin == 1000000000.0:
    oddMin = 0

if oddMax == -1000000000.0:
    oddMax = 0


if n == 1:
    print("OddSum=%g," % oddSum)
    print("OddMin=%g," % oddMin)
    print("OddMax=%g," % oddMax)
    print("EvenSum=%g," % evenMax)
    print("EvenMin=No,")
    print("EvenMax=No")
elif n == 0:
    print("OddSum=%g," % oddSum)
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=%g," % evenMax)
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print("OddSum=%g," % oddSum)
    print("OddMin=%g," % oddMin)
    print("OddMax=%g," % oddMax)
    print("EvenSum=%g," % evenSum)
    print("EvenMin=%g," % evenMin)
    print("EvenMax=%g" % evenMax)