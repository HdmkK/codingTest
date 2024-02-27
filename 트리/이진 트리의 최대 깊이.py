# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0
        
        queue = deque()
        depth = 1

        queue.append((root, depth))

        while queue:
            cur_node, depth = queue.popleft()

            if cur_node.left != None:
                queue.append((cur_node.left, depth+1))
            if cur_node.right != None:
                queue.append((cur_node.right, depth+1))

        return depth

        