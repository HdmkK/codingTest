p, q = map(float, input().split())

#s1
s1 = (1-p) * q


#s2
s2 = p * (1 - q)  * q 
print(s1, s2)
print("YES" if s1 < s2 else "NO")