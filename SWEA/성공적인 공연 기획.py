mem = list(map(int, input()))

#not_stand = sum(mem)
stand = 0
staff = 0

for i, v in enumerate(mem):
    if v == 0:
        continue
    
    # if stand + staff < i:
    #     staff += (i - stand + staff)
    if stand < i:
        staff += (i - stand)
        stand += (i - stand)
        
    #not_stand -= v
    stand += v
    
print(staff)