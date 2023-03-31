def firstLast(numberList):
    firstNum = numberList[0]
    lastNum = numberList[-1]
    if firstNum == lastNum:
        return True
    else:
        return False


number = [10, 20, 30, 10, 21, 45, 75]
print("result is", firstLast(number))
