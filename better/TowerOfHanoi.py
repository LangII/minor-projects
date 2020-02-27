


import pandas



DISC_COUNT = 5

LABELS = ['A', 'B', 'C']  # <-- LABELS have to be 3 single letters only.

PILLAR_FORMAT = '|'
DISC_FORMAT = '<%s>'
DISC_BODY = 'o'

MAX_DISC_WIDTH = (DISC_COUNT * 2) + 1
ROWS = [ i + 1 for i in range(DISC_COUNT) ]



####################################################################################################
                                                                                    ###   MAIN   ###
                                                                                    ################

def main():

    step = getStartStep()

    while True:

        prettyPrintStep(step)

        from_choice, to_choice = getChoices()

        if not acceptableChoices(from_choice, to_choice):
            print("\nyour input was not accepted, please try again\n")
            continue

        if not isLegalMove(step, from_choice, to_choice):
            print("\nyou did not input a legal move, please try again\n")
            continue

        step = getNextStep(step, from_choice, to_choice)

        if succeeded(step):  break

    prettyPrintStep(step)
    print("\nWINNER!!!\n")


####################################################################################################
                                                                               ###   FUNCTIONS   ###
                                                                               #####################

def getStartStep():

    step_ = pandas.DataFrame(index=ROWS, columns=LABELS)
    for col in LABELS:
        if col == 'B':  step_[col] = ROWS
        else:           step_[col] = [ 0 for _ in ROWS ]

    return step_



def disc(_int):

    if _int == 0:   disc_ = PILLAR_FORMAT
    else:           disc_ = DISC_FORMAT % (DISC_BODY * ((_int * 2) - 1))

    return disc_



def prettyPrintStep(_step):

    print('\n  ' + ' '.join([ disc(0).center(MAX_DISC_WIDTH, ' ') for _ in LABELS ]) + '')
    for _, row in _step.iterrows():
        print('  ' + ' '.join([ disc(r).center(MAX_DISC_WIDTH, ' ') for r in row.tolist() ]) + '')
    print(' -' + '-'.join([ '-'.center(MAX_DISC_WIDTH, '-') for _ in LABELS ]) + '-')
    print('  ' + ' '.join([ l.center(MAX_DISC_WIDTH, ' ') for l in LABELS ]) + '\n')



def getChoices():

    from_choice_, to_choice_ = '', ''

    from_choice_ =  input('move from: ').upper()
    to_choice_ =    input('move to:   ').upper()

    return from_choice_, to_choice_



def acceptableChoices(_from, _to):

    return False if (_from not in LABELS) or (_to not in LABELS) else True



def getTopDiscRung(_col):

    top_disc_rung_ = 'empty'
    for i, rung in enumerate(_col):
        if rung != 0:
            top_disc_rung_ = i + 1
            break

    return top_disc_rung_



def isLegalMove(_step, _from, _to):

    to_rung = getTopDiscRung(_step[_to].tolist())
    if to_rung == 'empty':  return True

    from_rung = getTopDiscRung(_step[_from].tolist())
    if from_rung == 'empty':  return False

    if _step.at[to_rung, _to] > _step.at[from_rung, _from]:     return True
    else:                                                       return False



def getNextStep(_step, _from, _to):

    from_rung = getTopDiscRung(_step[_from].tolist())

    to_col = _step[_to].tolist()
    to_rung = getTopDiscRung(to_col)
    if to_rung == 'empty':  to_rung = len(to_col)
    else:                   to_rung -= 1

    _step.at[to_rung, _to] = _step.at[from_rung, _from]
    _step.at[from_rung, _from] = 0

    return _step



def succeeded(_step):

    in_col = [ _step[l].tolist() for l in LABELS ]

    if any(in_col[1]):  return False
    if not any(in_col[0]) or not any(in_col[2]):  return True
    return False



############
main()   ###
############
