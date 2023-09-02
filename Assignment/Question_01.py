def arroHandle(a, b, pos_1, pos_2):
    if(a==b):
         print(a)
         return
    if(a < pos_1):
        print(a,end=" > ")
    elif(a < pos_2):
        print(a,end=" -- ")
    else:
        print(a,end=" < ")
    
    arroHandle(a+1, b, pos_1, pos_2)

def printRange(a,b):
        if(a>b):
           print("Invalid input :( ")
           return
        pos_1 = (a+b)//2
        pos_2 = 0
        if (a+b)%2 != 0:
           pos_2 = pos_1 + 1
        arroHandle(a, b, pos_1, pos_2)   

printRange(-10,5)
 