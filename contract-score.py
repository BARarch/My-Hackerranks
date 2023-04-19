from typing import List, Set, Tuple
from functools import reduce
from operator import mul
from pandas import *

def max_score_dp(scores, viable):

    STATE_OFFSET = 1
    N_STATES = 10                   ## Fix This
    viable = viable[:N_STATES]

    VisitedStates = set()
    VisitedScoresStates = {}

    def show_matrix(matrix, positionScores):
        df = DataFrame(matrix)
        df.index = [f'{row}: {score}' for row, score in enumerate(positionScores)]
        print(df)

    ## V Constants for Data Image
    V = {   'statesOfPos': [set(),],
            'I': [[]],
            'allScores': scores,
            'scores': [],
            'matchableStates': set(),
            'unMatchableStates': set(),
            'maximumScore': 0
             }

    def show_I():
        show_matrix(V['I'], V['scores'])
    V['show'] = show_I

    def set_display():
        V['I'] = [[0,] * N_STATES for pos in V['statesOfPos']]
        for pos, states in enumerate(V['statesOfPos']):
            for state in states:
                V['I'][pos][state] = 1 if state in V['matchableStates'] else -1
        show_I()
    
    def set_states_of_pos(viable):
        V['statesOfPos'] = []
        for pos in viable:
            stateSet = set()
            for state in pos:
                stateSet.add(state - STATE_OFFSET)
            V['statesOfPos'].append(stateSet)
        #[print(stateSet) for stateSet in V['statesOfPos']]

    def compute_matchable_states():
        for stateSet in V['statesOfPos']:
            V['matchableStates'] = V['matchableStates'].union(stateSet)
        V['unMatchableStates'] = set(range(N_STATES)).difference(V['matchableStates'])

    def compute_scores(scores):
        ## A state can only match with one postion
        ## If there are fewer matchable states than positions
        ## Some postions will go unmatched
        ## We only keep the top N scores for the N matchable positions
        V['scores'] = scores[:len(V['matchableStates'])]
        V['maximumScore'] = sum(V['scores'])
        print(f"matchable states { len(V['matchableStates']) }: {  V['matchableStates']  }")
        V['scores'] += [0] * len(V['unMatchableStates'])
        #print(V['scores'])
        #print(V['maximumScore'])

    def set_lowest_positions():
        revPos = 1
        for pos in V['unMatchableStates']:
            ## Mutate Positions stateSet matrix
            V['statesOfPos'][-revPos] = {pos}          # Each Lower position has a single unmatchable state as a viable state
            revPos += 1

    

    def set_viable_states(viable, scores):
        set_states_of_pos(viable)
        #set_display()
        compute_matchable_states()
        compute_scores(scores)
        set_lowest_positions()
        set_display()
    V['set_viable'] = set_viable_states
            

    ## U State Dictionary
    U = {   'stateOf': ['',] * N_STATES,
            'display': [['',],],
            'posOf': ["",] * N_STATES,
            'unMatched': [],
            'totalScore': 0,
            'nSwaps': 0}

    ## Main State Variable for Swaps
    def u_stateOf(pos):
        return U['stateOf'][pos]
    U['state_of'] = u_stateOf
    
    def print_state():
        [print(state) for state in U['stateOf']]
    
  
    ## Initialize the used state matrix u
    def compute_U():
        U['display'] = [(['',] * state) + ['u',] + (['',] * (N_STATES - state - 1)) for state in U['stateOf']]
    
    def show_U():
        show_matrix(U['display'], V['scores'])
    U['show'] = show_U
    
    ## U position of state 
    def compute_U_posOf():
        for pos, state in enumerate(U['stateOf']):
            U['posOf'][state] = pos
    def u_posOf(state):
        return U['posOf'][state]
    U['pos_of'] = u_posOf

    ## Additional Interface Functions
    def compute_total_score():
        U['totalScore'] = 0
        for score, usedState, viablestates in zip(scores, U['stateOf'], V['I']):
            U['totalScore'] += score * viablestates[usedState]
        
    def compute_unmatched_positions():
        U['unMatched'] = []
        for pos, uState in enumerate(U['stateOf']):
            if uState not in V['statesOfPos'][pos]:
                U['unMatched'].append(pos)

    def set_state(newUsedState):
        U['stateOf'] = newUsedState
        U['nSwaps'] += 1
        compute_U()
        compute_U_posOf()
        compute_unmatched_positions()
        compute_total_score()
        VisitedStates.add(newUsedState)
        VisitedScoresStates[U['totalScore']] = newUsedState        
    U['set_state'] = set_state

    ## Swap Utility Functions
    def cost(pos, state):
        ## p3(3) wanna be p3(4) huh...
        ## what position holds state 4
        ## uof(4) is p10 so p10(4)
        ## what is the cost of p10 going to p10(3)
        ## look at the table
        initalVal = scores[pos] if pos not in U['unMatched'] else 0
        finalVal = V['I'][pos][state] * scores[pos]
        return initalVal - finalVal
    
    def get_swapState(pos, state):
        # what will the state vector look like?
        otherPos = U['pos_of'](state)
        posCurrentState = U['state_of'](pos)
        resultingState = list(U['stateOf'])
        resultingState[otherPos] = posCurrentState
        resultingState[pos] = state
        return tuple(resultingState), cost(otherPos, state)
    
    def ressultOf_swap(pos, state):  
        return state, *get_swapState(pos, state)
    
    def get_viable_moves(pos, without=None):
        if without:
            return list(filter(lambda result: result[1] not in VisitedStates, map(lambda state: ressultOf_swap(pos, state), filter(lambda state: state != without, V['statesOfPos'][pos]))))
        return list(filter(lambda result: result[1] not in VisitedStates, map(lambda state: ressultOf_swap(pos, state), V['statesOfPos'][pos])))
    
    ## Main Function
    def wannabe(pos, state, n):
        ## conduct swap here
        print(f'{pos} gonnabe {state} at step {n} ')
        U['set_state'](get_swapState(pos, state)[0])
    
        print(f"unmatched positions: {U['unMatched']} score: {U['totalScore']}")
        if U['unMatched']:
            pos = U['unMatched'][0]

            ## compute viable swaps SET
            viable_moves = get_viable_moves(pos)
            while U['unMatched'] and viable_moves:
                viable_moves.sort(key=lambda move: move[2])
                print(f'cheapest move at position {pos}: {viable_moves[0]}')  
                state = viable_moves[0][0]
                total, state = wannabe(pos, state, n + 1)
                ## compute remaining viable swaps SET
                viable_moves = get_viable_moves(pos, without=state)

        res = max(VisitedScoresStates)
        return res, VisitedScoresStates[res]
    
    
    ## Start Computation
    V['set_viable'](viable, scores)             #  Initialize Case
    U['set_state'](tuple(range(N_STATES)))      #  Initialize State

    [print(f'{pos}: {states}') for pos, states in enumerate(V["statesOfPos"]) ]
    print(V['scores'])
    print(V['allScores'])
    print(V['matchableStates'])
    print(V['unMatchableStates'])

    n = 0
    
    if U['unMatched']:
        pos = U['unMatched'][0]
        print(f'Starting Position to swap: {pos}')
        viable_moves = get_viable_moves(pos)
        #print(f'viable moves at position {pos} {viable_moves}')
        viable_moves.sort(key=lambda move: move[2])
        print(f'cheapest move at position {pos}: {viable_moves[0]}')

        ## Call Recursove Helper Here
        res, finalState = wannabe(pos, viable_moves[0][0], 0)      # Conduct Swap


    print('\nfinalScore')
    print(f'{res} states: {finalState}')
    U['show']()
    
    print(f'nSwaps: {U["nSwaps"]}')
    print(f'maxPosible {V["maximumScore"]}')

    return res, finalState

