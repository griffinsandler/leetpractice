class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_hash = {}
        for num in nums:
            if num in dup_hash:
                return True
            else:
                dup_hash[num] = True
        return False

#O(n) Time
#O(n) space
