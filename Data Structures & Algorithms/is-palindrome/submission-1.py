class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(c for c in s if c.isalnum())).lower()
        j = s[::-1]
        if s != j:
            return False 
        return True