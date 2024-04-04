# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        
        
        preList=[]
#recursion
        def trav(root,preList):
            
            if root==None:
                return


            trav(root.left,preList)
            trav(root.right,preList)
            preList.append(root.val)

        trav(root,preList)
        return preList

        