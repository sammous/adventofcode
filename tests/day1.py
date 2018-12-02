from tasks.day1 import task1, task2

def test_task1():
    assert task1([+1, +1, +1]) == 3
    assert task1([+1, +1, -2]) == 0
    assert task1([-1, -2, -3]) == -6

def test_task2():
    assert task2([+1, -1]) == 0
    assert task2([+3, +3, +4, -2, -4]) == 10
    assert task2([-6, +3, +8, +5, -6]) == 5
    assert task2([+7, +7, -2, -7, -4]) == 14
