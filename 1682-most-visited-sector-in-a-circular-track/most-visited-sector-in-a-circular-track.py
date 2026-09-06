class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        res = []
        if start == end:
            return [start]
        
        if start < end:
            for i in range(start, end + 1):
                res.append(i)
        else:
            for i in range(1, end + 1):
                res.append(i)
                
            for i in range(start, n + 1):
                res.append(i)
        return res