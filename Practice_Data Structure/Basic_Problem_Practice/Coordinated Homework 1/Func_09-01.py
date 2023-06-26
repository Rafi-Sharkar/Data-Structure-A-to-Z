def prime(num):
    Prime = True
    for i in range(2,num):
        if num%i == 0:
            Prime = False
    return Prime


print(prime(21))
print(type(prime(11)))          # checking the data type is bool or not

