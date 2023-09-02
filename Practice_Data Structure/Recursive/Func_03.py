def revers(num,rev):
    if num==0:
        return rev
    else:
        rev = (rev*10)+(num%10)
        return revers(num//10, rev)
        

def checkPalindrome(num):
    rev_01 = revers(num,0)
    return rev_01 == num

input = 1234
print(checkPalindrome(input))