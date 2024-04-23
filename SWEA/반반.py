import collections
string = input()

mem = collections.Counter(string)
answer = "No"
if len(mem) == 2:
    for v in mem.values():
        if v == 2:
            answer = "Yes"
            
print(answer)


