from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        '''
        We have to take the two branches of the tree and swap them. 
        We can do this by recursively calling the invertTree function on the left and right branches of the tree.
        But, the problem is that we have to swap the branches after we have inverted them.

        '''
        left,right = self.invertTree(root.left),self.invertTree(root.right)
        root.left,root.right = right,left
        return root
