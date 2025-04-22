def p(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
        
n=int(input('enter a num: '))
if p(n):
    print('prime')
else:
    print('not prime')
    