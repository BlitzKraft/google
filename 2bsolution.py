#!  /usr/bin/python

'''
This is not the final accepted solution. 
The final accepted one used an index to traverse the number line,
from each pair a, b. It does so only on higher indexes. There is
no array creation, so no more memory error and only traverses the
entire given array exactly once. Therefore, no time out error.
'''

def answer(intervals):
    intervals.sort(key = lambda tup: tup[0])
    print(intervals)
    imin = 10000
    imax = 0

    for a, b in intervals:
        if a < imin:
            imin = a
        if b > imax:
            imax = b

    diff = imax - imin + 1
    
    hours = [0] * diff
    for a, b in intervals:
        while a < b:
            hours[a - imin] = 1
            a = a + 1
    print(hours)

    return sam(hours)

def sam(array):
    t = 0
    for s in array:
        t = t + s
    return t

print(answer([[1,2],[5,9],[13, 18],[3,10]]))
print(answer([[10,14],[4,18],[19,20],[13,20]]))
