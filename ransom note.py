class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine): return False
        letter_dict = {}
        for char in magazine:
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
        for char in ransomNote:
            if char not in letter_dict:
                return False
            elif letter_dict[char] == 0:
                return False
            else:
                letter_dict[char] -= 1
        return True
    
    # o(m) len(magazine)
    #o(26) o(k) = o(1) since k is constant
