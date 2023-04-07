from typing import List, Set, Tuple

def max_score(viable: Set[int], positionsToChoose: int, ViableContactsForRow: List[Set[int]], MS) -> Tuple[int, List[int]]:
    ## Input the 
    #           number of viable contracts and 
    #              the number of positions to choose  - as in n choose k
    #  Then output the
    #                   maximum score and
    #               the resulting ranked contract choices
    return 1, list(viable)


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
    
    viable0 = set(list(range(1,11)))

    print(max_score(viable0, 10, viableContracts0, {}))







