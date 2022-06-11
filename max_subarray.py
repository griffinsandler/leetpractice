class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current_value = nums[0]
        
        for num in nums[1:]:
            current_value = max(num, current_value + num)
            max_value = max(max_value, current_value)
                
        return max_value
    
    #O(n) time
    # O(1)
    #could use divide and conquer
            
