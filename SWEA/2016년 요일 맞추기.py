m, d = map(int, input().split())

days = 0

mem = {
    1: 4,
    2: 5,
    3: 6,
    4: 0,
    5: 1,
    6: 2,
    0: 3
}

if m == 1:
    days = d
    
    ret = days % 7
    
    #print(mem[ret])
    print("#{} {}".format(test_case, mem[ret]))
else:
    for month in range(1, m):
        
        if month == 2:
            days += 29
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            days +=31
        else:
            days += 30
            
    days += d
    
    ret = days % 7
    print("#{} {}".format(test_case, mem[ret]))
    #print(mem[ret])
    
    
        