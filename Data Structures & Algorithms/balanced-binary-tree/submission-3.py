class Solution:
    
    def findHeight(self, root):
        if not root:
            return 0

        return 1 + max(
            self.findHeight(root.left),
            self.findHeight(root.right)
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        diff = abs(left - right)

        if diff > 1:
            return False

        return (
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )