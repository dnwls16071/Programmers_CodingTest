def solution(x1, x2, x3, x4):
    answer = True
    if x1 == True and x2 == True:
        temp1 = True
    elif x1 == True and x2 == False:
        temp1 = True
    elif x1 == False and x2 == True:
        temp1 = True
    else:
        temp1 = False
        
    if x3 == True and x4 == True:
        temp2 = True
    elif x3 == True and x4 == False:
        temp2 = True
    elif x3 == False and x4 == True:
        temp2 = True
    else:
        temp2 = False
        
    if temp1 == True and temp2 == True:
        return True
    elif temp1 == True and temp2 == False:
        return False
    elif temp1 == False and temp2 == True:
        return False
    else:
        return False