#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Introduction to the Game

""" Docstring:

A. Introduction 
This game is based on the horror movie Psycho. It consists of three stages and 
includes 3 loops. It has defined functions for start, win and fail. The stages are
based on scenes from the movie with a little ajust to make it playable. You win 
when you defeat Norman Bates.

Stage 1: Lobby
Stage 2: Cabin
Stage 3: House

B. Known bugs and errors: None

This game was created by Sebastian Valenzuela Urena.

"""
#Import random. Need this function to choose the door.

import random 

#Defining start function

def start():
    print ("""It is Halloween night, you are tired and alone driving along 
the road to return home. However, your house is very far away
so you decide to stop at Bates Motel to rest. Also, you see a big 
house next to the motel.""")
#Creating an input to continue 
    input(prompt="\n<<Press enter to continue>>\n")
    #Adding lobby function to send the player to that stage
    lobby()
    
#Defining lobby function

def lobby():
    print("""You are in the lobby of Bates Motel. A strange man is in the front desk. 

There is a label with his name:

"Norman Bates".
    
    What would you do?
    
    1. Ask for a cabin
    2. Leave
    3. Go to the bathroom""")
    
    #Creating an input to select a choice

    choice01 = input(prompt="\n").lower()
    
    #Creating a conditional statement
    #Adding multiple choices to control the code
    
    if "1" in choice01 or "1." in choice01 or    "cabin" in choice01 or "ask" in choice01:
        print("\nYou got cabin 2. He is going to give you a soda as a gift.")
        input(prompt="\n<<Press enter to continue>>\n")
        
        #Adding random function to select a random soda
        soda = ['Coke', 'Sprite', 'Canada Dry', 'Dr Pepper']
        soda01=random.choice(soda)
        print(f"You got a can of {soda01}. Enjoy it.")
        
        input(prompt="\n<<Press enter to continue>>\n")
        #Adding cabin function to send the player to the next stage
        cabin()
        
    #Adding elif to create multiple conditions
    
    elif "2." in choice01 or "2" in choice01 or "leave"    in choice01:
        print("\nIt starts to downpour. You can't leave.")
        input(prompt="\n<<Press enter to continue>>\n")
        #Adding lobby function to send the player back
        lobby()
        
    elif "3" in choice01 or "3." in choice01    or "bathroom" in choice01:
        print("\nNow that you went to the bathroom, you need to go back to the lobby.")
        input(prompt="\n<<Press enter to continue>>\n")
        #Adding lobby function to send the player back
        lobby()
    
    #Adding else to control the code
    
    else:
        print("\n<Not an option. Try again.>\n")
        input(prompt="<<Press enter to continue>>\n")
        #Adding lobby function to send the player back
        lobby()

#Defining cabin
        
def cabin():
    print("""You are about to sleep. Suddenly, you hear a loud scream 
of a woman coming from cabin 1.
    
    What would you do?
    
    1. Run away
    2. Call the police
    3. Go to investigate""")
    
    #Writing an input to select a choice
    
    choice02 = input(prompt="\n").lower()
    
    #Writing a conditional statement 
    #Adding multiple choices to control the code
    
    if "1" in choice02 or "1." in choice02 or "run" in choice02 or    "away" in choice02:
        print("""\nYou left the cabin. You go outside but it is downpouring. 
Therefore, you go to the house next to the motel.""")
        input(prompt="\n<<Press enter to continue>>\n")
        #Adding house function to send the player to the next stage
        house()
        
    #Adding elif to create multiple conditions
    
    elif "2" in choice02 or "2." in choice02 or "call" in choice02 or "police" in choice02:
        print("""\nOh no! Your phone is out of battery! You leave the cabin and 
go to the house next to the motel.""")
        input(prompt="\n<<Press enter to continue>>\n")
        #Adding house function to send the player to the next stage
        house()
        
    elif "3" in choice02 or "3." in choice02    or "investigate" in choice02:
        print("""\nYou go to cabin 1. You find the dead body of Marion Crane.
You turn around, the only thing that you see is a shadow of an old woman. 
You try to hide in a random place so she can't see you...""")
        
        #Adding a random function to choose a place to hide
        place01=['under the bed', 'behind the curtains', 'under the table']
        place02=random.choice(place01)
        input(prompt="\n<<Press enter to continue>>\n")
        print(f"""You hide {place02}. Unfortunately, Norman Bates dressed as an
old woman finds you.""")
        input(prompt="\n<<Press enter to continue>>\n")
        #Adding fail function to end the game 
        fail()
        
    #Adding else to control the code

    else:
        print("\n<Not an option. Try again.>\n")
        input(prompt="<<Press enter to continue>>\n")
        #Adding cabin function to send the player back
        cabin()
        
#Defining house 
        
