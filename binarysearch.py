class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            split = (right+left)//2
            if nums[split] == target:
                return split
            elif nums[split] >  target:
                right = split-1
            else:
                left = split+1
        return -1
#time O(log n)
#space O(1)
