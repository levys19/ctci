from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_subtree(tree1, tree2):
    def match_tree(t1, t2):
        if t1.val == t2.val:
            if t2.left == None and t2.right == None:
                return True
            elif t2.right == None and t2.left != None:
                return True and match_tree(t1.left, t2.left)
            elif t2.left == None and t2.right != None:
                return True and match_tree(t1.right, t2.right)
            else:
                return True and match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)
        else:
            return False
    visiting = deque()
    visiting.append(tree1)
    while visiting:
        curr_node = visiting.popleft()
        print("curr : " + str(curr_node.val))
        if curr_node.val == tree2.val:
            if match_tree(curr_node, tree2):
                return True
            
        if curr_node.left == None and curr_node.right == None:
            print("nothing left")
            continue
        elif curr_node.left == None:
            visiting.append(curr_node.right)
        elif curr_node.right == None:

            visiting.append(curr_node.left)
        else:
            print(curr_node.left.val)
            print(curr_node.right.val)

            visiting.append(curr_node.left)
            visiting.append(curr_node.right)
    return False




smallT = TreeNode(3)
smallT.left = TreeNode(4)
smallT.right = TreeNode(5)


bigT = TreeNode(1)
bigT.left = TreeNode(2)
bigT.right = TreeNode(3)
bigT.left.left = TreeNode(4)
bigT.left.right = TreeNode(5)
bigT.right.left = TreeNode(6)
bigT.right.right = TreeNode(7)


print(check_subtree(bigT,smallT))