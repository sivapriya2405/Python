import random
print("------------------------------------------------------------------------------------------------")
print("******Welcome to play ROCK PAPER  SCISSOR******")
print("******1st player is user and  2nd player is system******")
print("******If we entered the wrong Input more than three times ,system will Quit the Game!!!.******")
print("------------------------------------------------------------------------------------------------")

try:
    games=int(input("Enter the number of times to play the game : "))

    System=["ROCK" ,"PAPER" ,"SCISSORS"]
    wronginput=0
    i=0
    UI={"ROCK":"R","PAPER":"P","SCISSORS":"S"}
    Userpoint,systempoint,tie=0,0,0

    while(i<games):
        User=input("Give your Input[Rock or R ,Paper or P, Scissors or S] : ")
        Useraction=User.upper()
        #print(Validinput)
        #print(Useraction)
        validinput=False
        for key,value in UI.items():
                if value == Useraction:
                    Useraction=key
                    validinput=True
                    break
                elif key==Useraction:
                    Useraction=key
                    validinput=True
                    break
        if validinput:
            Systemaction=random.choice(System)
            Systemaction=Systemaction.upper()
            print("System input: ",Systemaction)
            #print("System input: ",Useraction)
            if Useraction==Systemaction:
                tie+=1
            elif Useraction=="ROCK":
                if Systemaction=="PAPER":
                    systempoint+=1
                else:
                    Userpoint+=1
            elif Useraction=="PAPER":
                if Systemaction=="SCISSORS":
                    systempoint+=1
                else:
                    Userpoint+=1
            elif Useraction=="SCISSORS":
                if Systemaction=="ROCK":
                    systempoint+=1
                else:
                    Userpoint+=1
            i+=1        
            #print("Userpoint input: ",Userpoint)
            #print("systempoint input: ",systempoint)
        else:       
            print("Please Enter the Valid Input Like ",Validinput)
            wronginput+=1
            print(wronginput)
        if wronginput==3:
            break;
        

    if wronginput==3:
        print("You Entered the Wrong Input has three times.So Play the game again")
    else:
        print("Total of number games:",games)
        print("System points ==>", systempoint)
        print("User point ==> ",Userpoint)
        print("Tie ===>" ,tie)
        if Userpoint==systempoint:
            print("Tie")
        elif Userpoint>systempoint:
            print("USER wins the game !!! Congrats !!!!")
        else:
            print("USER Lose the Game,Better Luck Next Time")
except Exception as ex:
  print(ex)
"""
------------------------------------------------------------------------------------------------
******Welcome to play ROCK PAPER  SCISSOR******
******1st player is user and  2nd player is system******
******If we entered the wrong Input more than three times ,system will Quit the Game!!!.******
------------------------------------------------------------------------------------------------
Enter the number of times to play the game : 3
Give your Input[Rock or R ,Paper or P, Scissors or S] : S
System input:  PAPER
Give your Input[Rock or R ,Paper or P, Scissors or S] : P
System input:  PAPER
Give your Input[Rock or R ,Paper or P, Scissors or S] : R
System input:  ROCK
Total of number games: 3
System points ==> 0
User point ==>  1
Tie ===> 2
USER wins the game !!! Congrats !!!!
"""
