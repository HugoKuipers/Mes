import math
from random import randint

def makeNumLong(num, length):
    num = str(num)
    newNum = num
    if len(num) < length:
        for l in range(len(num), length):
            newNum = "0"+newNum
    return newNum

def stringer(fileX):
    with open(fileX, "r") as myfile:
        stringX = myfile.read()
        extra = len(stringX) % 3
        if extra > 0:
            extra = 3 - extra
            for i in range(extra):
                stringX += "\n"
        return stringX

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
        greatestOrd = str(len(str(greatestOrd)))
    else:
        greatestOrd = "6"
    tempKey += greatestOrd
    for i in range(0, len(x), 3):
        if not (x[i:i+3]) in tempRegistry:
            numInUse = False
            numVal = randint(0, 9999999999)
            numVal = makeNumLong(numVal, 10)
            if str(numVal) == "0123456789":
                numInUse = True
            for k in tempRegistry:
                if tempRegistry[k] == numVal:
                    numInUse = True
            while numInUse:
                numInUse = False
                numVal = randint(0, 9999999999)
                numVal = makeNumLong(numVal, 10)
                if str(numVal) == "0123456789":
                    numInUse = True
                for k in tempRegistry:
                    if tempRegistry[k] == numVal:
                        numInUse = True
            tempRegistry[x[i:i+3]] = str(numVal)
        newX += tempRegistry[x[i:i+3]]
    for i in tempRegistry:
        keyPiece = ""
        for c in i:
            j = makeNumLong((ord(c)*Xfactor), int(greatestOrd))
            keyPiece += j
        keyPiece += tempRegistry[i]
        tempKey += keyPiece
    endTempKey = ""
    for i in range(int(greatestOrd)):
        tempChar = i + Xfactor
        while tempChar > 9:
            tempChar -= 10
        endTempKey += str(tempChar)
    tempKey += (endTempKey+endTempKey+endTempKey+"0123456789")
    resultX = tempKey + newX
    return resultX

def numberR(numListX, name):
    numList = open(name, "w")
    numList.write(numListX)
    numList.close()

def docMes(docX):
    stringX = stringer(docX)
    numStringX = mes(stringX)
    numNumName = docX.replace(".", "NumNum") + ".txt"
    numberR(numStringX, numNumName)

def numStringer(numX):
    with open(numX, "r") as myfile:
        stringX = myfile.read()
        return stringX

def glue(x):
    Xfactor = x[0:1]
    z = int(Xfactor)
    greatestOrd = x[1:2]
    y = int(greatestOrd)
    keyLength = (y*3)+10
    registry = {}
    endRegistryPart = ""
    for i in range(y):
        tempChar = i + z
        while tempChar > 9:
            tempChar -= 10
        endRegistryPart += str(tempChar)
    endRegistry = endRegistryPart + endRegistryPart + endRegistryPart + "0123456789"
    for i in range(2, len(x), keyLength):
        if x[i:i+keyLength] == endRegistry:
            startReal = i+keyLength
            break
        firstLetter = x[i:i+y]
        firstLetter = int(int(firstLetter) / z)
        firstLetter = chr(firstLetter)
        secondLetter = x[i+y:i+2*y]
        secondLetter = int(int(secondLetter) / z)
        secondLetter = chr(secondLetter)
        thirdLetter = x[i+2*y:i+3*y]
        thirdLetter = int(int(thirdLetter) / z)
        thirdLetter = chr(thirdLetter)
        registry[x[i+3*y:i+3*y+10]] = firstLetter+secondLetter+thirdLetter
    returnOfTheString = ""
    for i in range(startReal, len(x), 10):
        returnOfTheString += registry[x[i:i+10]]
    return returnOfTheString

def returner(returnString, name):
    returnDoc = open(name, "w")
    returnDoc.write(returnString)
    returnDoc.close()

def docGlue(numDocX):
    numbersX = numStringer(numDocX)
    resultX = glue(numbersX)
    correctName = "New" + numDocX.replace("NumNum", ".")
    correctName = correctName[:-4]
    numberR(resultX, correctName)

# docMes("Testing.txt")
# docMes("TestingNumNumtxt.txt")
# docMes("TestingNumNumtxtNumNumtxt.txt")
# docMes("TestingNumNumtxtNumNumtxtNumNumtxt.txt")
# docMes("TestingNumNumtxtNumNumtxtNumNumtxtNumNumtxt.txt")
# docGlue("TestingNumNumtxt.txt")
