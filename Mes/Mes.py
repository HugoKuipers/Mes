import math
from random import randint

testString = "alfa beta gamma Hi there"

def makeNumLong(num, length):
    num = str(num)
    newNum = num
    if len(num) < length:
        for l in range(len(num), length):
            newNum = "0"+newNum
    return newNum

def mes(x):
    tempRegistry = {}
    Xfactor = randint(1, 9)
    greatestOrd = 0
    tempKey = str(Xfactor)
    newX = ""
    for i in x:
        j = makeNumLong((ord(i)*Xfactor), 6)
        if int(j) > greatestOrd:
            greatestOrd = int(j)
    if len(str(greatestOrd)) < 6:
        greatestOrd = len(str(greatestOrd))
    else:
        greatestOrd = "6"
    tempKey += greatestOrd
    for i in range(0, len(x), 3):
        if not (x[i:i+3]) in tempRegistry:
            numInUse = False
            numVal = randint(0, 9999999999)
            numVal = makeNumLong(numVal, 10)
            for k in tempRegistry:
                if tempRegistry[k] == numVal:
                    numInUse = True
            while numInUse:
                numInUse = False
                numVal = randint(0, 9999999999)
                numVal = makeNumLong(numVal, 10)
                for k in tempRegistry:
                    if tempRegistry[k] == numVal:
                        numInUse = True
            tempRegistry[x[i:i+3]] = numVal
        newX += tempRegistry[x[i:i+3]]
    for i in tempRegistry:
        keyPiece = ""
        for c in i:
            j = makeNumLong((ord(i)*Xfactor), int(greatestOrd))
            keyPiece += j
        keyPiece += tempRegistry[i]
        tempKey += keyPiece
        print (keyPiece)
    return newX

newString = mes(testString)
print (newString)
