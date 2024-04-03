# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def preorderTraversal(self, root):
        preList=[]
        
        def trav(root,preList):
            if root==None:
                return
            
            preList.append(root.val)
            trav(root.left,preList)
            trav(root.right,preList)
        
        trav(root,preList)
        return preList
        
        