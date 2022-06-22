class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        output = []
        idx = 0
        n = len(intervals)
        
        while idx < n and n_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
        
        if not output or output[-1][1] < n_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], n_end)
        
        while idx < n:
            interval = intervals[idx]
            idx += 1
            if output[-1][1] < interval[0]:
                output.append(interval) 
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output
        
#O(n)
#O(n)
