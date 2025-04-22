s=input('enter string: ')
r=""
c=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c=c+1
    else:
        r=r+s[i]+str(c)
        c=1
r=r+s[-1]+str(c)
print(r)