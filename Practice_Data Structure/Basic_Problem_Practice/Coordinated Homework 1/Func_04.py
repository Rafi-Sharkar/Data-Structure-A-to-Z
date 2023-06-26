def digit(num):           #recursive mathod. it return reverce
    if num == 0:
        return 
    else:
        dt = num%10
        print(dt, end=",")
        num = num // 10
        return digit(num)

digit(3456789)