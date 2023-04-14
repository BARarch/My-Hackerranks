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

    N_STATES = 10
    viable = viable[:N_STATES]
       
    ## Declare the Viable State Matrix I.
    I = [[0,] * N_STATES for _ in viable] 
    ## This will not change
    for pos, states in enumerate(viable):
        for col in states:
            I[pos][col - 1] = 1
    def print_I():
        [print(row) for row in I]

    ## Main State Variable for Swaps
    uStateOf = tuple(range(N_STATES))
    def u_stateOf(pos):
        return uStateOf[pos]
    def print_state():
        [print(state) for state in uStateOf]
  
    ## Initialize the used state matrix u
    def compute_U(usedStates):
        return [(['',] * state) + ['u',] + (['',] * (N_STATES - state - 1)) for state in usedStates]
    def print_u():
        [print(row) for row in u]
    u = compute_U(uStateOf)

    ## U position of state 
    uPosOf = ['',] * N_STATES 
    def compute_U_posOf(usedStates):
        for pos, state in enumerate(usedStates):
            uPosOf[state] = pos
    def u_posOf(state):
        return uPosOf[state]
    compute_U_posOf(uStateOf)

    ## Utility Functions
    def total_calc(usedStates, scores, I):
        res = 0
        for score, usedState, viablestates in zip(scores, usedStates, I):
            res += score * viablestates[usedState]
        return res
    
    def unmatched_positions():
        stateHistory = [''.join([reduce(mul, col) for col in pos]) for pos in [tuple(zip(*row)) for row in zip(u, I)]]
        return [matched[0] for matched in filter(lambda hist: "u" not in hist[1], enumerate(stateHistory))]

    def cost(pos, state):
        ## p3(3) wanna be p3(4) huh...
        ## what position holds state 4
        ## uof(4) is p10 so p10(4)
        ## what is the cost of p10 going to p10(3)
        ## look at the table
        initalVal = scores[pos] if pos not in unmatched_positions() else 0
        finalVal = I[pos][state] * scores[pos]
        return initalVal - finalVal
    

    
    def get_swapState(pos, state):
        # what will the stat vector look like?
        otherPos = u_posOf(state)
        posCurrentState = u_stateOf(pos)
        resultingState = list(uStateOf)
        resultingState[otherPos] = posCurrentState
        resultingState[pos] = state
        return tuple(resultingState), cost(otherPos, state)
    
    def ressultOf_swap(pos, state):  
        return state, *get_swapState(pos, state)
    
    def get_viable_moves(position, without=None):
        if without:
            return list(filter(lambda result: result[1] not in VistedStates, map(lambda state: ressultOf_swap(pos, state - 1), filter(lambda state: state != without, viable[pos]))))

        return list(filter(lambda result: result[1] not in VistedStates, map(lambda state: ressultOf_swap(pos, state - 1), viable[pos])))
    
    ## Main Function
    def wannabe(pos, state, n):
        ## conduct swap here
        uStateOf = get_swapState(pos, state)[0]
        u = compute_U(uStateOf) 
        compute_U_posOf(uStateOf)

        VistedStates.add(uStateOf)
        VistedScoresStates[total_calc(uStateOf, scores, I)] = uStateOf

        unMatched = unmatched_positions()

        if unMatched:
            pos = unMatched[0]

            ## compute viable swaps SET
            viable_moves = get_viable_moves(pos)
            print(f'viable moves at position {pos} {viable_moves}')
            while unmatched_positions() and viable_moves:
                viable_moves.sort(key=lambda move: move[2])
                print(f'cheapest one: {viable_moves[0]}')  
                state = viable_moves[0][0]
                total, state = wannabe(pos, state, n + 1)
                ## compute remaining viable swaps SET
                viable_moves = get_viable_moves(pos, without=state)

        res = max(VistedScoresStates)
        return res, VistedScoresStates[res]
    
    VistedStates = {uStateOf}
    VistedScoresStates = {total_calc(uStateOf, scores, I):uStateOf}

    print_state()
    print_u()
    print_I()
    print(uPosOf)
    print(unmatched_positions())
    print(cost(0,9))
    print(ressultOf_swap(3, 4))
    print(VistedStates)
    print(VistedScoresStates)

    unMatched = unmatched_positions()
    n = 0
    
    if unMatched:
        pos = unMatched[0]
        print(f'Starting Position to swap: {pos}')
        viable_moves = get_viable_moves(pos)
        print(f'viable moves at position {pos} {viable_moves}')
        viable_moves.sort(key=lambda move: move[2])
        print(f'cheapest one: {viable_moves[0]}')
        res, finalState = wannabe(pos, viable_moves[0][0], 0)      # Conduct Swap

    print(res)
    print(finalState)

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
    
    viableContracts0 = [[1,4,6,8,9,10],
                        [1,2,3,5,7,10],
                        [1,4,6,9,10],
                        [1,4,10],
                        [4,7],
                        [4,6,10],
                        [1,2,3,4,6,10],
                        [4],
                        [4,8],
                        [1,2,3,5,7,10],
                        [4,7]]
    
    viable0 = tuple(range(1,12))


    max_score_dp(scores0, viableContracts0)
    #print(max_score(viable0, 11, scores0, viableContracts0))







