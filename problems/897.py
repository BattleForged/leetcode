 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        leftTreeRoot = None
        newNow = None
        stack = [root]
        now = root
        while now.left != None:
            stack.append(now.left)
            now = now.left
        while len(stack) > 0:
            now = stack.pop()
            if (leftTreeRoot == None):
                leftTreeRoot = TreeNode(now.val, None, None)
                newNow = leftTreeRoot
            else:
                newNow.right = TreeNode(now.val, None, None)
                newNow = newNow.right
            if now.right != None:
                now = now.right
                stack.append(now)
                while now.left != None:
                    stack.append(now.left)
                    now = now.left
        return leftTreeRoot
            
