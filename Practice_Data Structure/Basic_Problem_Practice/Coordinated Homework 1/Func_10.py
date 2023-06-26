lst = [-15, -26, 15, 1, 23, -64, 23, 76]

def sort(arr):
    s_lst = []
    while arr:
        min = arr[0]
        for i in arr:
            if i < min:
                min = i
        s_lst.append(min)
        arr.remove(min)
    return s_lst

print(lst)
print(sort(lst))