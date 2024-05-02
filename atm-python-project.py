def welcome(n,a):
    account_no=str(input("enter the account number:"))
    for i in range(len(n)):
        if a[i]==account_no:
            print("welcome",n[i])


names=["kaviyadharshini","kalayarasi","sumila","keerthana"]
account_no=["iob980000067","st65000023","st65000098","ib64000023"]
welcome(names,account_no)
def enter(x,y):
    user_pin=int(input("enter your pin number:"))
    for i in range(len(x)):
        if x[i]==user_pin:
            choice=4
            while(True):
                print("\t\t1deposite")
                print("\t\t2withdrawal")
                print("\t\t3balance enquiry")
                print("\t\t4pin change")
                choice=int(input("enter number to proceed:"))
                print("\n\n")



                if choice==1:
                    amount=int(input("enter the amount"))
                    print("your amount is deposited")
                    print("if you want to check your current balance")
                    current_balance=str(input("enter yes or no:"))
                    if current_balance=="yes":
                        print(y[i]+amount)
                    else:
                        print("thank you")
                elif choice==2:
                    amount=int(input("enter the amount"))
                    print("your transaction has been processed")
                    print("collect your cash")
                    print("if you want to check your current balance")
                    current_balance=str(input("enter yes or no:"))
                    if current_balance=="yes":
                        print(y[i]-amount)
                    else:
                        print("thank you")
                elif choice==3:
                     print(y[i])
                else:
                     old_pin=int(input("enter your old pin"))
                     if old_pin==x[i]:
                         print("set your new pin")
                         new_pin=int(input("enter the new pin"))
                         print("confrim your new pin")
                         again=int(input("enter the new pin"))
                         if again==new_pin:
                             print("your pin has been set")
                         else:
                             print("pin mismatched")
                     else:
                              print("your pin is wrong")
                break




user_pin=[2123,2003,2004,2652]
user_balance=[8523.50,10256,6895.75,8695.12]
enter(user_pin,user_balance)


























            



