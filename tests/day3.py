from tasks.day3 import process_line, task1, task2
import numpy as np

def test_process_line():
    line = '#1 @ 1,1: 3x2'
    init = np.zeros((5,5), dtype= int)
    square = np.array(
        [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    )
    assert np.array_equal(square, process_line(init, line))

def test_task1():
    square = np.array(
        [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 2, 2, 0],
        [0, 0, 2, 2, 0],
        [0, 0, 0, 0, 0]]
    )
    lines = [
        '#1 @ 1,1: 3x2',
        '#2 @ 2,2: 2x2',
        '#3 @ 2,3: 2x1'
    ]
    x, y = task1(lines, size=5)
    assert x == 4
    assert np.array_equal(square, y)

def test_task2():
    square = np.array(
        [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 2, 2, 0],
        [0, 0, 2, 2, 0],
        [0, 0, 1, 1, 0]]
    )
    lines = [
        '#1 @ 1,1: 3x2',
        '#2 @ 2,2: 2x2',
        '#3 @ 2,3: 2x1',
        '#4 @ 2,4: 2x1'
    ]
    assert 4 == task2(lines, size=5)
