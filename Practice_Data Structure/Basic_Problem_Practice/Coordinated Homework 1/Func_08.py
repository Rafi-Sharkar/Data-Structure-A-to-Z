def LCD(num1, num2):
    result = num1
    if num1>num2:
        result = num2
    for i in range(1, result+1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    lcd = (num1*num2)//gcd      # LCS and GCD relation
    return lcd

print(LCD(15, 20))