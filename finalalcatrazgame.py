#-*- coding: utf-8 -*- 
"""
        Text Adventure Game
        Created by Luke Bartini
        All rights reserved.
"""

####SOME ASCII ART TAKEN FROM THE INTERNET. ALL RIGHTS RESERVED TO THE RESPECTIVE OWNERCREATOR###

import random, sys, time

##### BASE FUNCTIONS #####

def slowPrint(s, delay = 0.025, maxLineLength = 80, deleteNewLines = True):
    
    import time, sys
    
    if deleteNewLines:
        s = s.replace('\n', ' ')
        s = s.replace('~', '\n')
    
    length = 0
    index = 0

    for c in s:
        index += 1
        length += 1
        if c == ' ':
            #Don't print the space if it is the first line character
            if length == 1:
                length -=1
                continue
            #If space is last character or would start next line don't print it
            if length >= maxLineLength - 1:
                length = 0
                print 
                continue
            nextWord = s[index:].find(' ')
            nextLine = s[index:].find('\n')
            if nextLine < nextWord and nextLine != -1:
                nextWord = nextLine
            if length + nextWord > maxLineLength and length > maxLineLength - 20:
                length = 0
                print
                continue
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
        if c == '\n':
            length = 0
        if length == maxLineLength:
            print
            length = 0
    print

def slowPrint2(s, delay = 0.0, maxLineLength = 80, deleteNewLines = True):
    
    import time, sys
    
    if deleteNewLines:
        s = s.replace('\n', ' ')
        s = s.replace('~', '\n')
    
    length = 0
    index = 0

    for c in s:
        index += 1
        length += 1
        if c == ' ':
            #Don't print the space if it is the first line character
            if length == 1:
                length -=1
                continue
            #If space is last character or would start next line don't print it
            if length >= maxLineLength - 1:
                length = 0
                print 
                continue
            nextWord = s[index:].find(' ')
            nextLine = s[index:].find('\n')
            if nextLine < nextWord and nextLine != -1:
                nextWord = nextLine
            if length + nextWord > maxLineLength and length > maxLineLength - 20:
                length = 0
                print
                continue
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
        if c == '\n':
            length = 0
        if length == maxLineLength:
            print
            length = 0
    print

###WELCOME SCREEN AND GRAPHICS ####

def welcomeScreen(): #starting screen text
    time.sleep(.5)
    dividerEqual = '=' * 35 #adds equals above and below text lines
    print dividerEqual.center(79, ' ')
    gameTitle = 'ESCAPE FROM ALCATRAZ. VERSION 1.0'
    print gameTitle.center(80, ' ') #prints it 80 spaces from the left edge, (center)
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    projectName = 'A Text Adventure Game'
    print projectName.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    creatorName = 'Created by Luke Bartini'
    print creatorName.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(1.5)
    print dividerEqual.center(79, ' ')
    copyrightDate = '© 2013. All rights reserved.'
    print copyrightDate.center(80, ' ')
    print dividerEqual.center(79, ' ')
    time.sleep(.5)

def introStory():
    print
    print #adds two spaces before text starts
    time.sleep(1)
    introText = 'A borderline genius…  that is what you are, said to have had an I.Q of 133, however you  have been convicted of many crimes throughout your life, including theft, bank robberies, possession of narcotics, and many armed robberies. You have been put into some of the most secure prisons in the USA and have still escaped from them all. However, there is one last option. You are sentenced to life in prison on “The Rock”, Alcatraz, a prison that nobody has ever successfully escaped from. You are prisoner number AZ1441. You quickly make friends and decide to start planning your escape from the inescapable prison. You, Frank Lee Morris are the mastermind of this escape, accompanied by Clarence Anglin, John Anglin, and Allen West.'
    luckText = 'I wish you the best of luck on your quest to freedom, you’ll need it. Some hints for your journey follow: '
    hintText1 = '√1.) Do not anger the guards, or else you will have to spend up to 7 days in "the hole", which is a dark room with no light at all and made of all concrete walls. You only get fed once a day, bread and water.'
    hintText2 = '√2.) Stay away from "the chamber" at all costs, it is similar to "the hole" but the gaurds will blast air conditioning until the temperature reachs an unbearable cold.'
    hintText3 = '√3.) Avoid Warden Johnson.'
    slowPrint (introText)
    time.sleep(5)
    print
    slowPrint (luckText)
    print
    time.sleep(3)
    slowPrint (hintText1) # prints out text
    time.sleep(3) # waits 3 sec. #
    slowPrint (hintText2)
    time.sleep(3)
    slowPrint (hintText3)

