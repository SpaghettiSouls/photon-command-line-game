import pygame, os, time, random
from colorama import Fore, Back
pygame.init()
pygame.mixer.music.load('Music/Cloudy.mp3')
os.system('clear')
pygame.mixer.music.play(-1)
print(Fore.GREEN)

#set up variables to determine world state.
hasBadge = False
plan = False
identity = 'stranger'

#prompt to continue, stored in a variable to permit easy changing.
continuedialog = '    *ENTER>'


def promptForActions(choice1, choice2):
	while True:
		print('\n')
		print('       What is your decision? [' + choice1 + '/' + choice2 + ']')
		ans = input('                    >')
		if ans == choice1:
			return True
		elif ans == choice2:
			return False
		else:
			print('Try Again.')

#simple list output function, that's all.
def printList(list):
	for i in range(len(list)):
		print(list[i])


#ha ha funny text art
print('          _______      __      __       _______      _____________      _______      ___          __ ')
print('         |   ___  \   |  |    |  |    /   ___   \   |             |   /   ___   \   |   |        /  |')
print('         |  |   |  |  |  |____|  |   |  /     \  |  |____     ____|  |  /     \  |  |   |      /    |')
print('         |  |___|  |  |          |   |  |     |  |       |   |       |  |     |  |  |   |    /      |')
print('         |   ____ /   |   ____   |   |  |     |  |       |   |       |  |     |  |  |   |  /   /|   |')
print('         |  |         |  |    |  |   |  |     |  |       |   |       |  |     |  |  |   |/   /  |   |')
print('         |  |         |  |    |  |   |  \_____/  |       |   |       |  \_____/  |  |      /    |   |')
print('         |  |         |  |    |  |   |           |       |   |       |           |  |    /      |   |')
print('         |__|         |__|    |__|    \_________/        |___|        \_________/   |__/        |___|')

time.sleep(2.8)

print('\n\n')
print('                                           *PRESS ENTER TO PLAY*                                     ')
input('                                              [***********]                                          ')

os.system('clear')

#init text color
print(Fore.RED)

textlines = []
textlines.append('               ACT ONE:   HACKING AND ENTERING                                                       ')
textlines.append('                                                                                                     ')
textlines.append('                                                                                                     ')
textlines.append(' You are a pen tester working for a large corporation called \'Uniage, Inc.\' This company recently  ')
textlines.append('   hired some new IT professionals and various other security personnel. Your job is to hack into    ')
textlines.append('   the company\'s network and prove it with some data taken from a central server. They never told   ')
textlines.append('   you what is and isn\'t allowed, so everything is fair game. With your raspberry pi in your pocket ')
textlines.append('   and a smile on your face, you begin your hack.                                                    ')
printList(textlines)

time.sleep(2)
input(continuedialog)
os.system('clear')

textlines.append('\n')
textlines.append(' At the main building complex, you immediately notice a guard by the door. He doesn\'t seem to mind  ')
textlines.append('   you standing in the parking lot. You think about what to do first. You come up with two plans.    ')
textlines.append('   You can either walk up to the guard and tell him that you lost your badge and need a new one, or  ')
textlines.append('   you can stay and wait for a while until another opportunity presents itself.                      ')
printList(textlines)

time.sleep(2)
if promptForActions('guard', 'stay'):
	os.system('clear')
	textlines.append('                                                                                                     ')
	textlines.append(' You approach the guard with a friendly smile on your face. You tell him that you are an employee who')
	textlines.append('   has lost their badge somewhere. You ask if you could get a replacement one for now. He looks at  ')
	textlines.append('   you for a good thirty seconds and frowns. He tells you that he has never seen you before and to  ')
	textlines.append('   go away or he will call the police. Thinking quickly, you realize that only two options are left.')
	textlines.append('   You could lie about being new to the office building and hope for the best, or you could leave.  ')
	printList(textlines)

	time.sleep(2)
	if promptForActions('new hire', 'leave'):
		if random.randint(1, 5)==1:
			os.system('clear')
			identity = 'new hire'
		else:
			os.system('clear')
			textlines.append('\n He glares at you and tells you to leave. He isn\'t buying it.')
	else:
		os.system('clear')
		identity = 'stranger'

else:
	os.system('clear')
	textlines.append('                                                                                                    ')
	textlines.append(' You decide that you should be patient and wait. You take out your phone and pretend to make a call.')
	textlines.append('   A guard suddenly taps your shoulder from behind. Startled, you turn around. The guard hesitates, ')
	textlines.append('   then asks, are you new here? You are faced with an identity choice. Do you want to become a new  ')
	textlines.append('   hire, or are you just another employee in the parking lot?                                       ')
	printList(textlines)

	time.sleep(2)
	if promptForActions('new hire', 'employee'):
		os.system('clear')
		identity = 'new hire'
	else:
		os.system('clear')
		identity = 'employee'

