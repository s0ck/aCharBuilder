#
#   This loads the data from the D&D class into the class class. Yeah
#
#       Woohoo indents
#
#   Yo dog. Keep it real.
#
'''
Dwarf       = {'abil_increase':{'DEX':2},
               'speed':25,
               'vision':{'dim':60,'dark':'bw'}, #bw means black and white only
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }

High_Elf    = {'abil_increase':{'INT':1}}

Wood_Elf    = {}

Drow        = {}

Elf         = {'abil_increase':[],
               'speed':25,
               'vision':[],
               'special':{'Trance':'Ye'},
               'profs':['Perception'],
               'langs':[],
               'sub_race':[High_Elf,Wood_Elf,Drow,]
               }

Halfling    = {'abil_increase':[],
               'speed':25,
               'vision':[],
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }

Human       = {'abil_increase':[],
               'speed':25,
               'vision':[],
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }

Dragonborn  = {'abil_increase':[],
               'speed':25,
               'vision':{},
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }
'''
Gnome       = {'abil_increase':[],
               'speed':25,
               'vision':{},
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }
'''
Half-Elf    = {'abil_increase':[],
               'speed':25,
               'vision':{},
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }

Half-Orc    = {'abil_increase':[],
               'speed':25,
               'vision':{},
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }
'''
Teifling    = {'abil_increase':[],
               'speed':25,
               'vision':{},
               'special':[],
               'profs':[],
               'langs':[],
               'sub_race':[]
               }


#-------------------------------------------------------------------------------------#
q, t = 1, 2
lvl_1 = 'le'
higher = 'er'
armour = 'thing'
weapons = ' I eat memory ' #these are here just to not throw errors. 
tools = 23432              # I'll put the rest of the pirated stats in later.
skills = 'money'
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

#-------------------------------------------------------------------------------------#


class Race:
    """Love peebs"""
    def __init__(self, name):
        print('Yo, world.')
        print(name)
        print('Hubba Hubba!')
        self.name = name


