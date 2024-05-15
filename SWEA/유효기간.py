s = input()

#MMYY?
MMYY = False
a = s[:2]

if 1 <= int(a) <= 12:
    MMYY = True
    
#YYMM?
YYMM = False
b = s[2:]

if 1 <= int(b) <= 12:
    YYMM = True
    
if MMYY and YYMM:
    print("AMBIGUOUS")
elif MMYY:
    print("MMYY")
elif YYMM:
    print("YYMM")
else:
    print("NA")

