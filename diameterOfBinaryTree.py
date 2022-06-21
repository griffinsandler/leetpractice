class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        
        def longestPath(root):
            if not root:
                return 0
            nonlocal diameter
            left_path = longestPath(root.left)
            right_path = longestPath(root.right)
            if diameter < (left_path+right_path):
                diameter = (left_path+right_path)
            return 1 + max(left_path, right_path)
        
        longestPath(root)
        return diameter
    
    #space 0(n)
    #time O(n)
