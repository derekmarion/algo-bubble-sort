from bubble_sort import Solution

def test_01():
    sequence = [4, 3, 5, 0, 1]
    assert Solution.bubble_sort(sequence) == 7

def test_02():
    sequence = [1, 0, 2, 3, 4, 5]
    assert Solution.bubble_sort(sequence) == 1

def test_03():
    sequence = [5, 4, 3, 2, 1]
    assert Solution.bubble_sort(sequence) == 10

def test_04():
    sequence = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert Solution.bubble_sort(sequence) == 45

def test_05():
    sequence = list(range(20, 0, -1))
    assert Solution.bubble_sort(sequence) == 190