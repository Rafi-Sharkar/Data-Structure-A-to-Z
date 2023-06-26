def digit(num):           #itarative mathod. 
    sum = 0
    while num > 0:
        dt = num%10
        sum +=dt
        num = num//10
    print(sum)
digit(3456789)