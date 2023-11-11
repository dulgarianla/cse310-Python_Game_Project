# Import necessary modules
from datetime import datetime
import sys

# Define lists for different parts of the story
#starter 
part0= ["deeper", "backout"]
#Real start 
part1= ["flashlight", "jar"]
#First spill
jar_pt1= ["run", "hide"]
flashlight_pt1=["follow", "look"]
#Second spill 
jar_pt2=["forest", "watchtower"]
flashlight_pt2=["cabin", "path"]
#Final spill
jar_pt3=["signal", "radio"]
flashlight_pt3=["hitchhike","road"]
#Play agin yes_no
answer=["yes","no"]

#just a title screen and not part of testing 
def GAMEOPENING(): 
    print("=======================================WELCOME=TO=CHOOSE=YOUR=OWN=ADVENTURE=============================================")
    print("This game adapts to the choices you make. The story is up you. Your choices matter.")
    print()
    print("Type in START to began.")
    user_picks = input("> ").lower()
    if "start" in user_picks:
        print()
        print("Choose Your Own Adventure (Version 1: Hunted Forest)")
        current_date_and_time = datetime.now()
        print(f"Current Date is: {current_date_and_time:%c }")
        
        print("---------------------------------------------------L-O-A-D-I-N-G--------------------------------------------------------")
        START()
    else: 
        print("------------------------------------------------------------------------------------------------------------------------")
        print("Did not understand user's command. Please try again.")
        GAMEOPENING()

#Start of the main story
def START():
    print("GAME HAS STARTED")
    print()
    print("You are a high school student that was dared to go into the so-called hunted forest by some of your friends. \n"
            "As you started to walk into the forest you keep getting the feeling that you are being watched. \n"
            "Do you continue to go DEEPER into the forest or BACKOUT?\n")

    user_picks = ""
    while user_picks not in part0:
        user_picks = input("Which way do you choose? ").lower()
        next_function = part0_choice(user_picks)
        next_function()

