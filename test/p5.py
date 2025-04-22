l=list(map(int,input('enter list: ').split()))
ul=[]
for i in l:
    if i not in ul:
        ul.append(i)
print(ul)