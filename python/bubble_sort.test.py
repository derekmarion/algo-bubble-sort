from bubble_sort import Solution

def test_01():
    sequence = [4, 3, 5, 0, 1]
    assert Solution.bubble_sort(sequence) == 7

def test_02():
    sequence = [1, 0, 2, 3, 4, 5]
    assert Solution.bubble_sort(sequence) == 1