while True:
    n=int(input('enter a num:  '))
    if n!=0:
        print('1.string')
        print('2.using cond')
        op=int(input('select approach: '))
        if op==1:
            if len(str(n))==3:
                print('3 digit num')
            else:
                print('not a digit num')
        elif op==2:
            if n>99 and n<1000:
                print('3 digit')
            else:
                print('not a 3 digit')
        else:
            print('choose valid option')
    else:
        break