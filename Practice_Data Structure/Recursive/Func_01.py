def rec_sum(n):
    if n < 0 :
        print("Invalid Input!")
    if n == 0 :         # Base Case
        return n
    return n+rec_sum(n-1)       # recursion call

print(rec_sum(3))      # output
