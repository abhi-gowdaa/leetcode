# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        
        def dfsHeight(root):
            if root is None:
                return 0       
            left= dfsHeight(root.left)
            if left==-1:
                return -1
            right= dfsHeight(root.right)
            if right==-1:
                return -1

            if abs(left-right)>1:
                return -1

            return max(left,right)+1

    
        return  dfsHeight(root) != -1


