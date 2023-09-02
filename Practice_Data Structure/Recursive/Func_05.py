def reverseString(str):
    if len(str)==1:
        return str
    return reverseString(str[1:]) + str[0]

print(reverseString("rafi"))

'''
rs("rafi")
rs("afi") + r
rs("fi") + a 
rs("i") + f
return i

i -> if -> ifa -> ifar

'''