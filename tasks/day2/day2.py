import os
import string

inputs = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'rb') as f:
    for l in f.readlines():
        inputs.append(l.replace('\n', ''))

def task1(input):
    d = {'double': 0, 'triple': 0}
    for l in input:
        count_letters = {}
        for c in l:
            if not count_letters.get(string.lowercase.index(c)):
                count_letters[string.lowercase.index(c)] = 1
            elif count_letters.get(string.lowercase.index(c)):
                count_letters[string.lowercase.index(c)] += 1
        if len(filter(lambda x: x[1] == 2, count_letters.items())) > 0:
            d['double'] += 1
        if len(filter(lambda x: x[1] == 3, count_letters.items())) > 0:
            d['triple'] += 1
    return d['triple'] * d['double']


def task2(input):
    for i in range(len(input)):
        if i == len(input) - 1:
            continue
        for j in range(i+1,len(input)):
            diff = []
            for c, e in enumerate(input[i]):
                if e == input[j][c]:
                    continue
                else:
                    diff.append(e)
            if len(diff) == 1:
                return input[i].replace(diff[0], '')
    return None
