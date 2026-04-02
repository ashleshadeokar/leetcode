class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = [(num, i) for i, num in enumerate(nums)]

        copy.sort()
        
        i, j = 0, len(copy) - 1
        while i < j:
            sum1 = copy[i][0] + copy[j][0]
            if sum1 == target:
                return sorted([copy[i][1], copy[j][1]])
            elif sum1 < target:
                i += 1
            else:
                j -= 1
        return []