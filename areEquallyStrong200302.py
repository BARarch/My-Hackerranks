def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStongest = max(yourLeft, yourRight)
    yourWeakest = min(yourLeft, yourRight)
    friendsStrongest = max(friendsLeft, friendsRight)
    friendsWeakest = min(friendsLeft, friendsRight)

    return (yourStongest == friendsStrongest) and (yourWeakest == friendsWeakest)
