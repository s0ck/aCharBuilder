#
#   This loads the data from the D&D class into the class class. Yeah
#
#       Woohoo indents
#
#   Yo dog. Keep it real.
#
#   Added 'Size' dictionaries for M or S.
#   Resistances works like:
#       Key: What you have resistance against
#       Data: Either True of False.
#
#   Not sure how to put 'Dwarves have Advantage against Poison.'
#   Add saving throws later
#

foo = 'bar'

Dwarf       = {'abil_increase':{'CON':2},
               'speed':25,
               'vision':{'dim':60,'dark':'bw'}, #bw means black and white only
               'special':[foo],
               'profs':{
               'weps':{'battleaxe':True,'handaxe':True,'throwing hammer':True, 'warhammer':True},
               'tools':{'smith':False,'brewer':False,'mason':False}, # How do I put the 'or' in here.
               'stone': 'You are proficient with History if you\'re checking the origin of a cut stone.'},
               'res':{'poison': True}, #Resistances from types of damage
               'langs':['Common', 'Dwarvish'],
               'sub_race':[foo]
               }

High_Elf    = {'abil_increase':{'INT':1}}

Wood_Elf    = {'foo':foo}

Drow        = {'foo':foo}

Elf         = {'abil_increase':[foo],
               'speed':25,
               'vision':[foo],
               'special':{'Trance':'Ye'},
               'profs':['Perception'],
               'langs':[foo],
               'sub_race':[High_Elf,Wood_Elf,Drow,]
               }

Halfling    = {'abil_increase':[foo],
               'speed':25,
               'vision':[foo],
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Human       = {'abil_increase':[foo],
               'speed':25,
               'vision':[foo],
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Dragonborn  = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Gnome       = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Half_Elf    = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Half_Orc    = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }

Teifling    = {'abil_increase':[foo],
               'speed':25,
               'vision':{'foo':foo},
               'special':[foo],
               'profs':[foo],
               'langs':[foo],
               'sub_race':[foo]
               }



#-------------------------------------------------------------------------------------#



q, t = 1, 2
lvl_1 = 'le'
higher = 'er'
armour = 'thing'
weapons = ' I eat memory ' #these are here just to not throw errors.
tools = 23432              # I'll put the rest of the pirated stats in later.
skills = 'money'           # 'Cool beans, dog' -- dubPirate
Barbarian = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Bard      = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Cleric    = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Druid     = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Fighter   = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Monk      = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Paladin   = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Ranger    = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Rouge     = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Sorcerer  = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Warlock   = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

Wizard    = {'prof_bonus':[],
             'features':[],
             'cantrips':[],
             'spell_slots':[],
             'hit_di':[q,t], #q is for quantity; t is for type
             'hit_points':[lvl_1,higher],
             'profs':[armour,weapons,tools,skills]
             }

"""
    The Races dict keys:
            dw = Dwarf
            el = Elf
            hl = Halfling
            he = Half-Elf
            ho = Half-Orc
            db = Dragonborn
            hu = Human
            tl = Teifling
"""

the_races = {'dw':Dwarf,'el':Elf,'hl':Halfling,'he':Half_Elf,'ho':Half_Orc,'db':Dragonborn, 'hu':Human, 'tl':Teifling}
the_classes = {}

#-------------------------------------------------------------------------------------#

"""The Following is redundat"""
#class Race:
#    """Love peebs""" #What are peebs?
#    '''I'm going to use this to load classes into a class and then load that into the character class.'''
#    def __init__(self, race):
#        self.
