from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ''' 
        We have to go from top to bottom and left to right, so we can use a queue to help us with that.
        We will use a queue to keep track of the nodes at each level. 
        We will also keep track of the current level we are on, so we can add the values of the nodes at that level to a list.

        My plan is to firts go till the end of the left side of the tree and then go to the right side of the tree.
        '''
        queue = [root]
        result = []

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
        return result