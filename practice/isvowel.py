while True:
    n=input('enter input(enter l to exit): ').lower()
    if n!='l':
        print('1.using membership')
        print('2.using cond')
        op=int(input('select approach: '))
    
        if op==1:
            vol='aeiou'
            if n in vol:
                print('is vowel')
            else:
                print('not vowel')
        elif op==2:
            if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
                print('is vowel')
            else:
                print('not vowel')
        else:
            print('select correct approach')
    else:
        break
    