if __name__ == "__main__":
    ## CASE 0
    print()
    print("Case 0")
    scores0 = [500, 
               450, 
               350, 
               350, 
               300, 
               250, 
               200, 
               150, 
               100, 
               50, 
               50]
    
    viableContracts0 = [[1,4,6,8,9,10], #8
                        [1,2,3,5,7,10], #4 
                        [1,4,6,9,10],   #0
                        [1,4,10],       #9
                        [4,7],          #6
                        [4,6,10],       #5
                        [1,2,3,4,6,10], #1
                        [4],            #3
                        [4,8],          #7
                        [1,2,3,5,7,10], #2 All MATCHED !!!
                        [4,7]]          #

    max_score_dp(scores0, viableContracts0)

    ## CASE 1
    print()
    print("Case 0")
    scores1 = [490, 
               490, 
               360, 
               360, 
               360, 
               250, 
               250, 
               250, 
               250, 
               250]
    
    viableContracts1 = [[4,5,10],   #8
                        [1,2,3,4],  #4 
                        [1,4,5,9],  #0
                        [2,3,4,9],  #9
                        [4,10],      #6    
                        [1,4,10],   #1
                        [1,2,3,4],  #3
                        [1,2,3,4],  #7
                        [4],        #2 All MATCHED !!!
                        [1,4]]      #

    max_score_dp(scores1, viableContracts1)






