string = input()
mem = {
    "o": 0,
    "x": 0
}
for c in string:
    mem[c] += 1
    
if 15 - len(string) >= 8 - mem["o"]:
    print("#{} YES".format(test_case))
else:
    print("#{} NO".format(test_case))