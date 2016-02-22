from char_setup_checks import *
#
#   1: Make class
#   2: Make the class take the info from setup
#   3: Take info from race_class document and put it into the Character
#   4: pickle info into somewhere.
#
#   Does anyone know how to use pickle?
#
#   Because class gets confused with class I made everything caps.
#
#   'Don't even trip, dog'-- Rick Sanchez
#
#

class Character(object):
    """Taking the information from setup and saving it."""
    """ I guess it's just important to remember caps.  """

    def __init__(self, name):
        self.attributes, self.deets, stats = setup()
        self.stats = stats
        self.NAME = name
        self.STR = stats['str']
        self.DEX = stats['dex']
        self.CON = stats['con']
        self.INT = stats['int']
        self.WIS = stats['wis']
        self.CHA = stats['cha']
        self.my_stats()

    def my_stats(self):
        James = True
        while James == True:
            try:
                stat_print = str(input('What stat you need, bro?'))
                if stat_print == 'quit':
                    James = False
                    break
                print('>> Your',stat_print, 'is', self.stats[stat_print])
            except KeyError:
                print('>> Uh, what.')
                print(">> Type 'quit' to quit. Or type a stat to print it, dog.")
