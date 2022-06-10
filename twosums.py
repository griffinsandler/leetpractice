class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}
        for i in range(len(nums)):
            if (target-nums[i]) in sum_hash:
                return [i,sum_hash[(target-nums[i])]]
            sum_hash[(nums[i])] = i
                
