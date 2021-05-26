list1=[1,342,75,23,98,19,10]
list2=[75,23,98,12,78,10,1,1,342]
i=0
a=[]
while i<len(list1):
    b=list1[i]
    if b in list2:
        a.append(b)
    i=i+1
print(a)
