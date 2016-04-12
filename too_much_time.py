#! /usr/bin/python

#def answer(intervals):
#    all_hours = []
#    index = 0
#    #print(intervals)
#    for [a, b] in intervals:
#        a, b = intervals[index]
#        all_hours.extend(my_range(a,b))
#        #print(a, b)
#        #for i in my_range(a, b):
#            #all_hours.append(i)
#        index = index + 1
#    all_hours.sort()
#    return hours(all_hours)
#
#def my_range(a, b):
#    i = a
#    r = []
#    while i <= b:
#        r.append(i)
#        i = i + 1
#    return r
#
#def hours(array):
#    index = 0
#    time = 0
#    #print(array)
#    for i in array:
#        try:
#            if array[index + 1] - array[index] == 1:
#                time = time + 1
#                #print(i, time)
#            index = index + 1
#        except IndexError:
#            break
#    return time

#def answer(intervals):
#    all_hours = []
#    index = 0
#    for [a, b] in intervals:
#        a, b = intervals[index]
#        while a <= b:
#            all_hours = all_hours + [a]
#            a = a + 1
#        index = index + 1
#    all_hours.sort()
#    print(all_hours)
#
#    ind = 0
#    time = 0
#    for i in all_hours:
#        try:
#            if all_hours[ind + 1] - all_hours[ind] == 1:
#                time = time + 1
#            ind = ind + 1
#        except IndexError:
#                break
#    return time

def answer(intervals):
    all_hours = []

    inde = 0
    siz = 0
    for [a, b] in intervals:
        a, b = intervals[inde]
        while a <= b:
            all_hours = all_hours + [a]
            a = a + 1
            siz = siz + 1
        inde = inde + 1
    all_hours.sort()
    #print(all_hours)
    print(len(all_hours))
    print(siz)

    ind = siz - 1
    tim = 0
    #for i in all_hours:
    while ind > 0:
        if all_hours[ind] - all_hours[ind - 1] == 1:
            tim = tim + 1
        ind = ind - 1
    return tim
print(answer([[1,2],[5,9],[13, 18],[3,10]]))
print(answer([[10,14],[4,18],[19,20],[13,20]]))
