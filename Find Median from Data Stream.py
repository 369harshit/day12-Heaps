class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        self.nums.append(num)

    def findMedian(self):
        sorted_nums = sorted(self.nums)
        n = len(sorted_nums)
        if n % 2 == 0:
            mid_right = n // 2
            mid_left = mid_right - 1
            return (sorted_nums[mid_left] + sorted_nums[mid_right]) / 2
        else:
            mid = n // 2
            return sorted_nums[mid]

operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
values = [[], [1], [2], [], [3], []]

result = []
median_finder = MedianFinder()

for op, val in zip(operations, values):
    if op == "MedianFinder":
        result.append(None)
    elif op == "addNum":
        median_finder.addNum(val[0])
        result.append(None)
    elif op == "findMedian":
        result.append(median_finder.findMedian())

print(result)
