if __name__ == "__main__":
    txt = "   apple banana   cherry  orange "

    x = txt.split(" ")
    print(x)
    print(list(filter(lambda word: bool(word),x)))
    print(list(filter(lambda word: bool(word),x))[::-1])

    print(" ".join(["cat", "dog"]))

    print(" ".join(list(filter(bool,x))[::-1]))
   