if identity == 'new hire':
	textlines.append('                                                                                                     ')
	textlines.append(' You tell him that this is your first time working at this building and that you do not have a badge ')
	textlines.append('   yet. You ask if he could help with your problem. He tells you that he could let you through the ')
	if random.randint(1,2) == 1:
		textlines.append('   front enterance, if it would help. You thank him and follow him to the front door. As you walk  ')
	else:
		hasBadge = True
		textlines.append('   front door and give you a temporary replacement badge. You thank him and follow him. As you walk')
	textlines.append('   away, he wishes you luck on your first day.                           ')

elif identity == 'employee':
	textlines.append('                                                                                                     ')
	textlines.append(' You tell him that you are an employee and you lost your badge somewhere in the building. You tell   ')
	textlines.append('   him that last night, you and a few other employees left at the same time and somebody else      ')
	textlines.append('   had opened the door. You left the badge inside your desk in your workspace. He tells you to     ')
	textlines.append('   follow him to the door, and he lets you in. He wishes you luck in finding your badge.           ')

elif identity == 'stranger':
	textlines.append('                                                                                                     ')
	textlines.append(' You turn around and head back the way you came. I guess you have some social engineering lessons to ')
	textlines.append('   learn before you can get inside. At least you weren\'t arrested. The next time will be better.  ')

printList(textlines)

def finishMsg(actname):
	time.sleep(2)
	input(continuedialog)
	os.system('clear')

	print('  END OF ' + actname + '.')
	time.sleep(1)
	print('     you completed as: ' + identity)
	time.sleep(1)
	if hasBadge:
		print('       you have a badge!')
	else:
		print('       you have no badge yet....')
	time.sleep(1)
	if identity == 'stranger':
		print(Fore.YELLOW)
		print('\n  BETTER LUCK NEXT TIME!')
		exit()
	else:
		print(Fore.BLUE)
		print('\n  ACT COMPLETED!')
	print(Fore.RED)

finishMsg('ACT ONE:     HACKING AND ENTERING')
time.sleep(2)
input(continuedialog)
pygame.mixer.music.stop()
pygame.mixer.music.load('Music/Peace.mp3')
pygame.mixer.music.play(-1)

os.system('clear')
textlines.append('\n\n\n')
textlines.append('               ACT TWO:  ATTACK VECTOR                                                                ')
textlines.append('                                                                                                      ')
textlines.append(' You are now in the lobby. There is a receptionist busy at her desk, a restroom off to the side, and  ')
textlines.append('   an elevator right next to the receptionist\'s desk. Do you want to dip into the restroom and create')
textlines.append('   a plan of attack, or do you want to do something else?                                             ')
printList(textlines)

time.sleep(2)
if promptForActions('restroom', 'something else'):
	os.system('clear')
	textlines.append('                                                                                                     ')
	textlines.append(' You decide to hide out in the restrooms until you have a good plan of attack. You think over your   ')
	textlines.append('   your options. You will want to plant your raspberry pi somewhere secret, but it has to be         ')
	textlines.append('   connected to the company\'s network. There are plenty of secret places to plant the pi, but the   ')
	textlines.append('   problem is, you need to plant it inconspicuously in an office building full of employees. You     ')
	textlines.append('   can find an empty cubicle and plant the pi in there. Is this the plan you want, or do you want to ')
	textlines.append('   play it by ear?                                                                                   ')
	printList(textlines)

	time.sleep(2)
	if promptForActions('plan', 'no plan'):
		os.system('clear')
		plan=True
		textlines.append('                                                                                                    ')
		textlines.append(' You go with the plan. You will infiltrate an empty cubicle and plant the pi. For now, you go back  ')
		textlines.append('   to the lobby.                                                                                    ')
		printList(textlines)
		time.sleep(2)
		input(continuedialog)
	else:
		os.system('clear')
		plan=False
		textlines.append('                                                                                                    ')
		textlines.append(' To heck with the plan. You head back out into the lobby.                                           ')
		printList(textlines)
		time.sleep(2)
		input(continuedialog)
