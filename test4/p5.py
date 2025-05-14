def f(num):
    if num==0 or num==1:
        return 1
    else:
        return num*f(num-1)
while True:

    num=int(input("num plz: "))
    print(f"factorial of {num} is {f(num)}")