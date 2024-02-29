# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    longest:int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        # 이 함수는 현재노드와 동일한 값을 갖는 오른쪽 path와 왼쪽 path중 더 긴 길이를 반환하면서
        # 동시에 현재까지 탐색한 노드에서 자신과 동일한 값을 가진 노드의 최대 길이를 longest에 갱신한다고 믿는다.
        def dfs(cur_node):

            if cur_node.left == None and cur_node.right == None:
                return 0

            left_v = right_v = 0

            if cur_node.left != None:
                ret = dfs(cur_node.left)
                if cur_node.val == cur_node.left.val:
                    left_v = ret + 1
            
            if cur_node.right != None:
                ret = dfs(cur_node.right)
                if cur_node.val == cur_node.right.val:
                    right_v = ret + 1

            self.longest = max(self.longest, left_v + right_v)

            return max(left_v, right_v)
        
        dfs(root)

        return self.longest