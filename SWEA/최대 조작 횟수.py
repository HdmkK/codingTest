a, b = map(int, input().split())


# count = 0
# while a < b:
#     if b - a >= 2:
#         b -= 2
#         count +=1
#     if a == b or b - a == 1:
#         break

count = 0
if b- a >= 2:
    count = int((b-a)/2)

if a != b and count == 0:
    print(-1)
elif a == b and count == 0:
    print(0)
else:
    print(count)
    
        
    
    