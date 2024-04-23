P = list(input())
Q = list(input())

answer = "Y"
if len(P) != len(Q):
    if P[:-1] == Q and P[-1] == 'a' or P == Q[:-1] and Q[-1] == 'a':
        answer = "N"
else:
    if abs(ord(P[-1]) - ord(Q[-1])) == 1:
        answer = "N"
        
print()
        