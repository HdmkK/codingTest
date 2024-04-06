from collections import defaultdict
import heapq

student_num = int(input())

mem = []

for i in range(student_num):
    mem.append([])
    for num in list(map(int, input().split())):
        mem[i].append(num)

student_dict_list = []
for i in range(1, student_num+1):
    student_dict_list.append({})

    
#1학년 ~ 5학년
for i in range(5):
    
    dict = defaultdict(list)
    for student in range(1,student_num+1):
        dict[mem[student-1][i]].append(student)
    
    
    for key, value in dict.items():
        for student in value:
            for friend in value:
                if student == friend:
                    continue
                else:
                    student_dict_list[student-1][friend] = -1
    
heap = []
for student in range(1, student_num+1):
    
    heapq.heappush(heap, (-len(student_dict_list[student-1]), student))
    

_, candidate = heapq.heappop(heap)

print(candidate)

                    

                

    
    