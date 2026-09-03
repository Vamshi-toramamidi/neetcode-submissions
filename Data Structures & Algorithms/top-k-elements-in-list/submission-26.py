class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return []

        dictionary = {}
        for num in nums:
            dictionary[num] = 1 + dictionary.get(num, 0)
        heap = []

        for key in dictionary:
            heapq.heappush(heap,(dictionary[key], key))
            if len(heap)>k:
                heapq.heappop(heap)
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output


        '''
#Create a dictionary to store number and frequency of number
        dictionary = {}
        for val in nums:
            if val in dictionary:
                dictionary[val] += 1
            else:
                dictionary[val] = 1

# Sort the dictionary in Desc Order 
        sorted_desc = dict(sorted(dictionary.items(),
                            key=lambda item: item[1], reverse=True))   

# Extract the keys of the list                  
        op = list(sorted_desc)

# Return the top k elements in the list as its already in desc order (acc. to frequency)
       return op[0:k]
        '''

       