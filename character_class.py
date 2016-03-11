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
    """Taking the information from setup and saving it
       I guess it's just important to remember caps.

       the load parameter on __init__ is either True
       or False depending if the character has already
       been setup."""
    def __init__(self, name, load):
        self.NAME = name
        if load == False:
            self.new_setup(name)
        elif load == True:
            self.load_setup(name)
        """self.opts_dict = {
        'stats':self.my_stats(),'race':self.my_race(),
        'help':"you're fucked",'quit':True,'attack':self.attack(),
        'save':self.save(),'skills':self.skill_check()
        }"""
        self.skill_setup()
        self.menu()


    def load_setup(self, name):
        payload = pickle.load(open(str(name)+'_save.p', "rb"))
        self.attributes = payload[0]
        self.deets = payload[1]
        self.STATS = payload[2]
        self.RACE = payload[3]
        self.CLASS = payload[4]


    def new_setup(self, name):
        races = pickle.load(open('races.p', 'rb'))
        classes = pickle.load(open('classes.p', 'rb'))
        self.attributes, self.deets, self.STATS = setup()
        self.RACE = races[self.attributes['race']]
        self.CLASS = classes[self.attributes['class']]

        #pickle.dump(self, char_saves.py,*,fix_imports=True)

    def skill_setup(self):
        """
            ath = Athletics         prc = Perception
            anh = Animal Handling   arc = Arcana
            acr = Acrobatics        hst = History
            soh = Slight of Hand    inv = Investigation
            stl = Stealth           nat = Nature
            ins = Insight           dec = Deception
            med = Medicine          rel = Religion
            prf = Performance       itm = Intimidation
                        prs = Persuasion
        """
        ath = self.STATS['str']
        acr = self.STATS['dex']
        soh = self.STATS['dex'] #Ahk, Soh düd
        stl = self.STATS['dex']
        anh = self.STATS['wis']
        ins = self.STATS['wis']
        med = self.STATS['wis']
        prc = self.STATS['wis']
        arc = self.STATS['int']
        hst = self.STATS['int']
        inv = self.STATS['int']
        nat = self.STATS['int']
        rel = self.STATS['int']
        dec = self.STATS['cha']
        itm = self.STATS['cha']
        prf = self.STATS['cha']
        prs = self.STATS['cha']
        self.skill_dict = {'Athletics':ath, 'Acrobatics':acr, 'Slight of Hand':soh, #dud, soh
        'Stealth':stl, 'Insight':ins,'Medicine':med,'Perception':prc, 'Arcana':arc,
        'History':hst, 'Investigation':inv, 'Nature':nat, 'Religion':rel, 'Deception': dec,
        'Intimidation':itm, 'Performance':prf, 'Persuasion':prs}

    def my_items(self):
        """This is a place holder at the moment until I get
        Actuall items up in theis beithc"""
        items = self.STATS

    def menu(self):
        self.James = True

        self.options = "--- Options: ---\n>> stats / race <<\n>> help / quit <<\n>> attack / save <<"
        print(self.options)
        while self.James == True:
            key = str(input('>> '))
            if key == 'quit':
                self.James = False
            else:
                self.str(key+ '()')
                print(key)
            """
            if key in opts_dict:
                opts_dict[key]
            """

    def my_race(self):
        race_print = str(input('>> What you need, bro: '))
        try:
            print('>> Ok, bro, your',race_print,'be',self.RACE[race_print])
        except KeyError:
            print('Wh- what.')

    def my_stats(self):
        stat_print = str(input('>> What stat you need, bro?\n>> [str - con - dex - wis - int - cha]\n>> '))
        try:
            print('-- Your',stat_print, 'is', self.STATS[stat_print],'--')
            mod_print = str(stat_print) + '_m'
            print('-- And your',stat_print,'modifier is',self.STATS[mod_print],'--')
        except KeyError:
            print('>> Uh, what.')
            print('>> You can type str, con, dex, wis, int, or cha.')
            print(">> Or you can type 'quit' to quit, dog.")

    def skill_check(self):
        print('>> Which skill ya need bruh.')
        skill = str(input('>> '))
        try:
            print(">> Dude, your",skill,"is +"+self.skill_dict[skill])
        except KeyError:
            print(">> Uh wha.")

    def attack(self):
        wep = str(input('>> What are you attacken with, bruh: '))

    def save(self):
        payload = [self.attributes, self.deets, self.STATS, self.RACE, self.CLASS]
        pickle.dump(payload, open(str(self.NAME)+'_save.p', "wb"))
        print('>> radical brah,', self.NAME, 'got saved 8)')