#***********GLOBAL DATA*************#
#**** GAME BEGINNING STARTS AFTER GLOBAL DATA ****#

def load_3():                   ###### LOADING SCREEN ######
    ##########CLOCK ANIMATIONS#######
    time.sleep(0)
    print '.        , - ~ ~ ~ - ,'
    print ".    , '               ' ,"
    print '.  ,                       ,' 
    print '. ,                         ,'
    print '.,                           ,'
    print '.,             0             ,'
    print '.,              \            ,'
    print '. ,              \          ,' 
    print '.  ,              \        ,'
    print '.    ,             \    ,'
    print ".      ' - , _ _ _ ,  '"
    time.sleep(.3)
    print '.        , - ~ ~ ~ - ,'
    print ".    , '               ' ," 
    print '.  ,                       ,' 
    print '. ,                         ,' 
    print '.,                           ,'
    print '.,             0             ,' 
    print '.,            /              ,' 
    print '. ,          /              ,'
    print '.  ,        /              ,' 
    print '.    ,     /            ,' 
    print ".      ' - , _ _ _ ,  '"
    time.sleep(.3)
    print '.        , - ~ ~ ~ - ,'
    print ".    , '               ' ," 
    print '.  ,                       ,'
    print '. ,                         ,' 
    print '.,_ _ _ _ _ _ _              ,' 
    print '.,             0             ,' 
    print '.,                           ,' 
    print '. ,                         ,' 
    print '.  ,                       ,'
    print '.    ,                  ,' 
    print ".      ' - , _ _ _ ,  '"
    time.sleep(.3)
    print '.        , - ~ ~ ~ - ,' 
    print ".    , '   \            ' ," 
    print '.  ,        \               ,' 
    print '. ,          \               ,' 
    print '.,            \               ,'
    print '.,             0             ,'
    print '.,                           ,' 
    print '. ,                         ,' 
    print '.  ,                       ,' 
    print '.    ,                  ,' 
    print ".      ' - , _ _ _ ,  '"
    time.sleep(.3)
    print '.        , - ~ ~ ~ - ,' 
    print ".    , '           /   ' ," 
    print '.  ,              /        ,' 
    print '. ,              /          ,' 
    print '.,              /            ,' 
    print '.,             0             ,' 
    print '.,                           ,' 
    print '. ,                         ,' 
    print '.  ,                       ,' 
    print '.    ,                  ,' 
    print ".      ' - , _ _ _ ,  '"

    time.sleep(.3)
    print '.        , - ~ ~ ~ - ,'
    print ".    , '               ' ," 
    print '.  ,                       ,' 
    print '. ,                         ,' 
    print '.,                           ,' 
    print '.,             0_ _ _ _ _ _ _,' 
    print '.,                           ,' 
    print '. ,                         ,' 
    print '.  ,                       ,' 
    print '.    ,                  ,' 
    print ".      ' - , _ _ _ ,  '"



#**********Game Beginning Option**********#

