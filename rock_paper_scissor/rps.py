                        ########### Rock Paper Scissors   ###############

import random 

exit=False
user_score=0
computer_score=0

while exit ==False:
    options=["rock" ,"paper" , "scissor"]
    user_input= input("Enter choice rock , paper , scissor or exit\t")
    computer_input = random.choice(options)
    if user_input=="exit":
        print("Game Ended")
        print(f"Your Score is : {user_score}  and Computer Score is : {computer_score}")
        exit=True
    
    if user_input=="rock":
        if computer_input =="rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("it is tie")

        elif computer_input=="paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer Wins")
            computer_score+=1

        elif computer_input=="scissor":
            print("Your input is rock")
            print("Computer input is scissor")
            print("You Win ")
            user_score+=1    


    elif user_input=="paper":
        if computer_input =="rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You Win")
            user_score+=1

        elif computer_input=="paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("it is tie")
            
        elif computer_input=="scissor":
            print("Your input is paper")
            print("Computer input is scissor")
            print("Computer Wins ")
            computer_score+=1   


    elif user_input=="scissor":
        if computer_input =="scissor":
            print("Your input is paper")
            print("Computer input is rock")
            print("Computer Wins ")
            computer_score+=1 

        elif computer_input=="paper":
            print("Your input is scissor")
            print("Computer input is paper")
            print("You Win")
            user_score+=1

        elif computer_input=="scissor":
            print("Your input is scissor")
            print("Computer input is scissor")
            print("it is tie")


    elif user_input !=  "rock" or user_input !=  "paper" or user_input !=  "scissor" or user_input !="exit":
        print("Invalid Input")     



