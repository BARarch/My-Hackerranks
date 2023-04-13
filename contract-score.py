from typing import List, Set, Tuple

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
    for pos, states in enumerate(viable):
        for col in states:
            I[pos][col - 1] = 1

    uPosOf = list(range(N_STATES))
    u = [['',] * N_STATES for _ in viable]
    for col, pos in enumerate(uPosOf):
        u[pos][col] = 'u'

    [print(row) for row in u]

    
    def wannabe(pos, col):
        ## I am p3(3) I wanna be p3(4)
        ## what is the postion that holds column 4
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







