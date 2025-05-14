def sort_scnd(t):
    return sorted(t,key=lambda x:x[1])
l=[]
n=int(input("how many values?"))
for i in range(n):
    fv=int(input("enter 1st"))
    sv=int(input("enter 2nd"))
    l.append((fv,sv))
sortedlist=sort_scnd(l)
print("sorted tupes based on 2nd value are:")
print(sortedlist)