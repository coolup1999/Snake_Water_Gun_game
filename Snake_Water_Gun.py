import random
while True:
     computer_points = 0
     human_points = 0
     i = 10
     swg = [1,2,3]
     # swg_code = ["Snake", "Water", "Gun"]
     print("!!! SNAKE WATER GUN !!!\n")
     print("Hello users this game is developed by Upendra Gupta\n")
     try:
          select = int(input("Select 1 to start game & Select 2 for game rules:\n"))
          if(select==1):
               name = input("\nPlease Enter your name:")
               print("\n!!! Lets Start the Game !!!")
               while(i>0):
            
                    computer_choose = random.choice(swg)
                    human_choise = int(input("Select 1 for SNAKE\nSelect 2 for WATER\nSelect 3 for GUN\n"))
                    print("Computer Selected SNAKE and") if computer_choose==1 else  print("Computer Selected  WATER and") if computer_choose==2 else print("Computer Selected GUN and")
                    print(name," Selected SNAKE") if human_choise==1 else  print(name,"Selected  WATER") if human_choise==2 else print(name,"Selected GUN") if human_choise==3 else print("Its a Invalid choise",name," please select again\n")
                    if(computer_choose==human_choise):
                         print("\nDraw")
                    elif (computer_choose==1 and human_choise==2):
                         print("\nComputer Won")
                         computer_points = computer_points+1
                    elif (computer_choose==1 and human_choise==3):
                         print("\n",name,"Won")
                         human_points = human_points+1
                    elif (computer_choose==2 and human_choise==1):
                         print("\n",name,"Won")
                         human_points = human_points+1
                    elif (computer_choose==2 and human_choise==3):
                         print("\nComputer Won")
                         computer_points = computer_points+1
                    elif (computer_choose==3 and human_choise==1):
                         print("\nComputer Won")
                         computer_points = computer_points+1    
                    elif (computer_choose==3 and human_choise==2):
                         print("\n",name,"Won")
                         human_points = human_points+1
                    else:
                         continue

                    print("\nComputer point = ",computer_points,"&",name," points = ",human_points,"\n\n\n")
                    i = i-1    
               print("!!! ~~~ COMPUTER WON ~~~ !!!") if computer_points > human_points  else print("~~~ MATCH DRAW ~~~") if computer_points==human_points else print("!!! ~~~",name," WON ~~~ !!!") 



          elif(select==2):
               print("You have to select Snake, Water or Gun \n\nIf you choose Snake and computer choose Water than Snake will drink the water and you will loose\nIf you choose Snake and computer choose Gun than Gun will kill the snake and you will loose\nIf you choose Water and computer choose Gun than Gun will drown in the water and you will win\n\nThis game have 10 rounds, after 10 rounds the winner will be declared ")
          else:
               print("Please enter correct value")
     except:
          print("Please enter correct value")