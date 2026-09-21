class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]
        '''
        output = []
        numbs = sorted(nums)
        for i in range(len(numbs)):
            if numbs[i] >0:
                break
            if i > 0 and numbs[i] == numbs[i - 1]:
                continue
            l = i + 1
            r = len(numbs)-1
            while l < r:  
                threesum = numbs[i] + numbs[l] + numbs[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l +=1
                else :
                    output.append([numbs[i], numbs[l], numbs[r]])
                    l +=1
                    r -=1
                    while numbs[l] == numbs[l-1] and l < r:
                        l += 1
        return output