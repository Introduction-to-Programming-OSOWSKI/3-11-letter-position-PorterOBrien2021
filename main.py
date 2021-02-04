def letterPos(w, x):
    for i in range(0, len(w)):
        if i == "x":
            return w[x]
        else:
            return 0

print(letterPos("reed", "e"))
