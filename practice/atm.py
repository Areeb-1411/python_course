balance=100000
t=[]

def withdraw(amount):
    global balance
    if amount<=balance:
        print("collect your cash")
        print("your remaining balance is: ",balance-amount)
        balance-=amount
        t.append(f'{amount} is withdrawn from your account')
        
    else:
        print("insufficient balance")
    
def deposit(amount):
    global balance
    balance+=amount
    t.append(f'{amount} is deposited to your account')
    print("amounted succuessfully deposited")
def checkbalance():
    print(f'the balance is {balance}')
def viewhistory():
    for i in t:
        print(i)

print("welcome to ATM")
while True:
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check Balance")
    print("4.View transaction")
    print("5.Exit")
    
    op=int(input("enter the selection(1-5): "))
    if op==1:
        am=int(input("enter the amount to withdraw: "))
        withdraw(am)
    elif op==2:
        am=int(input("enter the amount to deposit: "))
        deposit(am)
    elif op==3:
        checkbalance()
    elif op==4:
        viewhistory()
    elif op==5:
        print("thank you for using ATM")
        break
    else:
        print("Invalid option selected, Try again")