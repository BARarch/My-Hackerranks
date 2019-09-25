#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190925

def almostIncreasingSequence(sequence):
    prev = sequence[0]
    dec = None
    
    # Seq 1
    i = 1
    if len(sequence) > 1:
        while i < len(sequence) and sequence[i] > sequence[i - 1]:
            i += 1
            
        if i == len(sequence):
            return True
        
        j = i + 1
        while j < len(sequence) and sequence[j] > sequence[j - 1]:
            j += i
            
        if j != len(sequence):
            return False
        
        if sequence[i] <= sequence[i - 2] and sequence[i - 1] <= sequence[i + 1]:
            return False
        
    return True
