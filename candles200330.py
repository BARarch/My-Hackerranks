def candles(candlesNumber, makeNew):
    leftOver = 0
    burnt = 0
    while candlesNumber > 0 or leftOver >= makeNew:
        if leftOver >= makeNew:
            # Burn LeftOver Candle
            burnt += 1
            leftOver = 1

        if candlesNumber > 0:
            candlesNumber -= 1
            burnt += 1
            leftOver += 1

    return burnt
            

