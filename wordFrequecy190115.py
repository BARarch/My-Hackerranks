if __name__ == "__main__":
    words = []
    hashh = {}
    for _ in range(int(input().rstrip())):
        word = input().rstrip()
        words.append(word)
        if word in hashh:
            hashh[word] += 1
        else:
            hashh[word] = 1

    print(len(hashh))

    for word in words:
        if word in hashh:
            print(hashh[word], end=' ')
            del hashh[word]
