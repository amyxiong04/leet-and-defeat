class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        non = []

        for interval in intervals:
            if not non or interval[0] >= non[-1][1]:
                non.append(interval)  

        return len(intervals) - len(non)      