def startGame():
    print
    time.sleep(3)
    saveGameOption = slowPrint('Would you like to start a new game or continue from a saved game? If you wish to start a new game, type: new. If you would like to continue, type the name of your previous game. ')
    choiceOption = raw_input('').upper()
    time.sleep(.2)
    if choiceOption == 'NEW': ##what happens if new is chosen##
        time.sleep(1)
        slowPrint ('Please wait while the game is started...')
        time.sleep(3)
    else: # saved game #
        slowPrint('Please wait while the game is loaded...')
        time.sleep(3)
    ###Creates loading creen with loop###
    for x in range(1,4):
        for y in range(1,30):
          print '-' * y
    for y in range(1,30):
        print '-' * (31-y)
        continue
    time.sleep(3)
    
def room_1():  ### First room in game ###
    slowPrint('It is your first day at the prison and you lie awake scheming in your bed. There is a sink in front of you and a shelf above and to the right of you.')
    print
    time.sleep(3)
    slowPrint('Currently you have no tools available. Tools can be obtained by speaking to various workers and jailmates.')
    print
    time.sleep(3)
    slowPrint('Below is a floor plan of your cell room...')
    print
    time.sleep(3)
                    ##### FLOOR PLAN WITH ASCII ART ##
    slowPrint2('********************************************')
    slowPrint2('* ***\              Vent                   *')
    slowPrint2('* *   *                                    *')
    slowPrint2('* *   *                                    *')
    slowPrint2('* ***/                                     *')
    slowPrint2('*                                          *')
    slowPrint2('* *******************                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *       Bed       *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *                 *                      *')
    slowPrint2('* *******************                      *')
    slowPrint2('* *        |        *                      *')
    slowPrint2('* *        |        *                      *')
    slowPrint2('* *        |        *                      *')
    slowPrint2('* *******************                      *')
    slowPrint2('*                Cell Door                 *')
    slowPrint2('********************************************')
    time.sleep(1.5)
    ##data for examination of vent ##
    vent_1 = '__|__|__|__|__|__|__|__|__|__|__|'
    vent_2 = '_|__|__|__|__|__|__|__|__|__|__|_'
    print
    slowPrint('You have two options, you can either go to bed and start obtaning materials tomorrow, or you can explore any of the items/furniture in your cell.')
    time.sleep(1)
    slowPrint('Type sleep to sleep, or type: examine [item]. Replace [item] with something in your room.')
    print
    slowPrint('Note: Please examine items in the order of bed... cell door... and then vent.')
    slowPrint('What would you like to do?')
    ##user input##
    sleepOption = raw_input('').upper()
    if sleepOption == 'EXAMINE BED':
        slowPrint('Your bed is a standard single bed, with a cheap, old, matress pad. There is one cotton pillow, and under the bed there is a small storage area with nothing there.')
        time.sleep(1.5)
        slowPrint('Would you like to keep examining items or go to sleep?')
        sleepOption = raw_input('').upper()

    if sleepOption == 'EXAMINE CELL DOOR':
        slowPrint('The door is only openable by the guard. The guards have a key and also the doors can be programmed to open with a remote. There are thick steel bars about 3.5 inches apart.')
        time.sleep(1.5)
        slowPrint('Would you like to keep examining items or go to sleep?')
        sleepOption = raw_input('').upper()
    if sleepOption == 'EXAMINE VENT':
        slowPrint('There is a small vent, about 2 feet wide and 1 foot tall, with a cross hitched metal screen to allow ventalation and air conditioning come through into the rooms')
        slowPrint('A diagram of the vent follows...')
        time.sleep(2.5)
        ##MAKES A VENT DIAGRAM PRINTING THE DASHES OVER AND OVER ###
        slowPrint2(vent_1)
        slowPrint2(vent_2)
        slowPrint2(vent_1)
        slowPrint2(vent_2)
        slowPrint2(vent_1)
        slowPrint2(vent_2)
        time.sleep(3)
        print
        slowPrint('Would you like to keep examining items or go to sleep?')
        sleepOption = raw_input('').upper()
    if sleepOption == 'SLEEP':
        slowPrint('Okay, when you wake up you will go to the dining hall.')

