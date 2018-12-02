import os

inputs = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'rb') as f:
    for l in f.readlines():
        inputs.append(l.replace('\n', ''))

def task1(inputs):
    count = 0
    for l in inputs:
        count += int(l)
    return count

def task2(inputs=inputs, count=None, s=None):
    if not s:
        s = set()
    for l in inputs:
        if count is not None:
            count += int(l)
            if count in s:
                return count
            else:
                s.add(count)
        else:
            count = l
    return task2(inputs, count, s)
