class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = defaultdict(list)
        for word in strs:
            alpha = [0]*26
            sum = 0
            for char in word:
                alpha[ord(char) - ord('a')] +=1
            op[tuple(alpha)].append(word)
        return(list(op.values()))