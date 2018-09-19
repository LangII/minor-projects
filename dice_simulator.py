#########
###
#
#    DICE ROLL SIMULATOR
#    by David Lang
#    on 2017-10-11
#
###
#########

import random, time

proceed = ['Yes', 'yes', 'YES', 'Yup', 'yup', 'YUP', 'Yeah', 'yeah', 'YEAH', 'Sure', 'sure', 'SURE']
exit = ['No', 'no', 'NO', 'Nope', 'nope', 'NOPE']

# 17-32 = dice roll function with interactive Q&A for input of player specifications
def dice_roll():
    try:
        dice_quantity = int(input("\nHow many dice would you like to roll?\n"))
    except ValueError:
        print("Numbers only, please. Let's try again.")
        dice_roll()
    try:
        dice_face = int(input("How many sides would you like the dice to have?\n"))
    except ValueError:
        print("Numbers only, please. Let's try again.")
        dice_roll()
    print("\nRolling dice...\nResults are...\n")
# 31-33 = dice results output generator
    for x in range(dice_quantity):
        print('dice#',repr(x+1),'= [',random.randint(1, dice_face),']')
    repeat()

# 35-57 = interactive Q&A
def interact():
    initiate = input("Would you like to roll some dice?\n")
    if initiate in proceed:
        dice_roll()
    elif initiate in exit:
        print('\nOk. Goodbye.')
        time.sleep(2)
        quit()
    else:
        print("I don't understand.  Let's try again.")
        interact()

def repeat():
    again = input("\nWould you like to roll the dice again?\n")
    if again in proceed:
        dice_roll()
    elif again in exit:
        print('\nOk. Goodbye.')
        time.sleep(2)
        quit()
    else:
        print("I don't understand.  Let's try again.")
        repeat()

# 60 = introduction
print('<><><><><><><> <><><><><><><>\n<><> DICE ROLL SIMULATOR <><>\n<><><><><><><> <><><><><><><>\n\nHello.\n')

interact()