class Solution:
    

    def partition(self, s: str) -> list[list[str]]:
        res = []
        subset = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtrack(j, i):
            if i >= len(s):
                if i == j:
                    res.append(subset.copy())
                return 

            if isPali(s, j, i):
                subset.append(s[j: i + 1])
                backtrack(i + 1, i + 1)
                subset.pop()

            backtrack(j, i + 1)

        backtrack(0, 0)
        return res