def hallwayWalk_1():
    time.sleep(4)
    print
    slowPrint('The guards have just woken you up. Now you must get up and get ready to go to the daily morning meal. You get out of the cell and start walking towards the cafeteria. You must pass through many doors at the end of hallways. A picture of the doors follow... They are maximum security, steel doors.')
    time.sleep(2)                   ###ASCII ART FOR JAIL HALLWAY##
    print
    print
    slowPrint2('88888888888888888888888888888888888888888888888888888888888888888888888')
    slowPrint2("88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88")
    slowPrint2("88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88")
    slowPrint2("88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88")
    slowPrint2("88..__  |     |`-!._ | `.| |_______________||.;'|  _!.;'   |     _|..88")
    slowPrint2('88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|"| _!-|   |   _|..-|"    88')
    slowPrint2('88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|."j   |_..!-"|     |     88')
    slowPrint2("88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88")
    slowPrint2("88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88")
    slowPrint2("88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88")
    slowPrint2("88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88")
    slowPrint2("88      |    _!.-j'  | _!,'|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88")
    slowPrint2("88     _!.-'|    | _.'|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88")
    slowPrint2("88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``'..88")
    slowPrint2("88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `'.    |     88")
    slowPrint2("88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88")
    slowPrint2("88  _!''|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88")
    slowPrint2("88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88")
    slowPrint2("88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88")
    slowPrint2("88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88")
    slowPrint2("88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88")
    slowPrint2("88888888888888888888888888888888888888888888888888888888888888888888888")
    time.sleep(5)

