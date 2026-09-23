class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        brute force solution, traverse the tree in-order and return the kth element
        My approch is to use the left side of the tree to find the kth smallest element. 
        If K> the number of nodes in the left subtree, then we know that the kth smallest element is in the right subtree.
        Then we can recursively call the function on the right subtree with k reduced by the number of nodes in the left subtree + 1 (for the root node).
        '''
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        left_count = count_nodes(root.left)
        if k <= left_count:
            return self.kthSmallest(root.left, k)
        elif k == left_count + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left_count - 1)