#! /usr/bin/python

def answer(words):
    dic = []
    print(words)
    for word in words:
        inde = (list(word)[0])
        if inde not in dic:
            dic.append(inde)
    return ''.join(dic)

inp = []
inp.append(['z','yx','yz'])
inp.append(['ba','ab','cb'])
inp.append(['y','z','xy'])


for s in inp:
    print(answer(s))

