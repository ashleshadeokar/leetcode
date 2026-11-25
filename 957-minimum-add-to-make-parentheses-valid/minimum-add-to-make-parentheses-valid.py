class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = add = 0
        for c in s:
            if c == "(":
                count += 1
            elif count:
                count -= 1
            else:
                add += 1
        return add + count