os.system('clear')
textlines.append('                                                                                                     ')
textlines.append(' You look around. The elevator is at your floor and the receptionist is busy. A second look at the   ')
textlines.append('   receptionist reveals that she is staring at you out of the corner of her eye. You give a friendly ')
textlines.append('   nod, just in case she was suspicious of you. She looks up from her work and asks if you are lost. ')
textlines.append('   What do you say?                                                                                  ')
printList(textlines)

time.sleep(2)
if promptForActions('yes', 'no'):
	os.system('clear')
	textlines.append('                                                                                                   ')
	textlines.append(' Yes, you say. You are lost and cannot find your office. You ask her for help. She frowns and asks ')
	textlines.append('   for your badge. You tell her you lost it and she asks for your name. You give her a fake name   ')
	if random.randint(1, 2) == 1:
		textlines.append('   and she tells you to not lose your badge this time. She hands you a temporary badge with your  ')
		textlines.append('   fake name on it, and motions you towards the elevator. She tells you to move on. You gladly    ')
		textlines.append('   oblidge.                                                                                       ')
		printList(textlines)
		hasBadge = True
	else:
		textlines.append('   and she types into a small laptop on her desk. Her eyes widen and she looks at you and calls   ')
		textlines.append('   the police right in front of you. Oh, well.                                                    ')
		printList(textlines)
		identity = 'stranger'
else:
	os.system('clear')
	textlines.append('                                                                                                   ')
	textlines.append(' No, you say. You were only waiting for a colleague to come by. She says okay and goes back to her ')
	textlines.append('   work. You think about what to do next. You need to plant your raspberry pi device somewhere it  ')
	textlines.append('   has access to the company\'s network. When it is planted, you will have remote access to it and ')
	textlines.append('   be able to run commands and exploits over it. If only there was somewhere to plug it in...      ')
	printList(textlines)

	time.sleep(2)
	input(continuedialog)
	os.system('clear')
	textlines.append('                                                                                                   ')
	textlines.append(' You walk towards the elevator to find somewhere to plug in the pi, but alas! the door is badge    ')
	if hasBadge:
		textlines.append('   locked! But wait! The guard gave you a badge! You open the elevator and pick a floor.   ')
	else:
		textlines.append('   locked! You don\'t have a badge, either! You can talk to the receptionist and ask for   ')
		textlines.append('   her to open it, or you can ask if she can give you a badge. She might be more cautious  ')
		textlines.append('   about giving you a badge, but if you ask her to open the door, she might be more open to')
		textlines.append('   helping you.                                                                            ')
	printList(textlines)
	time.sleep(2)
	if promptForActions('open door', 'give badge'):
		os.system('clear')
		textlines.append(' You walk over to the receptionist and tell her you forgot your badge, and you need to go  ')
		textlines.append('   up the elevator to grab it. She asks who you are, and you give her a fake name. She asks')
		if identity == 'new hire':
			if random.randint(1,3) == 1:
				textlines.append('   if you are a new hire, and you say yes. She mutters under her breath and opens the door.')
			else:
				textlines.append('   if you are a new hire, and you say yes. She says to hold on. She calls someone for a    ')
				textlines.append('   while and then hangs up. She looks straight at you and says that you don\'t work here.  ')
				if random.randint(1,2) == 1:
					textlines.append('   She proceeds to ask you to leave. Your smile drops and you trudge outside, back to the')
					textlines.append('   hotel.                                                                                ')
					identity = 'stranger'
				else:
					if hasBadge:
						textlines.append('   You show her your badge and tell her there is a mistake. She is taken aback, and then quiet.')
						textlines.append('   She wonders why you asked her to open the door if you had the badge, but she opens the door.')
					else:
						textlines.append('   She calls the police right before your eyes and when she hung up, she tells you to stay put.')
						textlines.append('   If you were illegally hacking....                            ....lets not think about that. ')
						identity = 'stranger'
		else:
			textlines.append('   if you are a new hire, and you say no. She reaches under her desk and...')
			if random.randint(1,3)==1:
				textlines.append('      ...she opens the door for you.')
			else:
				textlines.append('      ...she asks who you work with. you tell her you are with marketing, and she seems satisfied.')
				if random.randint(1,2)==1:
					textlines.append('   She calls marketing and asks if they have a guy with the name you gave her. She frowns at you. You make a ')
					textlines.append('   break for it, and you get away. Jeez. Imagine going to your client and saying you couldn\'t get past the  ')
					textlines.append('   receptionist.....         ...oh, well.                                                                    ')
					identity = 'stranger'
				else:
					textlines.append('   She lets you through the door. You walk through and go to a floor, feeling good.')
		printList(textlines)
finishMsg('ACT TWO: ATTACK VECTOR')
