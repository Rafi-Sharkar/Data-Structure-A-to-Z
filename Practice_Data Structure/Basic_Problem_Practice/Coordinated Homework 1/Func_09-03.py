def palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        digt = num%10
        rev = rev*10 + digt
        num = num//10
    if temp ==  rev:
        return True
    else:
        return False

print(palindrome(1211))