
def IUB_ID(ID):
    lst = ["2131130","2014158","2278136","1265326"]
    for i in lst:
        if i is ID:
            return True
        else:
            return False

print(IUB_ID("2131131"))
        