def cafeteria_1():
    print
    slowPrint('You have reached the cafeteria and are in line getting a meal...')
    print
    time.sleep(2)
    slowPrint('You have two different options, 1, and 2... The options are below...')
    time.sleep(3.5)
    slowPrint('1')
    slowPrint2('1   Eggs & bacon    ___')
    slowPrint2('1          __..--"".--.`""--..__')
    slowPrint2('1    _..--"   _.--/    \""--.   "--..')
    slowPrint2("1  .'       .--.  '-..-'     ) (``\  '.")
    slowPrint2("1 |   .--''/    \-'''-. __.-' _.'  )   |")
    slowPrint2("1 ;\ (     '-..-'      )  _.-' _.-'   /;")
    slowPrint2("1  \'-:-._    _.._.-''`  ( ,.-'   _.-'/")
    slowPrint2("1   '-._ ``--`..___     __:.--''``_.-'")
    slowPrint2("1       ``--..___  `````  __..--``")
    slowPrint2("1                `````````")
    time.sleep(2)
    print
    print
    slowPrint2('2')
    time.sleep(2)
    slowPrint2('2_______________________________')
    slowPrint2('[_______________________________]')
    slowPrint2('|===============================|')
    slowPrint2('|   __                          |')
    slowPrint2("|._/_.' _, ,__  ,_ /_ _  / /'   |")
    slowPrint2("| / _  / / /// / // /(-'/ / /|  |")
    slowPrint2("| \__)(_(_//(_/_/(_/(__(_(_/_/_ |")
    slowPrint2("|            /                  |")
    slowPrint2("|       C O N D E N S E D       |")
    slowPrint2("|                               |")
    slowPrint2('|            .-"""-.            |')
    slowPrint2("|           /:`:..':\           |")
    slowPrint2("|==========|.:::::..:|==========|")
    slowPrint2("|           \::::::./           |")
    slowPrint2("|            `-:::-'            |")
    slowPrint2("|     ___                       |")
    slowPrint2("|      |  _ ,_ _  _ -|- _       |")
    slowPrint2("|      | (_)| | |(_| |_(_)      |")
    slowPrint2("|                               |")
    slowPrint2("|V( )V( )V(  S O U P  )V( )V( )V|")
    slowPrint2("|----------           ----------|")
    slowPrint2("'==============================='")
    time.sleep(2)
    print
    print
    slowPrint('What option will you choose?')
    time.sleep(.7)
    slowPrint('Hint: A spoon will be a useful tool later.')
    time.sleep(.8)
    slowPrint('1/2?')
    foodChoice_1 = raw_input('')        ###SIMPLE FOOD CHOICE If LOOP###
    if foodChoice_1 == '1' or '2':
        slowPrint('Okay... You must go sit down at a table.')
        time.sleep(.5)
        slowPrint('You can either sit with Al Capone, George Kelly and Sam Shockley, or you can sit with your partners in crime, John Aglin, Clarence Aglin and Allen West.')
        print
        time.sleep(1.5)
        slowPrint('A: Al Capone, George Kelly and Sam Shockley.')
        slowPrint('B: John Aglin, Clarence Aglin and Allen West.')
        tableChoice_1 = raw_input('').upper()
        if tableChoice_1 == 'B':
            slowPrint('Good choice...')
            print
            print                           ####TABLECHOICE LOOP###
            time.sleep(2)
        if tableChoice_1 == 'A':
            slowPrint('Are you sure you would like to sit with this rowdy group? They could get get sent to the hole if they cause a disturbance.')
            slowPrint('Would you like to sit here, or sit with John Aglin, Clarence Aglin and Allen West. Type Y to stay, type N to leave. (Y/N)')
            tableChoice_2 = raw_input('').upper()
            if tableChoice_2 == 'Y':
                slowPrint('You are making a large mistake')
                time.sleep(1)
                print
            if tableChoice_2 == 'N':
                slowPrint('Good choice...')
    time.sleep(1)
    print
    slowPrint('You should probably start thinking about obtaining tools to start digging your way out of your cell.')
    slowPrint('You can sneak either a knife, spoon or fork into your room.')
    time.sleep(2)
    slowPrint('Which one will you take?')     #PLAYER MUST WRITE spoon, fork, or knife#
    toolChoice_1 = raw_input('').upper()
    if toolChoice_1 == 'KNIFE':
        slowPrint('Okay... a knife is a good tool for picking the concrete from the walls around the vent, but it is risky to always keep one in your room.')
        print
        time.sleep(2)
        slowPrint2(' .------------------------.__________________________________')
        slowPrint2('/  == _  _  = _=   -  =  - \                                 `>')
        slowPrint2('| () _ =     _   ==  _  () |                               _,^')
        slowPrint2('\  _      ==  _=-   -  = _ /--^-^-^-^-^-^-^-^-^-^-^-^-^-^"`')
        slowPrint2(' "------------------------')
    if toolChoice_1 == 'SPOON':
        slowPrint('Good choice... a spoon is a great tool that will help you more than once on your journey.')
        print
        time.sleep(2)
        slowPrint2('.___           .-""-.')
        slowPrint2("/   '''---...-'.'  `\\")
        slowPrint2('\___...---"""-._-.__//')
        slowPrint2("                '---'")
        time.sleep(1)
    if toolChoice_1 == 'FORK':
        slowPrint("A fork is not a great tool, you can come back and try to get something else tomorrow, but you already have the fork hidden, and can't exchange it now.")
        print
        time.sleep(2)
        slowPrint2('||||')
        slowPrint2('||||')
        slowPrint2('\__/')
        slowPrint2('.|| ')          ###ASCII ART FOR SILVER WARE ^^^^###
        slowPrint2('.|| ')
        slowPrint2('.## ')
        slowPrint2('.## ')
        slowPrint2('.## ')
        slowPrint2('.## ')
        slowPrint2('.## ')
        print
        time.sleep(2)
        
