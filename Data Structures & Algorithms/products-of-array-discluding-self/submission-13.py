class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pre = 1
        post = 1
        for i in range(len(nums)):
            output.append(pre)
            pre = pre * nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * post
            post = post * nums[i]
        return output