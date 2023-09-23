import string , random

charts=list(string.ascii_letters+string.digits+"@#*&!")


def generate_password():
    passwordLength = int(input("Enter Password Length "))
    random.shuffle(charts)
    password =[]

    for i in range(passwordLength):
        password.append(random.choice(charts))

    random.shuffle(password)

    password = "".join(password)

    print(password)



option=input("Do You Generate Password ? y/n ")

while True : 
    if option=="y":
        generate_password()
    elif option =="n" :
        print("Program Ended")
        quit()
    else:
        print("You Should choose y or n")
        quit()
              


