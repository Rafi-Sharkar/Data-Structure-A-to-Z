def Perfect(num):
    sum = 0
    p = False
    for i in range(1, num):
        if num%i == 0:
            sum +=i
    if sum == num:
        p = True
    return p

print(Perfect(496))          # perfect numbers are 6, 28, 496, 8128, 33550336 etc