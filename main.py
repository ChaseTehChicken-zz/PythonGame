from time import sleep
import winsound
health = 20
score = 0
kills = 0
level = 0
money = 50
backpack = ['Stick', 'Water Bottle', 'Rock']
StickDamage = 2.5
GreenSlimeDamage = 1

name = input("A new adventurer appears! What is their name?: ")
print(f'Welcome {name}, a great adventure awaits you!')
sleep(2.0)
winsound.PlaySound("village.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
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
print('Where do you want to go? Library, Blacksmith, or Diner?')
location = input('LOCATION: ')
print(f'On your way to {location}, you stumble across a green slime')
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
    action = input('WHAT DO YOU DO?:')
    while True:
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
    print(f'YOU LOSE {GreenSlimeDamage} health!')
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

    enddemo = input('This is the end of my demo V1. Press enter to finish :)')

