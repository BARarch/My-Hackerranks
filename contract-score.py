from typing import List, Set, Tuple
from functools import reduce
from operator import mul

def max_score(viable: Tuple[int], positionsToChoose: int, scores, viableContracts ) -> Tuple[int, List[int]]:
    ## Input the 
    #           number of viable contracts and 
    #              the number of positions to choose  - as in n choose k
    #  Then output the
    #                   maximum score and
    #               the resulting ranked contract choices
    MS = {}
    S = scores
    VC = viableContracts
    def resultKey(viableSet, k):
        return tuple(viableSet), k

    def max_score_helper(viable, positionsToChoose):
        ## Base Cases
        if positionsToChoose == 0:
            return 0, []
        if resultKey(viable, positionsToChoose) in MS:
            return MS[resultKey(viable, positionsToChoose)]

        ## Recurse for Viable Solutions at this position
        currentRow = len(S) - positionsToChoose
        scoreForRow, contracts = S[currentRow], viableContracts[currentRow]
        
        ## FIRST Try Selectiing Nothing at this Stage
        maxScore, result = max_score_helper(viable, positionsToChoose - 1) 
        result.append('')

        ## THEN Try all posible selections at this position
        for choice in set(viable).intersection(contracts):
            currentScore, currentresult = max_score_helper(tuple(set(viable).difference({choice})), positionsToChoose - 1)
            if currentScore + scoreForRow > maxScore:
                currentresult.append(choice)
                maxScore, result = currentScore + scoreForRow, currentresult
                positonWasFilled = True
        
        return maxScore, result

    maxScore, result = max_score_helper(viable, positionsToChoose)
    return maxScore, list(reversed(result))



def max_score_dp(scores, viable):

    STATE_OFFSET = 1
    N_STATES = 10
    viable = viable[:N_STATES]

    VisitedStates = set()
    VisitedScoresStates = {}

    ## V Constants for Data Image
    V = {   'statesOfPos': [set(),],
            'I': [[]],
            'scores': [],
            'matchableStates': set(),
            'maximumScore': 0
             }

    def set_display():
        V['I'] = [[0,] * N_STATES for pos in V['statesOfPos']]
        for pos, states in enumerate(V['statesOfPos']):
            for state in states:
                V['I'][pos][state] = 1
    
    def set_states_of_pos(viable):
        V['statesOfPos'] = []
        for pos in viable:
            stateSet = set()
            for state in pos:
                stateSet.add(state - STATE_OFFSET)
            V['statesOfPos'].append(stateSet)

    def compute_matchable_states():
        for stateSet in V['statesOfPos']:
            V['matchableStates'].union(stateSet)

    def compute_scores(scores):
        ## A state can only match with one postion
        ## If there are fewer matchable states than positions
        ## Some postions will go unmatched
        ## We only keep the top N scores for the N matchable positions
        V['scores'] = scores[:len(V['matchableStates'])]
        V['maximumScore'] = sum(V['scores'])

    def set_viable_states(viable, scores):
        set_states_of_pos(viable)
        set_display()
        compute_matchable_states()
        compute_scores(scores)
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
    def print_u():
        [print(row) for row in U['display']]
    
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

    print(res)
    print(finalState)
    print(f'nSwaps: {U["nSwaps"]}')

    return res, finalState

   





if __name__ == "__main__":
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
    
    viable0 = tuple(range(1,12))


    max_score_dp(scores0, viableContracts0)
    #print(max_score(viable0, 11, scores0, viableContracts0))







