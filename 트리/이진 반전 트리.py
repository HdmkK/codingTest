# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        if not root:
            return root

        # 이 함수는 cur_node를 기준으로 invert 트리를 만든다고 믿는다.
        #재귀를 사용하여 리프노드부터 위로 차근차근 invert해 나간다.
        def dfs(cur_node):

            if cur_node.left == None and cur_node.right == None:
                return

            if cur_node.left:
                dfs(cur_node.left)
            if cur_node.right:
                dfs(cur_node.right)

            tmp = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = tmp


        dfs(root)

        return root