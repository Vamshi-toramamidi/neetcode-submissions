class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        new_s = s[::-1]
        print(s,new_s)
        if s.lower()== new_s.lower():
            return True
        else:
            return False