def cell_room_2():          #POSSIBLE VARIABLES FOR LOAD SCREEN#
    load_3 = '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_'
    load_4 = '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-'
    time.sleep(2)
    print
    print
    slowPrint('You have succesfully brought the %s back to your room')
    
    time.sleep(2)
    slowPrint('The rest of the day has flown by, you have succesfully dug out the vent in your room and replaced it with a paper mache replica that a buddy made for you.')
    time.sleep(2)
    print
    slowPrint('You are now going to bed, once you wake up you will go to the second stage of your escape.')
    print
    time.sleep(2)
    for x in range(1,3):
        for y in range(1,30):           #loop for load, passing time while sleeping
          print('-' * y)
    for y in range(1,30):
        print('-' * (31-y))
        continue
    time.sleep(3.5)
    print
    print
    slowPrint('You get rudely awaken by the guards, saying that they are checking every inmate cell. Halfway through the check of your cell, they find silverware under your matress pad.')
    time.sleep(1)
    print
    slowPrint("The guards are very angry and you get sent to 'the hole'")
    slowPrint('While walking to the hole, the guard, Warden Johnson, says that you will rot in the hole for 3 whole days, with no food, and little water.')
    slowPrint('When a beam of light goes into the room, you can see a guillotin, an old pair of handcuffs, a skeleton and a rope.')
    print
    print
    time.sleep(3)
    slowPrint('There is nothing to do while in the hole. You will have to just wait it out.')
    slowPrint('...')
    time.sleep(1)

def roof_1():
    time.sleep(4)
    print
    print
    slowPrint('You have gotten out of the hole, and you are laying on your bed.')
    print
    time.sleep(1.5)
    slowPrint('Your partners have obtained everything that you guys need to attempt your escape')
    slowPrint('Would you like to attempt tonight? or tommorow night?')
    print('Tonight, Tomorrow')
    escapeChoice = raw_input('').upper()
    if escapeChoice == 'TONIGHT':           ##IF STATEMENT FOR ESCAPE CHOICE#
        slowPrint('Okay, you will meet your friends near the vents that lead up to the roof')
        print
        print 
    if escapeChoice == 'TOMORROW':
            slowPrint('Okay, the rest of the day and night will be simulated.')
            print
            time.sleep(2)
            load_3()
            load_3()
