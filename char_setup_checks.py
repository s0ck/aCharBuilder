def race(): #Check's if the user has chosen an actual race.
    races = ['Elf', 'Human', 'Half-Elf', 'Half elf', 'Half Elf', 'Half Orc','Dwarf', 'Halfling', 'Dragonborn', 'Teifling']
    no_races = len(races)
    while True:
        char_race = str(input('>> Choose a race, dude: '))
        for num in range(0,no_races):
            if char_race == races[num]:
                print('>> Duuuuude, I love', char_race+'s, brah.')
                return char_race
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
    if stat > 10:
        mod = int((stat - 10) / 2)
    elif stat < 10:
        mod = int((abs(7-11)/2)*-1)

    return mod
