

s=BST()
s.insert(11)
s.insert(2)
s.insert(20)
s.insert(15)
s.insert(28)
s.insert(14)

def countLeftNodes(root):
    cur=root
    if(cur==None):
        return 0
    if(cur!=None):
        par=cur
        return 1 +countLeftNodes(cur.left)
    return 1 +countLeftNodes(par.right.left)

print(countLeftNodes(s.root))
