# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_length: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
              
        #재귀로 노드를 후위탐색하면서 현재 노드의 길이가 최댓값인지 확인하고 갱신해간다.
        def dfs(cur_node):

            left_v = right_v = 0
            if cur_node.left != None:
                left_v = dfs(cur_node.left) + 1
                
            if cur_node.right != None:
                right_v = dfs(cur_node.right) + 1

            self.max_length = max(self.max_length, left_v + right_v)

            return max(left_v, right_v)

        dfs(root)
        return self.max_length