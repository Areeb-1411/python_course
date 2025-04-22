l=list(map(int,input('enter num: ').split()))
m1=m2=-1
for i in l:
    if i>m1:
        m2=m1
        m1=i
    elif i>m2 and i!=m1:
        m2=i
print(m1)
print(m2)




l=list(map(int,input('enter num: ').split()))
m1=max(l)
l.remove(max(l))
m2=max(l)
print(m1)
print(m2)

l1=list(map(int,input('enter num: ').split()))
l1.sort()
print("max: ",l1[-1])
print("2nd max: ",l1[-2])