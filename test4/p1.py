def g_even(num):
    for i in range(1,num+1):
        if i%2==0:
            yield i
while True:
    num=int(input("\n enter a num: "))
    for i in g_even(num):
        print(i,end=" ")