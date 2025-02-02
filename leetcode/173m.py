# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    nodes = []

    def __init__(self, root: Optional[TreeNode]):

        def recurse(node):
            if not node:
                return
            recurse(node.left)
            self.nodes.append(node)
            recurse(node.right)
        recurse(root)

    def next(self) -> int:
        node = self.nodes.pop(0)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
