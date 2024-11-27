def regressiva(i):
    if i <= 0:
        print("End!")
        return
    print(i)
    regressiva(i - 1)

regressiva(3)
