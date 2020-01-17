
import copy

MAZE = [
#    0  1  2  3  4  5  6  7
    [0, 1, 1, 1, 1, 0, 1, 0], # 0
    [0, 1, 0, 0, 1, 0, 1, 0], # 1
    [1, 1, 1, 0, 1, 1, 1, 1], # 2
    [0, 1, 0, 0, 0, 0, 0, 0], # 3
    [1, 1, 1, 1, 0, 1, 0, 1], # 4
    [1, 0, 0, 1, 1, 1, 1, 1], # 5
]
# MAZE = copy.deepcopy(ORIGINAL_MAZE)

MAX_V, MAX_H = len(MAZE), len(MAZE[0])

START = [0, 6]
END =   [4, 7]

####################################################################################################

def main():

    print(''), printMatrix(insertStartEnd())

    print(''), mainLoop()

def mainLoop():

    prev_pos = []
    current_pos = copy.deepcopy(START)
    path = []

    step = 0
    while True:
        step += 1

        print('\n' + '-' * 80 + '\n')
        printMatrix(insertPositions(prev_pos, current_pos, []))
        print('')

        options = removePrevPosFromOptions(current_pos, prev_pos, getOptions(current_pos))
        print(options)
        print('')

        path = buildPath(path, current_pos, getTotalOptions(options))
        print("path")
        for p in path:  print(p)
        print('')

        dead_end = not bool(getTotalOptions(options))
        if dead_end:
            print("DEAD END ... back tracking ...\n")
            current_pos, prev_pos, path = backTrack(path)
            options = removePrevPosFromOptions(current_pos, prev_pos, getOptions(current_pos))

            print("path")
            for p in path:  print(p)
            print('')
            print("options", options)

        next_pos = getNextPos(current_pos, options)
        printMatrix(insertPositions(prev_pos, current_pos, next_pos))
        print('')

        if next_pos == END:
            print("WINNER", next_pos)
            exit()

        prev_pos = copy.deepcopy(current_pos)
        current_pos = copy.deepcopy(next_pos)

        if step == 30:  exit()

####################################################################################################

def printMatrix(_matrix):
    for row in _matrix:  print('  ' + ' '.join([ '+' if i == 1 else ' ' if i == 0 else i for i in row ]))

def insertStartEnd():
    maze = copy.deepcopy(MAZE)
    maze[START[0]][START[1]] = 'S'
    maze[END[0]][END[1]] = 'E'
    return maze

def insertPositions(_prev_pos, _current_pos, _next_pos):
    maze = copy.deepcopy(MAZE)
    if _prev_pos:  maze[_prev_pos[0]][_prev_pos[1]] = 'P'
    if _current_pos:  maze[_current_pos[0]][_current_pos[1]] = 'C'
    if _next_pos:  maze[_next_pos[0]][_next_pos[1]] = 'N'
    return maze

def getOptions(_cur):
    north, east, south, west = 0, 0, 0, 0
    # north
    if _cur[0] == 0:  north = 0
    else:
        if MAZE[_cur[0] - 1][_cur[1]] == 0:  north = 0
        else:  north = 1
    # south
    if _cur[0] == MAX_V - 1:  south = 0
    else:
        if MAZE[_cur[0] + 1][_cur[1]] == 0:  south = 0
        else:  south = 1
    # east
    print(MAX_V)
    if _cur[1] == MAX_H - 1:  east = 0
    else:
        if MAZE[_cur[0]][_cur[1] + 1] == 0: east = 0
        else:  east = 1
    # west
    if _cur[1] == 0:  west = 0
    else:
        if MAZE[_cur[0]][_cur[1] - 1] == 0: west = 0
        else:  west = 1
    options = {'north': north, 'east': east, 'south': south, 'west': west}
    return options

def removePrevPosFromOptions(_current_pos, _prev_pos, _options):
    if not _prev_pos:  return _options
    if _current_pos[0] - 1 == _prev_pos[0]:    _options['north'] = 0
    elif _current_pos[0] + 1 == _prev_pos[0]:  _options['south'] = 0
    elif _current_pos[1] + 1 == _prev_pos[1]:  _options['east'] = 0
    elif _current_pos[1] - 1 == _prev_pos[1]:  _options['west'] = 0
    return _options

def getNextPos(_current_pos, _options):
    if _options['north']:  next_pos_ = [_current_pos[0] - 1, _current_pos[1]]
    elif _options['east']:  next_pos_ = [_current_pos[0], _current_pos[1] + 1]
    elif _options['south']:  next_pos_ = [_current_pos[0] + 1, _current_pos[1]]
    elif _options['west']:  next_pos_ = [_current_pos[0], _current_pos[1] - 1]
    return next_pos_

def getTotalOptions(_options):
    total_options = 0
    for o in _options.values():  total_options += o
    return total_options

def buildPath(_path, _pos, _total_options):
    _path += [{'pos': _pos, 'forked': True if _total_options >= 2 else False}]
    return _path

def backTrack(_path):
    global MAZE
    path_ = copy.deepcopy(_path)
    for p in reversed(_path):
        if not p['forked']:
            MAZE[p['pos'][0]][p['pos'][1]] = 0
            del path_[_path.index(p)]
        else:
            current_pos_ = p['pos']
            prev_pos_ = path_[path_.index(p) - 1]['pos']
            total_options = getTotalOptions(getOptions(current_pos_))
            print("\n\nHERE >>>", total_options, "\n\n")
            if total_options <= 2:  path_[-1]['forked'] = False
            break
    return current_pos_, prev_pos_, path_

main()
