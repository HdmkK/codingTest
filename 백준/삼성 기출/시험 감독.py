N = int(input())
people_each_room = map(int, input().split())
B, C = map(int, input().split())


total = 0
for people in people_each_room:
    
    need_each_room = 0
    
    if B >= C:
        
        need_each_room +=1
        people -= B
            
        if people < 0:
            people = 0
            
        share = int(people/C)
        remainder = people%C
        if remainder > 0:
            share+=1
        need_each_room +=share
            
    elif B < C:
        need_each_room +=1
        people -= B
        
        if people < 0:
            people = 0
            
        share = int(people/C)
        remainder = people%C
        if remainder > 0:
            share+=1
        need_each_room +=share
        
    total += need_each_room
    
print(total)