import os

def task1(s):
    stack = None
    while stack != s:
        stack = s
        for i in range(0,26):
            s = s.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            s = s.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
    return len(stack)

def task2(s):
    stack = s
    smallest_s = len(s)
    for j in range(26):
        s = stack
        s = s.replace(chr(ord("a") + j),"")
        s = s.replace(chr(ord("A") + j),"")
        t = task1(s)
        smallest_s = t if t < smallest_s else smallest_s
    return smallest_s

            

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'rb') as f:
        line = f.read().replace('\n', '')

        print('Task 1: %s' %task1(line))
        print('Task2: %s' %task2(line))