# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        #현재 위치에 root1노드와 root2노드가 모두 있다면
        if root1 and root2:
            #병합된 새로운 노드 생성
            new_node = TreeNode(root1.val + root2.val)

            #새로운 노드에 병합된 자식 트리 부착
            new_node.left = self.mergeTrees(root1.left, root2.left) #병합된 left 트리를 반환한다고 믿는다.
            new_node.right = self.mergeTrees(root1.right, root2.right) #병합된 right 트리를 반환한다고 믿는다.

            #병합 완료된 현재노드를 반환
            return new_node
        else:
            #반환한 트리가 이전 단계의 new_node의 자식으로 붙게 된다.
            return root1 or root2