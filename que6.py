n=["mona","usha","nikki","mona","preeti","usha"]
i=0
l=[]
while i<len(n):
    a=n[i]
    if a not in l:
        l.append(a)
    i=i+1
print(l)

