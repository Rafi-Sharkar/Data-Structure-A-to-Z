# def rev(num):
#     if num == 0:
#         return
#     else:
#         dt = num %10
#         print(dt, end="")
#         num = num //10
#         return rev(num)
    
# rev(45678)

def rev(num):
    lst = []
    while num > 0:
        dt = num % 10
        num = num // 10
        lst.append(dt)
    # st = "".join(lst)
    return lst

print(rev(5678))