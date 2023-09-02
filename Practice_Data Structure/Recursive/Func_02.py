def revers(st,rev):
    if len(st)==0:
        return rev
    else:
        rev += st[-1]
        return revers(st[:-1], rev)
    
def Is_Palindrome(st):
    if(st==revers(st,"")):
        return True
    return False

name = "noon"
print(Is_Palindrome(name))




