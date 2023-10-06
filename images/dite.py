import os

def getdate():
    import datetime
    return datetime.datetime.now()

def sonu():
    b=(int(input("Enter ( 1 for Add )( 2 for Retrive ) ")))
    if(b==1):
        c=(int(input("Enter ( 1 for Dite )( 2 for Exercise ) ")))
        if(c==1):
            with open("sonu1.txt","a") as s:
                s.write(" ["+str(getdate())+"] "+input("==> ")+"\n")
        elif(c==2):
            with open("sonu2.txt","a") as s:
                s.write(" ["+str(getdate())+"] "+input("==> ")+"\n")
    elif(b==2):
        d=(int(input("Enter ( 1 for Dite )( 2 for Exercise ) ")))
        if(d==1):
            with open("sonu1.txt") as s:
                print(s.read())
        elif(d==2):
            with open("sonu2.txt") as s:
                print(s.read())

def aman():
    b=(int(input("Enter ( 1 for Add )( 2 for Retrive ) ")))
    if(b==1):
        c=(int(input("Enter ( 1 for Dite )( 2 for Exercise ) ")))
        if(c==1):
            with open("aman1.txt","a") as s:
                s.write(" ["+str(getdate())+"] "+input("==> ")+"\n")
        elif(c==2):
            with open("aman2.txt","a") as s:
                s.write(" ["+str(getdate())+"] "+input("==> ")+"\n")
    elif(b==2):
        d=(int(input("Enter ( 1 for Dite )( 2 for Exercise ) ")))
        if(d==1):
            with open("aman1.txt") as s:
                print(s.read())
        elif(d==2):
            with open("aman2.txt") as s:
                print(s.read())

def raj():
    b=(int(input("Enter ( 1 for Add )( 2 for Retrive ) ")))
    if(b==1):
        c=(int(input("Enter ( 1 for Dite )( 2 for Exercise ) ")))
        if(c==1):
            with open("raj1.txt","a") as s:
                s.write(" ["+str(getdate())+"] "+input("==> ")+"\n")
        elif(c==2):
            with open("raj2.txt","a") as s:
                s.write(" ["+str(getdate())+"] "+input("==> ")+"\n")
    elif(b==2):
        d=(int(input("Enter ( 1 for Dite )( 2 for Exercise ) ")))
        if(d==1):
            with open("raj1.txt") as s:
                print(s.read())
        elif(d==2):
            with open("raj2.txt") as s:
                print(s.read())


a=(int(input("Enter ( 1 for Sonu )( 2 for Aman )( 3 for Raj ) ")))
if (a==1):
    sonu()
elif(a==2):
    aman()
elif(a==3):
    raj()
else:
    print("invalid input!")



