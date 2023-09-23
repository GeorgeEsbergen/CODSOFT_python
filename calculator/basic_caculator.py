def add (a,b):
    result=a+b
    print(f"##  {a} + {b} = {result}  ##")

def sub(a,b):
    result=a-b
    print(f"##  {a} - {b} = {result}  ##")

def multiple(a,b):
    result=a*b
    print(f"##  {a} * {b} = {result}  ##")

def division (a,b):
    result=a/b
    print(f"##  {a} / {b} = {result}  ##")


while True :
    
    choice=int(input("\n 1 for addition \n 2 for subtraction \n 3 for multiple \n 4 for division \n 5 for Exit  \n"))
    if choice ==1 :
       print("** Addition ** ")
       a=int(input("Enter First number : "))
       b=int(input("Enter Second number : "))
       add(a,b)

    elif choice ==2 :
         print("** Subtraction ** ")
         a=int(input("Enter First number : "))
         b=int(input("Enter Second number : "))
         sub(a,b)
    elif choice ==3 :
         print("** Multiple ** ")
         a=int(input("Enter First number : "))
         b=int(input("Enter Second number : "))
         multiple(a,b)
    elif choice ==4 :
         print("** Division ** ")
         a=int(input("Enter First number : "))
         b=int(input("Enter Second number : "))
         division(a,b)

    elif choice ==5:
         quit() 

    else : 
      print("Wrong Choice")





