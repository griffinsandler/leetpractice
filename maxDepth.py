class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
#time O(n) num nodes
#space O(n) unbalanced O(logN) balanced
