class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [0,0]
        hashset = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in hashset:
                return([hashset[diff]+1,i+1])
            hashset[num] = i