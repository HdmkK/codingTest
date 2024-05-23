s = list(input())


a = 1
b = 1

for c in s:
    if c == 'L':
        b += a
    elif c == 'R':
        a += b
        
print("#{} {} {}".format(test_case, a, b))