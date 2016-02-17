import char_setup_checks
import char_classes
from char_setup_checks import *
from char_classes import *

def start_up():
    heading = '====================================='
    print(heading)
    print('===========Start Character===========')
    print(heading)
    print('')
    char_name = str(input('>> First things first, Character Name: '))
    print('>> Duuuuuude. Sick name, duuude.')

    char_race = race()

    char_class = c_class()

    print('>> Braaaaaah. Wiiiickeeeeed.')
    print(heading, '\n', heading)

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

    char_attributes = [char_name,char_race,char_class]
    char_stats = [[STR,DEX,CON,WIS,INT,CHA], [STR_mod,DEX_mod,CON_mod,WIS_mod,INT_mod,CHA_mod]]
    return char_attributes, char_stats
