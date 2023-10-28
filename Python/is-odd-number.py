def isOddNumber(num):
    val = num % 2
    if val != 0:
        return True
    else:
        return False
    
print(isOddNumber(3))