a=list(map(int,input("enter num").split()))
r=list(filter(lambda x:x%3==0,a))
print(r)