def house():
    print("""You are in the house. Although you are terrified and your heart
is pounding because of the horrible scream, you want to find a telephone
and ask for help since your phone is out of battery.
            
There are two closed doors in the house, you randomly pick one.
            
Good luck!""")
    
    #Creating a while loop with conditional statement
    
    #Defining the doors
    
    door02  = ['Door 1', 'Door 2']
    
    doors = 2
    
    while doors > 0:
        door = random.choice(door02)
        #Adding input to select the door
        input (prompt="\n<<Press enter to randomly pick a door>>\n")
        print(door + " ")
        
        #Adding if to create the first door
        if door == door02[0]:
            print ("""\nYou enter into the basement, you find Mrs. Bates mummified body
in a chair. Suddenly, Norman Bates enters dressed as her mom with 
a knife. 
He is about to tell you something...""")
            
            #Creating dynamic string to enter the name
            
            name= input(prompt="\nEnter your name\n")
            print(f"""\n-Norman Bates: "Hello {name.capitalize()}, I am Mrs. Bates
and you're trespassing my property so I'm going to kill you".""")
            doors-=1
            #Adding norman function to send the player to that stage
            norman()
            #Adding break to close the loop
            break
        
        #Adding elif to create the second door
        elif door == door02[1]:
            print ("""You enter into Mrs. Bates room, you find a gun without bullets.
You need to find them quickly before Norman Bates arrives.""")
            doors-=1
            #Adding bullet function to send the player to that stage
            bullet()
            #Adding break to close the loop
            break
        
        #Adding else for good practice
        else:
            print("\n<Not an option. Try again.>\n")
            input(prompt="<<Press enter to continue>>\n")
            house()
            
#Defining norman
            
def norman():
    print("""\nYou need to yell his mother's name in order to make him get a
psychological shock so he can't stab you. 

Clue: It is the feminine version of Norman""")
    
    #Creating a while loop with conditional statement 
    
    #Defining the correct answer
    
    mother_name = 'Norma'
    
    name_attempts = 3
    
    while name_attempts > 0:
        #Adding capitalize function to control the answer
        name0_attempt = input(prompt="\nEnter Mrs. Bates first name.\n>").capitalize()
        
        #Creating the winning statement
        if name0_attempt == mother_name:
            print("\nYou yell him his mother's name. You make him get a pshycological shock.\n")
            win()
            #Adding break to close the loop
            break
            
        #Adding elif to loose chances
        elif name0_attempt != mother_name:
            name_attempts -= 1
        
        print(f"""\nYou have {name_attempts} chance (s) left.\n""")
        
        #Adding if to end the game when zero chances are left 
        if name_attempts == 0:
            #Adding the fail function to end the game
            fail()
            
        #Adding else for good practice    
        else:
            print("\n<Not an option. Try again.>\n")
            input(prompt="<<Press enter to continue>>\n")
            norman()
        
#Defining bullet
        
def bullet():
    print("""\nThere is a bed, a nightstand, a bookshelf, a crib and a desk.

Where are the bullets?""")
    
    #Creating a while loop with conditional statement
    
    bullets = 'Desk'
    
    bullet_attempts = 2
    
    while bullet_attempts > 0:
        bullet0_attempt = input(prompt="\nEnter the name of a furniture.\n>").capitalize()
        
        #Creating the winning statement
        if bullet0_attempt == bullets:
            print("\nYou found the bullets.\n")
            #Adding win fuction to end the game
            win()
            #Adding break to close the loop
            break
            
        #Adding elif to loose chances
        elif bullet0_attempt != bullets:
            bullet_attempts -= 1
        
        print(f"""\nYou have {bullet_attempts} chance (s) left.\n""")
        
        #Adding if to end the game when zero chances are left
        if bullet_attempts == 0:
            fail()
            
        #Adding else for good practice
        else:
            print("\n<Not an option. Try again.>\n")
            input(prompt="<<Press enter to continue>>\n")
            bullet()
        
#Defining fail
    
def fail():
    print ("""Norman Bates has killed you. He is going to throw away your corpse in a 
random place.""")
    input(prompt="\n<<Press enter to continue>>\n")
    #Adding a random fuction to select a random place 
    grave=['swamp','lake', 'water well']
    grave01= random.choice(grave)
    print(f"He throws your corpse away in a {grave01}. Rest in peace.")
    input(prompt="\n<<Press enter to continue>>")
    print ("\nGAME OVER\n")
    input (prompt="<<Press enter to play again>>\n")
    #Adding the start function to start the game again
    start()

#Defining win
    
def win():
    print("""You defeated Norman Bates. You escaped and survived!
You want to celebrate with someone.""")
    input(prompt="\n<<Press enter to continue>>\n")
    #Adding a random function to celebrate with someone
    celebration= ['friends','family', 'partner']
    celebration01 = random.choice(celebration)
    print(f"""You decide to have a dinner with your {celebration01} to celebrate!""")
    print("\nTHE END\n")
    input(prompt="<<Press enter to play again>>\n")
    #Adding the start function to start the game again
    start()

#Adding the start funciton to start the game
start()


# In[ ]:





# In[ ]:




