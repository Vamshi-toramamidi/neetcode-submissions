class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_array = set(nums)
        if len(set_array) == len(nums):
            return False
        else: 
            return True