# lst = []

# def stack_in(arr, v):
#     arr.append(v)
#     print(arr)

# def stack_out(arr):
#     arr.pop()
#     print(arr)


# stack_in(lst, "Rafi")
# stack_in(lst, "Hasan")
# stack_in(lst, "Tanty")
# stack_in(lst, "Akash")
# stack_out(lst)
# stack_out(lst)
# stack_out(lst)
# stack_out(lst)

# lst_1 = ["I love Bangladesh"]


# l=input().split(", ")
# print(l)


# c="Bangladesh"


# def split_C(str):
#     i = 0
#     lst=[]
#     while(i < len(str)):
#         lst.append(str[i])
#         i=i+1
#     return lst
# print(split_C(c))
# print(list(c))

# a,b=map(int, input().split(" "))
# print(a+b)

# def ha():
#    i=input().split(" ")
#    a=int(i[0])
#    b=int(i[1])
#    print(a+b)
# ha()
# i = input().split(" ")
# a= sum(i)
# print(a)




# Python program to show working
# of map() function
 
# Return cube of n
def cube(n):
    return n**3
 
# Taking list as iterator
# evennum = [2,4,6,8]
# res = map(cube,evennum)
# print(res)


text = ""
count = dict()

for c in text:
    n = count.get(c,0)
    count[c] +=1


