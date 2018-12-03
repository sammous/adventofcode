import numpy as np
import os 

def process_line(square, line):
    elements = line.split(' ')
    left_edge, top_edge = map(int, elements[2].replace(':','').split(','))
    wide, tall = map(int, elements[3].split('x'))
    for i in range(wide):
        for j in range(tall):
            square[top_edge + j, left_edge + i] += 1
    return square 

def task1(lines, size=1000):
    square = np.zeros((size, size), dtype=int)
    for l in lines:
        square = process_line(square, l)
    return len(np.where(square > 1)[0]), square


def task2(lines, size=1000):
    _, square = task1(lines)
    for l in lines:
        elements = l.split(' ')
        id_line = int(elements[0].replace('#',''))
        left_edge, top_edge = map(int, elements[2].replace(':','').split(','))
        wide, tall = map(int, elements[3].split('x'))
        sub_square = square[top_edge:top_edge+tall, left_edge:left_edge+wide]
        if np.array_equal(sub_square, np.full((tall, wide), 1, dtype=int)):
            return id_line
    return None

if __name__ == "__main__":
    inputs = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt'), 'rb') as f:
        for l in f.readlines():
            inputs.append(l.replace('\n', ''))
    print task2(inputs)