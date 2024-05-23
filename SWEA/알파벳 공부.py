
lexi = "abcdefghijklmnopqrstuvwxyz"
string = input()

count = 0
for i in range(len(string)):
    if string[i] == lexi[i]:
        count += 1
    else:
        break
    
print(count)
    