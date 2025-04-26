def fun(s):
    ss=''
    for i in s:
        if i.islower():
            ss+=i.upper()
        elif i.isupper():
            ss+=i.lower()
        else:
            ss+=char
    return ss
if __name__=='__main__':
    s=input()
    print(fun(s))