from typing import List


class Solution:
    def kth_Largest_And_Smallest_By_AscendingOrder(self, arr, k) :
        arr.sort()
        n = len(arr)
        print("kth Largest element", arr[n - k],"kth Smallest element", arr[k - 1])


if __name__ == "__main__":
    arr = [1, 2, 6, 4, 5, 3]
    Solution().kth_Largest_And_Smallest_By_AscendingOrder(arr, 3)
