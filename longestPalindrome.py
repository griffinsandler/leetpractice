class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()
        
        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        return 2*pairs+1 if unpaired_chars else pairs*2
    
    #time o(n)
    #space o(1)
