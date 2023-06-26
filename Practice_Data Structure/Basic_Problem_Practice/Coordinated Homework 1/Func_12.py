st = "Hellow, Neha. What's going on. Are you free for a meet up"

def count_word(string):
    count = 0
    for i in string:
        if i == " ":
            count +=1
    return f"There have around {count+1} word"

print(count_word(st))
# make_upper(st)