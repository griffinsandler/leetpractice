class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letter_dic = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in letter_dic:
                letter_dic[char] += 1
            else: 
                letter_dic[char] = 1
        for char in t:
            if char not in letter_dic:
                return False
            elif letter_dic[char] <= 0:
                return False
            else:
                letter_dic[char] -= 1
        return True
    
    #Runtime O(n)
    
    #Space O(1)
    
    # def isAnagram(self, s, t):
#        if len(s) != len(t):
#            return False
#        return sorted(s) == sorted(t)

#O(nlogn)
#O(n)
