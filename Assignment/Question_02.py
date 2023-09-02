def collapseSequences(a,b):
    if len(a)==0:
        return ""
    
    if len(a)==1:
        return a
    
    if a[0]==b and a[1]==b:
        return collapseSequences(a[1:], b)
    else:
        return a[0] + collapseSequences(a[1:], b)
print(collapseSequences("aabaaccaaaaaada", 'a'))
print(collapseSequences("mississssipppi", 's'))
print(collapseSequences("tennessee", 'x'))