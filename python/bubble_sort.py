class Solution:
    def bubble_sort(array: list) -> int:
        swaps = 0
        idx = 0
        while idx < len(array):
            previous = array[idx]
            try:
                current = array[idx+1]
            except IndexError:
                print(f"Final result: {array}")
                print(f"Swaps: {swaps}")
                return swaps
            if current < previous:
                array[idx+1] = previous
                array[idx] = current
                idx = 0
                swaps += 1
            else:
                idx += 1