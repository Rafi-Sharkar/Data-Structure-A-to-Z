def GCD(num_1, num_2):
    if num_2 <= 0:
        return num_1
    return GCD(num_2, num_1%num_2) 

print(GCD(60, 24))