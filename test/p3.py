t=tuple(map(int,input('enter num: ').split()))
s=0
for i in t:
    if i%2!=0:
        s+=i
print(s)