from race_class_loader import *

#
#   It's called 'char_setup_checks' but the function is called 'start_up'?
#   I changed it to setup
#
#   Changed the loop checker to get a race from the list to a 'if char_race in...' thing.
#

def race(): #Check's if the user has chosen an actual race.
    races = ['Elf', 'Human', 'Half-Elf', 'Half elf', 'Half Elf', 'Half Orc','Dwarf', 'Halfling', 'Dragonborn', 'Teifling']
    race_keys = {'Dwarf':'dw','Elf':'el', 'Halfling':'hl', 'Half-Elf':'he','Half-Orc':'ho', 'Dragonborn':'db', 'Human':'hu', 'Teifling':'tl'}
    while True:
        char_race = str(input('>> Choose a race, dude: '))
        if char_race in races:
            print('>> Duuuuude, I love', char_race+'s, brah.')
            return race_keys[char_race]
        else:
            print('>> Whu? is that a race?')



def c_class():
    classes = ['Bard','Fighter', 'Rouge', 'Ranger', 'Monk', 'Wizard', 'Warlock','Sorcerer']
    NO_classes = len(classes)
    while True:
        char_class = str(input('>> Choose a Class, brah: '))
        for num in range(0,NO_classes):
            if char_class == classes[num]:
                return char_class



def stat_check(stat_type):
    while True:
        try:
            stat = int(input(stat_type))
            if stat > 30:
                print('>> Dude, stats only go to, like... 30, bro.')
            elif stat <=3:
                print('>> Stats usually only go down to three, so...')
            else:
                return stat
        except ValueError:
            print('>> Wha? That... isn\'t a number, man.')
        print('>> Try agian I guess?')



def stat_mod(stat):
    if stat => 10:
        mod = int((stat - 10) / 2)
    elif stat < 10:
        mod = int((abs(7-11)/2)*-1)
    return mod




def setup():
    heading = '====================================='
    """
    print(heading)
    print('===========Start Character===========')
    print(heading)
    print('')
    char_name = str(input('>> First things first, Character Name: '))
    """
    print('>> Duuuuuude. Sick name, duuude.')

    char_race = race()
    char_class = c_class()

    print('>> Braaaaaah. Wiiiickeeeeed.')
    char_height = str(input('>> Hi how high are you bro (height get it bro haha): '))
    char_eyes = str(input('>> What\'s your eye color duude: '))
    print('Hahahha pretty sick, duuuuude.')
    print(heading)
    print('\n')
    print(heading)

    ### Now the Stats

    print('=== Now the totally rad part, brah ===')
    print('=============== STATS ===============')

    STR = stat_check('>> Put your strength stat, brah: ')
    STR_mod = stat_mod(STR)
    print('>> Radical, man. Your strenght mod is', STR_mod, 'btdubs.')

    DEX = stat_check('>> Dex Time dude: ')
    DEX_mod = stat_mod(DEX)
    print('>> Sweeeeet.', str(DEX_mod),'ain\'t bad, bro')

    CON = stat_check('>> Con (it\'s important too) :')
    CON_mod = stat_mod(CON)
    print('>> Broooo. You\'re tough as balls, broo.')

    WIS = stat_check('>> Wissy wissard hahaha: ')
    WIS_mod = stat_mod(WIS)

    INT = stat_check('>> Int is for nerds: ')
    INT_mod = stat_mod(INT)

    CHA = stat_check('>> Cha-Ching Charismo bro: ')
    CHA_mod = stat_mod(CHA)
    print('Time to pick up the babes am I right brah hahaha.')
    print('Or bros, man, what ever you is brah haha.')


    char_attributes = {'fsrace':char_race,'class':char_class}
    char_deets = {'height':char_height,'eyes':char_eyes}
    char_stats = {'str':STR,'dex':DEX,'con':CON,'wis':WIS,'int':INT,'cha':CHA, 'str_m':STR_mod,'dex_m':DEX_mod,'con_m':CON_mod, 'wis_m':WIS_mod,'int':INT_mod,'cha':CHA_mod}
    return char_attributes,char_deets, char_stats
