for e in range(9):
    if e % 3 == 0:
        print(e)

e = [e for e in range(9) if e % 3 == 0]
print(e)

e = (e for e in range(9) if e % 3 == 0)
