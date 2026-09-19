class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        if not numbers:
            return [0,0]
        hashset = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in hashset:
                return([hashset[diff]+1,i+1])
            hashset[num] = i
        '''
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []