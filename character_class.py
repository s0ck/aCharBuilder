from char_setup_checks import *
from race_class_loader import *
from items import *
import pickle
#
#   1: Make class  // Tick-ish
#   2: Make the class take the info from setup // Tick
#   3: Take info from race_class document and put it into the Character //
#   4: pickle info into somewhere.
#
#   Because class gets confused with class I made everything caps.
#
#   'Don't even trip, dog'-- Rick Sanchez
#
#

class Character(object):

    """
        Taking the information from setup and saving it
        I guess it's just important to remember caps.

        the load parameter on __init__ is either True
        or False depending if the character has already
        been setup.
    """

    def __init__(self, name, load):
        if load == False:
            self.new_setup(name)

        elif load == True:
            self.load_setup(name)

        self.name = name
        self.str = self.sts['str']
        self.dex = self.sts['dex']
        self.con = self.sts['con']
        self.int = self.sts['int']
        self.wis = self.sts['wis']
        self.cha = self.sts['cha']
        self.skill_setup()
        self.menu()


    def load_setup(self, name):
        payload = pickle.load(open(str(name)+'_save.p', "rb"))
        self.attributes = payload[0]
        self.level = payload[1]
        self.sts = payload[2]
        self.RACE = payload[3]
        self.CLASS = payload[4]


    def new_setup(self, name):
        races = pickle.load(open('races.p', 'rb'))
        classes = pickle.load(open('classes.p', 'rb'))
        self.attributes, self.level, self.sts = setup()
        self.RACE = races[self.attributes['race']]
        self.CLASS = classes[self.attributes['class']]

        #pickle.dump(self, char_saves.py,*,fix_imports=True)

    def menu(self):
        self.options = "--- Options: ---\n>> stats / race <<\n>> help / quit <<\n>> attack / save <<"
        print(self.options)
        '''
        for item in dir(Character):
            if item[0:1] != '__':
                print(item)
        '''

        while True:
            key = str(input('>> '))
            if key == 'quit':
                break

            else:
                print(key)
            """
            if key in opts_dict:
                opts_dict[key]
            """

    def skill_setup(self):
        self.dex_skills = [self.stat_mod(self.dex),{'Acrobatics':False, 'Slight of Hand':False, 'Stealth':False}]
        self.int_skills = [self.stat_mod(self.int),{'Perception':False, 'Arcana':False, 'History':False, 'Investigation':False, 'Nature':False, 'Religion':False}]
        self.wis_skills = [self.stat_mod(self.wis),{'Insight':False, 'Animal Handling':False, 'Medicine':False, 'Perception':False, 'Survival':False}]
        self.cha_skills = [self.stat_mod(self.cha),{'Deception':False, 'Intimidation':False, 'Performance':False, 'Persuasion':False}]
        self.skills = [self.dex_skills, self.int_skills, self.wis_skills, self.cha_skills]

    def skill_check(self):
        print('>> Which skill ya need bruh.')
        skill = str(input('>> '))
        mod = 0
        for lst in self.skills:
            if skill in lst[1]:
                mod += lst[0]
            if skill == True:
                mod += self.CLASS['prof boni'][self.level]

    def my_items(self):
        """This is a place holder at the moment until I get
        Actuall items up in theis beithc"""
        items = self.str

    def my_race(self):
        race_print = str(input('>> What you need, bro: '))
        try:
            print('>> Ok, bro, your',race_print,'be',self.RACE[race_print])

        except KeyError:
            print('Wh- what.')

    def my_stats(self):
        stat_print = str(input('>> What stat you need, bro?\n>> [str - con - dex - wis - int - cha]\n>> '))
        try:
            print('-- Your',stat_print,'is', self.sts[stat_print],'--')
            mod_print = str(stat_print)+'_m'
            print('-- And your',stat_print,'modifier is',self.stat_mod(stat_print),'--')

        except KeyError:
            print('>> Uh, what.')
            print('>> You can type str, con, dex, wis, int, or cha.')
            print(">> Or you can type 'quit' to quit, dog.")


    def attack(self):
        wep = str(input('>> What are you attacken with, bruh: '))

    def stat_mod(self, stat):
        if stat >= 10:
            mod = int((stat - 10) / 2)

        elif stat < 10:
            mod = int((abs(7-11)/2)*-1)

        return mod

    def save(self):
        payload = [self.attributes, self.level, self.sts, self.RACE, self.CLASS]
        pickle.dump(payload, open(str(self.name)+'_save.p', "wb"))
        print('>> radical brah,', self.name, 'got saved 8)')
