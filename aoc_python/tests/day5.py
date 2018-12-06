from tasks.day5 import task1, task2

def test_task1():
    p = 'lomMki'
    m = 'zaxkKazdAaLmMlzp'
    c = 'dabAcCaCBAcCcaDA'
    d = 'admqQplPmMmlLMp'
    l = 'aAaAaAAaAaAa'
    k = 'aAamM'
    assert task1(p) == 4
    assert task1(m) == 8
    assert task1(c) == 10
    assert task1(d) == 5
    assert task1(l) == 0
    assert task1(k) == 1

def test_task2():
    c = 'dabAcCaCBAcCcaDA'
    assert task2(c) == 4