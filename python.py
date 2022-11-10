def createPartition(l,a):
    r=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if a=='+' and (l[i]+l[j])==n:
                r.append([l[i],l[j]])
            if a=='-' and (l[i]-l[j])==n:
                r.append([l[i],l[j]])
            if a=='*' and (l[i]*l[j])==n:
                r.append([l[i],l[j]])
            if a=='/' and (l[i]/l[j])==n:
                r.append([l[i],l[j]])
    return r
    
#constraints =>3
def check_duplicate(l):
    e=[]
    for i in range(len(l)):
        if l[i] not in e:
            e.append(l[i])
    if e==l:
        return True
    else:
        return False
    
a=input() # operator input
n=int(input()) # compared input
b=int(input()) #length of the list
l=[]
for i in range(b):
    x=int(input())
    l.append(x)
#constraints => 1,2,3
if b>2 and (a=='+' or a=='-' or a=='*' or a=='/') and check_duplicate(l):
    print(createPartition(l,a))
else:
    print("Invalid Input")
