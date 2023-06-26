lst = [-15, -26, 15, 1, 23, -64, 23, 76]

def sort(arr):
    s_lst = []
    min = arr[0]
    max = arr[0]
    sum = 0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
        sum+=i
    avg = sum/(len(arr))


    return f"Main Array = {arr}\nMinimum = {min}\nMaximum = {max} \nAverage = {avg}"

print(sort(lst))
