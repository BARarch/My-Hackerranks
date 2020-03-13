def tennisSet(score1, score2):
    return (min(score1, score2) < 5 and max(score1, score2) == 6) or (min(score1, score2) >= 5 and min(score1, score2) < 7 and max(score1, score2) == 7)

