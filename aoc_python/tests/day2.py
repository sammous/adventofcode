from tasks.day2 import task1, task2

def test_task1():
    assert(task1(['abcdef',
                  'bababc',
                  'abbcde',
                  'abcccd',
                  'aabcdd',
                  'abcdee',
                  'ababab'])) == 12 

def test_task2():
    assert(task2([
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ])) == 'fgij'
