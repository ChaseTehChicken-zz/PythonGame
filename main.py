### IMPORTS ###

from time import sleep
import winsound

### VARIABLES ###

health = 20
healthMaximum = 20
score = 0
kills = 0
level = 0
money = 50
backpack = ['Stick', 'Water Bottle', 'Rock']
StickDamage = 2.5
GreenSlimeDamage = 1
possiblelocations = ['Diner', 'Library', 'Blacksmith']
## ENEMIES ##
slimeList = ['Green Slime', 'Blue Slime', 'Red Slime']

def gameover():
    if health <= 0:
        for _n in range(1, 21):
            print('\n')
        print('\033[1;31;40mGAME OVER')

### GAME ###


winsound.PlaySound("startmenu.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
name = input("A new adventurer appears! What is their name?: ")
print(f'Welcome {name}, a great adventure awaits you!')
sleep(2.0)
winsound.PlaySound("snowdin.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
print(f'Welcome to the village travellor!')
sleep(3.0)
print(f'I believe your name was {name} wasnt it?')
sleep(2.0)
print('Yes, that was it.')
sleep(1.5)
print('Anyways, welcome to our village')
sleep(2.0)
print('We have many things to do here')
sleep(2.0)
print('We have a library, where you can learn magic spells, or just read a novel')
sleep(5.0)
print('We also have a blacksmith, down by the river. He\'s a crazy guy, ignore most of what he says')
sleep(7.0)
print('Theres also an amazing diner down the road. Family owned and the best food in town.')
sleep(5.0)
print('Because its the only food in town...')
sleep(5.0)
print('Why dont you go explore? I\'ll be here until you get back.')
sleep(5.0)
print('Oh yeah! My name is Tyke! I live here. Uhh, yeah. OK, you can go explore')
print('Where do you want to go? Library, Blacksmith, or Diner?\n\033[1;31;40m')

while True:
    location = input("LOCATION: ")
    lowerlocation = location.lower()
    if lowerlocation == 'blacksmith':
        break
    elif lowerlocation == 'library':
        break
    elif lowerlocation == 'diner':
        break
    else:
        print("PLEASE ENTER A VALID LOCATION")

print(f'On your way to the {location}, you stumble across a green slime')
locationUpper = location.capitalize()
sleep(2.0)
print('It may look friendly, but trust me, the narrator, it isnt.')
sleep(4.0)
print("When you stumble across an enemy, you can run, or you can fight.")
sleep(2.0)
print('What do you choose to do now?')
while True:
    action = input("RUN OR FIGHT?: ")
    if action == 'fight':
        break
    else:
        print('Sorry you have to fight this one..')
print('Hi, narrator again.')
sleep(1.0)
print('You really think you can fight that thing with your fists??')
sleep(3.0)
print('HA!')
sleep(1.0)
print('You must first equip a weapon.')
sleep(3.0)
print('I\'m pretty sure I left a stick in your backpack')

while True:
    weapon = input('SELECT A WEAPON: ')
    if weapon == 'stick':
        print(f'SELECTED WEAPON IS NOW: {weapon}')
        sleep(3.0)
        print('Thats more like it. I\'ll leave you to it')
        sleep(2.0)
        print('TO ATTACK, TYPE attack')
        print('TO DEFEND, TYPE defend')
        print('TO RUN, TYPE run')
        print('TO SHOW MERCY OR SPARE YOUR OPPONENT, TYPE mercy')
        while True:
            action = input('WHAT DO YOU DO?:')
            if action == 'attack':
                break
            else:
                print('Sorry, you have to fight this one..')
        winsound.PlaySound('enemyapproaching.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        GreenSlimeHealth = 5
        print('YOU ATTACKED THE SLIME')
        sleep(1.0)
        GreenSlimeHealth = GreenSlimeHealth - StickDamage
        print(f'GREEN SLIME HEALTH IS NOW {GreenSlimeHealth}')
        sleep(3.0)
        print('GREEN SLIME IS ANGERED')
        sleep(1.0)
        print('GREEN SLIME ATTACKS')
        sleep(1.0)
        print(f'YOU LOSE {GreenSlimeDamage} HEALTH!')
        gameover()
        sleep(2.0)
        health = health - GreenSlimeDamage
        print(f'HEALTH: {health}')
        print('attack, run, mercy')
        action = input('WHAT DO YOU DO?:')
        while True:
            if action == 'attack':
                break
            else:
                print('Sorry, you have to fight this one..')
        print('YOU ATTACKED THE SLIME')
        sleep(1.0)
        GreenSlimeHealth = GreenSlimeHealth - StickDamage
        print(f'GREEN SLIME HEALTH IS NOW {GreenSlimeHealth}')
        print('YOU KILLED THE GREEN SLIME!')
        break
    else:
        print('Sorry, you only have a stick at the moment...')
sleep(3.0)
print('Wow..')
sleep(5.0)
print("I thought you would die there..")
sleep(2.0)
print("Oh well..")
sleep(3.0)
print(f'YOU ARRIVE AT {locationUpper}')
while True:
    if lowerlocation == 'diner':
        print(f"Welcome {name} to the Crapple Diner!")
        sleep(3.0)
        print('My name\'s Shaz')
        print("Would you like somthing to eat?")
        while True:
            eat = input("EAT?: ")
            answer = eat.lower()
            if answer == 'yes':
                print('Awesome!')
                sleep(2.0)
                print('We dont have much at the moment sorry...')
                sleep(2.0)
                print("Would you like some fries?")
                while True:
                    fries = input("EAT?: ")
                    if fries == 'yes':
                        print("Awesome!")
                        sleep(3.0)
                        print("I'll go get them ready!")
                        sleep(2.0)
                        print('Hi. Narrator again')
                        sleep(2.0)
                        print('Fun fact, eating heals you..')
                        sleep(2.0)
                        print('Yep.. thats all bye')
                        sleep(4.0)
                        print('As you sit in the diner.. you feel weird..')
                        sleep(3.0)
                        print(f'Im back! Here are your fries {name}! Enjoy!')
                        sleep(1.0)
                        print('Youre filled with something..')
                        sleep(3.0)
                        print('What is that feeling?')
                        sleep(2.0)
                        print('HEALTH IS NOW FULL!')
                        health = healthMaximum


                    if fries == 'no':
                        print("Ok then..")
                        sleep(3.0)
                        print("Enjoy the rest of your day!")
                        break
                    break
            elif answer == 'no':
                break
            else:
                print('PLEASE ANSWER IN A YES OR NO FORM')
    elif lowerlocation == 'library':
        print('Ah, hi Mark.. I was waiting for y-')
        sleep(5.0)
        print('Wait a minute..')
        sleep(2.0)
        print('Youre not Mark..')
        sleep(2.0)
        print('Wait! Are you?..')
        sleep(2.0)
        print('Sorry, excuse me. My name is Debbie..')
        sleep(2.0)
        print('Im not used to having people around here..')
        sleep(3.0)
        print(f'What was your name again? {name}?')
        sleep(2.0)
        print('Yeah, I think that was it..')