#This is still part of start just into two parts for testing purposes 
def part0_choice(user_picks):
    next_function = None
    if user_picks == "backout":
        print("You chose to back out. You thought it wasn't worth it of what could be in there.\n"
          "As you step up of the forest your friends laugh at you. You LOST the bet.")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again
        
    elif user_picks == "deeper":
        print("You chose to go deeper and deeper into the forest. You realize that you are lost. So you sign and reach to grab your phone.\n"
            "As your heart stops you so realize that you don't have your phone on you. It starts to get really dark out and you start to panic.\n"
            "As you are panicking you see two items leaning against a tree. The items are a FLASHLIGHT and JAR of fireflies \n")
        next_function = PART1
            
    else: 
        print ("Please type one of the all CAPITALIZED words. Try again.\n"
            "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = START
    return next_function
    

#Part 1 of the story with flashlight or Jar 
def PART1():
    print()
    user_picks = ""
    while user_picks not in part1:
        user_picks = input("Which one do you want to pick up? ").lower()
        next_function = part1_choice(user_picks)
        next_function()

#This is still part of PART 1 just into two parts for testing purposes 
def part1_choice(user_picks):
    next_function = None

    if user_picks == "jar":
        print("You pick up the jar of fireflies and give them a good shake. The fireflies lit up and as the forest lights up around you in a green glow.\n"
           "For a spilt second, you see a large creature stand right in front of you.\n"
           "As you heart stops the fireflies light starts to dim. In that moment you choose to RUN from the creature or HIDE hoping it wont find you?")
        next_function = JARpt1

    elif user_picks == "flashlight":
        print("You pick up the flashlight and turn it on. Luckily there is power. As you shine the flashlight forward,\n"
            "you see a pathway that looks like its been used before. Maybe this is your ticket out.\n" 
            "But as you start to go toward the path..you jump as you heard a noise off in the distance.\n" 
            "Do you FOLLOW the path and continue into the forest or LOOK around for what could've made the noise?")
        next_function = FLASHLIGHTpt1

    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
            "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = PART1                                                                                                                                                                                                                   
    return next_function

#A continuation of the jar of fireflies story line (part 1 out of 3)
def JARpt1(): 
    print()
    user_picks = ""
    while user_picks not in jar_pt1:
        user_picks = input("Which way do you choose? ").lower()
        next_function = jar_pt1_choice(user_picks)
        next_function()

#This is still part of JARpt1 just into two parts for testing purposes 
def jar_pt1_choice(user_picks):
    next_function = None
    if user_picks == "run":
        print("You chose to run from the huge creature but its no use. The creature got you and it brought you back to its cave. As it fests on you.")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again

    elif user_picks == "hide":
        print("You chose to hide from the creature and luckily you are safe but now you have to get out of there.\n "
           "Now that your light source doesn't work anymore. You now have to rely on the moon as your light.\n"
           "While looking around you see a watchtower in the distance.\n"
           "Do you go the WATCHTOWER or continue in the FOREST? ")
        next_function = JARpt2

    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
            "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = JARpt1
    return next_function
    

#A continuation of the flashlight story line (part 1 out of 3)
def FLASHLIGHTpt1():
    print()
    user_picks = ""
    while user_picks not in flashlight_pt1:
        user_picks = input("Which way do you choose? ").lower()
        next_function = flashlight_pt1_choice(user_picks)
        next_function()

#This is still part of FLASHLIGHTpt1 just into two parts for testing purposes
def flashlight_pt1_choice(user_picks):
    next_function = None
    
    if user_picks == "look":
        print("As you walked towards the noise, to take a look. You step in a bear trap! You scream 'AHHHHHHH!!!'. You are now trapped.\n" 
        "As you call for help for anyone, no one comes until you see this huge mud man thing comes towards you.\n"
        "You continue scream more for help but then you are gulped by the mud man.")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again

    elif user_picks == "follow":
        print("You chose to follow the path instead of going to look. As you are walking down the path you see a cabin illuminated light from in side.\n"
        "As you get closer to the cabin, you as see that the path still continue. Do go to the CABIN or continue with the PATH? \n")
        next_function = FLASHLIGHTpt2

    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
        "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = FLASHLIGHTpt1
    return next_function
    

#A continuation of the jar of fireflies story line (part 2 out of 3)
def JARpt2():
    print()
    user_picks = ""
    while user_picks not in jar_pt2:
        user_picks = input("Which way do you choose? ").lower()
        next_function = jar_pt2_choice(user_picks)
        next_function()

#This is still part of JARpt2 just into two parts for testing purposes
def jar_pt2_choice(user_picks):
    next_function = None
    if user_picks == "forest":
        print("You chose to continue in the forest but the huge beast like creature finds you. You start to run as fast as you can.\n"
            "As you are running. You slip and fall down a cliff. You dont make it.")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again

    elif user_picks == "watchtower":
        print("You stared heading towards the watchtower. As you get to the bottom of the tower, you see a ladder.\n"
            "As you start climbing up the ladder you hear noises around you. So you start to climb faster. As you make your way up to the tower's landing.\n"
            "You look in...Its dark inside you hope there's something in there that can help you. You go inside. Luckily the lights work!\n" 
            "You see a radio and a light signal. Do you go to the RADIO or the SIGNAL")
        next_function = JARpt3
    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
        "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = JARpt2
    return next_function 


#A continuation of the flashlight story line (part 2 out of 3)
def FLASHLIGHTpt2():
    print()
    user_picks = ""
    while user_picks not in flashlight_pt2:
        user_picks = input("Which way do you choose? ").lower()
        next_function = flashlight_pt2_choice(user_picks)
        next_function()

#This is still part of FLASHLIGHTpt2 just into two parts for testing purposes
def flashlight_pt2_choice(user_picks):
    next_function = None

    if user_picks== "cabin":
        print("You chose to walked up to the cabin. As you walk closer to the front door you notice something in the window. As you lean in,"
            "you see a man covered in blood and holding a knife. You freeze in shock, You try to gasp for air but then the man notices you.\n"
            "You cant move. You are frozen in fear. You try to escape but he stabs you. It looks like Your his next meal.")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again
    elif user_picks== "path":
        print("You decided to continue the path forward. As you are walking through this hunted forest you see a road up ahead.\n"
            "As you jump with joy you run closer to the road.\n"
            "You look to see if there are any cars or anything that could aim to human civilization. You then come up with two ideas.\n"
            "Continue walking down the ROAD or stick your thumb out aka HITCHHIKE and hope for the best.")
        next_function = FLASHLIGHTpt3

    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
        "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = FLASHLIGHTpt2
    return next_function 
    

#A continuation of the jar of fireflies story line (part 3 out of 3)
def JARpt3():
    print()
    user_picks = ""
    while user_picks not in jar_pt3:
        user_picks = input("Which one do you choose? ").lower()
        next_function = jar_pt3_choice(user_picks)
        next_function()

#This is still part of JARpt3 just into two parts for testing purposes
def jar_pt3_choice(user_picks):
    next_function= None
    if user_picks == "signal":
        print("You walk over to the light signal and try to turn it on but it seem to be broken. It seems your plan has failed.\n"
            "You then sit and wait, as hours went past, You later fell asleep and once you awoken you realize you have become lost within the forest.")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again
    elif user_picks == "radio":
        print("You walk over to the radio that you see sitting on the wooden desk. As you turn it on you hear a noise! A static comes from the radio.\n"
            "You jump for joy and you turn the knob around trying to catch a signal and boom you got a signal.\n"
            "You tell the people on the other side that you need help, that you are trapped in this forest.\n"
            "The person on the other end told you that they are coming to get you and help is on the way.\n"
            "You wait as you hear a helicopter flying over. You are saved. You get out of the hunted forest.")
        print("YOU WON!\n" 
            "Ending 1 out of 2")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again

    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
        "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = JARpt3
    return next_function
    

#A continuation of the flashlight story line (part 3 out of 3)
def FLASHLIGHTpt3():
    print()
    user_picks = ""
    while user_picks not in flashlight_pt3:
        user_picks = input("Which way do you choose? ").lower()
        next_function = flashlight_pt3_choice(user_picks)
        next_function()

#This is still part of FLASHLIGHTpt3 just into two parts for testing purposes
def flashlight_pt3_choice(user_picks):
    next_function= None 
    if user_picks == "hitchhike":
        print("You are tired of walking so you decide to wait and stand next to the road, while waiting, You stick out your thumb.\n"
            "Waiting for a car to drive by. As you are waiting. A car pulls up next to you and you feel so relieved. You step into the car\n"
            "but something is off. No one is in the car. When you realized this the car locks you in and you become trapped.\n"
            "You are banging the windows but nothing. Then the car starts to drive off very fast and after that you were never heard from again.\n")
        print("GAME OVER")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again
    elif user_picks == "road":
        print("You choose to just stay on the road and you began to walk down it. You still feel a bit uneasy.\n"
            "but then you hear a car in the distance. You pray that it's your classmates. You start to run towards the sound.\n"
            "Then you see car lights coming at you. It was your classmates. You are saved.\n")
        print("YOU WON!\n"
            "Ending 2 out of 2")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = play_again

    else: 
        print("Please type one of the all CAPITALIZED words. Try again.\n"
        "Do not worry you will start back at the level you where at.")
        print("------------------------------------------------------------------------------------------------------------------------")
        next_function = FLASHLIGHTpt3
    return next_function
    

def play_again():
    while True:
        user_picks = input("Do you want to play again? (YES or NO) ").lower()
        if user_picks == "yes":
            print("Okay! Thank you for choosing to play again! Enjoy!")
            return True
        elif user_picks == "no":
            print("Okay! Thank you for playing. Goodbye!")
            sys.exit()  # Exit the program
        else:
            print("Did not understand user's command. Please try again. Type either YES or NO.")

    
#STARTER
if __name__ == "__main__":
    while True:
        GAMEOPENING()
        if not play_again():
            break  # Exit the loop if the user chooses not to play again