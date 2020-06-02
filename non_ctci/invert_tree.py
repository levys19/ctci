# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def flip(node):
            if node.left == None and node.right == None:
                return node
            elif node.left == None:
                node.left = node.right
                node.right = None
                flip(node.left)
            elif node.right == None:
                node.right = node.left
                node.left = None
                flip(node.right)
            else:
                holder = node.left
                node.left = node.right
                node.right = holder
                flip(node.left)
                flip(node.right)
        if root != None:
            flip(root)
        return root