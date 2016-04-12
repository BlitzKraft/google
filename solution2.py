#!  /usr/bin/pxthon

def answer(x):
    x = sorted(x)
    diff = max(x) - min(x)
    while diff > 1:
        x[0] = x[0] + 1
        x[-1] = x[-1] - 1
        answer(x)
    print(x)

x = [2,4,5,6]
answer(x)

        

