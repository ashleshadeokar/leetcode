class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals:
            end_last = res[-1][1]

            if start <= end_last:
                res[-1][1] = max(end_last, end)
            else:
                res.append([start, end])
        return res