def escape():
    time.sleep(1)
    print
    print
    slowPrint('The time has finally come, the time of the escape attempt.')
    print
    slowPrint('As you guys planned, you and your three partners are in the walls of the prison. But to get up to the roof, you have to jump up to a another vent. The vent is on the ceiling, ten feet up. In order to get to the roof,you will need support from someone, and pull yourself through the vent hole.')
    slowPrint('.')
    time.sleep(.4)
    slowPrint('.')
    time.sleep(.4)
    slowPrint('.')
    time.sleep(.4)
    slowPrint('Only three people will make it out. Unfortunately one will be forced to stay behind because there will be no one to support the last person.')
    time.sleep(3)
    slowPrint('Since you are the leader, you will be the one to choose who stays behind.')
    slowPrint('Your options are...')
    slowPrint('1.) Clarence Aglin')
    slowPrint('2.) Allen West')
    slowPrint('3.) John Aglin')
    slowPrint('Will you leave behind 1, 2, or 3.')
    sacrificeChoice = raw_input('')         ###person who stays behind###
                                            #escape will only be possible if you leave behind 2
    if sacrificeChoice == '1':
        slowPrint("John: 'Nice job Frank, you just sacrificed my twin brother, after all we've done for you thrpughout your short time in ALcatraz. We always had your back through every step of the way. Thanks a lot, if my brother stays here, I am staying as well... Have fun escaping by yourself.")
    if sacrificeChoice == '2':
        slowPrint("Allen: 'Okay, I understand, take the stronger men. I will be out of here next year anyways. Good luck Frank, thanks for everything. I hope one day in the future we cross paths. Good bye.'")
    if sacrificeChoice == '3':
        slowPrint("Clarence: 'Nice job Frank, you just sacrificed my twin brother, after all we've done for you thrpughout your short time in ALcatraz. We always had your back through every step of the way. Thanks a lot, if my brother stays here, I am staying as well... Have fun escaping by yourself.'")

    if sacrificeChoice == '2':              #ESCAPE LOOOP .... what happens if 2 is left behind
        time.sleep(3)
        print
        print
        slowPrint('You have pulled yourself through the bars on the ceiling. Allen hands you the raft a nd life jackets you will need to travel across to San Francisco')
        time.sleep(2)
        slowPrint('You are on the roof, and there are spotlights that move all around the roof at different times. There are also large lookout towers with guards up top making sure there are no escape attempts.')
        slowPrint('You must push on forward, the city of San Francisco is a direct shot north.')
        time.sleep(2)
        slowPrint('Choose a direction (N,E,S,W)')       #DIRECTION
        d_1 = raw_input('').upper()
        if d_1 == 'N':
            time.sleep(2)
            slowPrint('You are heading north, and you are finally down on the ground, blowing up the rafts. Thanks to your partners, you have evaded all the guards and security.')
            time.sleep(2)
            slowPrint('Congrats, you are on the raft, and are paddling to freedom.')
            slowPrint('You have just escaped from the most secure prison in the world. Goodluck with the rest of your life. You deserved freedom.')
            slowPrint('Thank you for playing...')
        else:
            time.sleep(1)
            slowPrint('Oh no, the light is shining directly on you, the sirens start going off and the prison is in a lockdown sitaution. You have no escape. You surrender and soon get taken back into the jail, and are put into a maximum security room.')
            time.sleep(1)
            slowPrint('GAME OVER.')
            slowPrint('Thank you for playing.')
            
            
            
    else:           #what happens if you leave behind 1 or 2
        time.sleep(3)
        print
        print
        slowPrint('You have pulled yourself through the bars on the ceiling. Allen hands you the raft a nd life jackets you will need to travel across to San Francisco')
        time.sleep(2)
        slowPrint('You are on the roof, and there are spotlights that move all around the roof at different times. There are also large lookout towers with guards up top making sure there are no escape attempts.')
        slowPrint('You must push on forward, the city of San Francisco is a direct shot north.')
        time.sleep(2)
        slowPrint('Choose a direction (N,E,S,W)')
        #user input for direction
        direction_1 = raw_input('').upper()
        if direction_1 == 'N':
            slowPrint('OK, which way will you go now?')
            direction_2 = raw_input('').upper()
            if direction_2 == 'N':
                slowPrint('OK, which way will you go now?')
                direction_3 = raw_input('').upper()
                slowPrint('Oh no, the light is shining directly on you, the sirens start going off and the prison is in a lockdown sitaution. You have no escape. You surrender and soon get taken back into the jail, and are put into a maximum security room.')
                time.sleep(1)
                slowPrint('GAME OVER.')
                slowPrint('Thank you for playing.')
            else:
                slowPrint('Oh no, the light is shining directly on you, the sirens start going off and the prison is in a lockdown sitaution. You have no escape. You surrender and soon get taken back into the jail, and are put into a maximum security room.')
                time.sleep(1)
                slowPrint('GAME OVER.')
                slowPrint('Thank you for playing.')
        else:
            slowPrint('Oh no, the light is shining directly on you, the sirens start going off and the prison is in a lockdown sitaution. You have no escape. You surrender and soon get taken back into the jail, and are put into a maximum security room.')
            time.sleep(1)
            slowPrint('GAME OVER.')
            slowPrint('Thank you for playing.')
        

                
            
def main_0():
    welcomeScreen()
    introStory()
    startGame()
    room_1()
    hallwayWalk_1()
    cafeteria_1()
    cell_room_2()
    load_3()
    load_3()
    roof_1()
    escape()
    

##FINAL (MAIN) GAME LOOP##
main_0()
