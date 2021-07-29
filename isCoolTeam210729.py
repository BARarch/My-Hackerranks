#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer
import functools

class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        def printH(H):
            print('    ' + '  '.join(H.keys()))
            for row in H:
                print(f'{row}: {list(H[row].values())} ')

        def eulerian(names):
            # constuct adjacency matrix for all letters in the begining or end of names
            letters = functools.reduce(lambda a, b: a.union(b), zip(map(lambda x: x[0].lower(), names), map(lambda y: y[-1].lower(), names)), set())
            H = {letter:{letter: 0 for letter in letters} for letter in letters}

            for fore, aft in map(lambda name: (name[0].lower(), name[-1].lower()), names):
                H[fore][aft] += 1

            #printH(H)
            ## Compute the diffenence between the words that go into the letter from the words that go out from a letter
            ## With the nodes as the letters at both ends of the words, the words are directed edges in the graph
            outs = {letter: sum(H[letter].values()) for letter in letters}
            ins  = {letter: sum([H[x][letter] for x in letters]) for letter in letters}
            nets = {letter: ins[letter] - outs[letter] for letter in letters}

            #print(nets)

            ## Compute euler score.  each node with the exepetion of the nodes where the transversal starts or stops should be zero.  There
            ## Should be exactly 1 start node with a score of -1 and exactly one stop node with a score of 1 or neither a start or stop node 
            ## in the case of a cycle.
            ## if these rules are true for a graph, there exists a sequence of nodes traversed were each edge is used exactly once.
            ## if each edge is used once this is a cool team! 
            euler = {}
            for letter in letters:
                if -1 > nets[letter] or nets[letter] > 1:
                    return False
                if nets[letter] == -1:
                    if 'start' in euler:
                        return False
                    else:
                        euler['start'] = letter
                if nets[letter] == 1:
                    if 'stop' in euler:
                        return False
                    else:
                        euler['stop'] = letter

            print(f'euler: {euler}')
            if ('start' in euler and 'stop' in euler) or not bool(euler):
                ## Last Step:
                ## Walk the graph once and make sure that you get all nodes
                ## if the team is cool the graph formed from the names should produce
                ## a signle connected region
                visted = set()
                lettersToWalk = [names[0][0].lower(),] if not bool(euler) else [euler['start'],]
                while lettersToWalk:
                    currentLetter = lettersToWalk.pop()
                    if currentLetter not in visted:
                        visted.add(currentLetter)
                        lettersToWalk += list(filter(lambda x: H[currentLetter][x] != 0, H[currentLetter]))

                return visted == letters
            else:
                return False

        return eulerian(self.names)


# Complete the function below.
@qtimer.timeit
def isCoolTeam(team):
    return bool(Team(team))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = isCoolTeam(team) 
    if isinstance(result, int) or isinstance(result, str):
        fptr.write(str(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        fptr.write(str(result))
    else:
        fptr.write(' '.join(map(str, iter(result))))
        
    fptr.write('\n')

    fptr.close()