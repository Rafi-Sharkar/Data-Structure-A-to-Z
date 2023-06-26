def HCF(num1, num2):        # it's also call as GCD
    hcf = 0
    smallest = num1
    if num1 > num2:
        smallest = num2
    for i in range(1,smallest+1):
        if num1 %i == 0 and num2 % i == 0:
            hcf = i
    
    return hcf

print(HCF(12,30))
