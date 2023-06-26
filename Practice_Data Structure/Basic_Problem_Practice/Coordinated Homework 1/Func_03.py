# def fact(num):          # recursion mathod
#     if num==0 or num == 1:
#         return 1
#     else:
#         return num*fact(num-1)

# print(fact(6))      # function call


def fact(num):          #iratative way
    if num == 0 :
        return 1 
    else:
        f = 1
        for i in range(1,num+1):
            f = f*i
        return f

print(fact(7))      #function call
