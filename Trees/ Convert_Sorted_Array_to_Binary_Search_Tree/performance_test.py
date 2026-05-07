import sys
import time
from solution import Solution


def performance_test():

    sys.setrecursionlimit(2000000)

    solution = Solution()
    sizes = [100, 1000, 10000, 100000]

    for n in sizes:

        test_data = list(range(n))
        start_time = time.perf_counter()
        solution.sortedArrayToBST(test_data)
        end_time = time.perf_counter()

        duration = end_time - start_time
        print (f"{n:12,d}, {duration:15.6f}")

if __name__ == "__main__":
    performance_test()


