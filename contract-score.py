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
    I = [[0,] * N_STATES for _ in viable]
    ## Declare the Viable State Matrix I. 
    ## This will not change
    for pos, states in enumerate(viable):
        for col in states:
            I[pos][col - 1] = 1

    uPosOf = list(range(N_STATES))
    ## Initialize the used state matrix u
    u = [['',] * N_STATES for _ in viable]
    for col, pos in enumerate(uPosOf):
        u[pos][col] = 'u'

    def unmatched_positions():
        stateHistory = [''.join([reduce(mul, col) for col in pos]) for pos in [tuple(zip(*row)) for row in zip(u, I)]]
        return {matched[0] for matched in filter(lambda hist: "u" in hist[1], enumerate(stateHistory))}


    #print([''.join([reduce(mul, state) for state in pos]) for pos in [tuple(zip(*row)) for row in zip(u, I)]])
    print(unmatched_positions())

   # set(pos for pos in [tuple(zip(*row)) for row in zip(u, I)]

    # Check Initializations
    #[print(tuple(zip(*row))) for row in zip(u, I)]  # How to combine
    #[print(row) for row in u]

    def cost(pos, state):
        ## p3(3) wanna be p3(4) huh...
        ## what position holds state 4
        ## uof(4) is p10 so p10(4)
        ## what is the cost of p10 going to p10(3)
        ## look at the table
        initalVal = scores[pos] if pos not in unmatched_positions() else 0
        finalVal = I[pos][state] * scores[pos]
        return initalVal - finalVal



    
    def wannabe(pos, state):
        ## I am p3(3) I wanna be p3(4)
        ## what is the postion that holds state 4
        ## U postion of 4 (uof(4)) is position 10 (or p(10))

        ## ok
        ## if you swap with p10 
        ## the cost will be whatever it costs for p10(4) to goto p10(3)

        ## Do the u->i->u->i
        ## where u is the marker of the state a postion is in on the state matrix
        ## U[pos, col] = 'u' if position pos is in state col.
        ## and where i is a marker for previous states for a position
        pass




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
    
    viableContracts0 = [{1,4,6,8,9,10},
                        {1,2,3,5,7,10},
                        {1,4,6,9,10},
                        {1,4,10},
                        {4,7},
                        {4,6,10},
                        {1,2,3,4,6,10},
                        {4},
                        {4,8},
                        {1,2,3,5,7,10},
                        {4,7}]
    
    viable0 = tuple(range(1,12))


    max_score_dp(scores0, viableContracts0)
    #print(max_score(viable0, 11, scores0, viableContracts0))







