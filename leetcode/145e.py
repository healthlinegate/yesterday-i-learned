# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        buffer = []

        def recurse(node):
            if not node:
                return
            recurse(node.left)
            recurse(node.right)
            buffer.append(node.val)

        recurse(root)
        return buffer
