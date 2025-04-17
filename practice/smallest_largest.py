while True:
    a,b=map(int,input('enter two num: ').split())

    print('1.largest of two num')
    print('2.smallest of two')
    print('3.exit')
    op=int(input('select approach: '))
    if op==1:
        print('greatest num is ',max(a,b))
    elif op==2:
        print('smallest num is ',min(a,b))
    elif op==3:
        print('exited')
        break
    else:
        print('select correct approach')