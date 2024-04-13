# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
 
    def maxPathSum(self, root):
        def depthSum(root,maxi):
            if not root:
                return 0
            left=max(0,depthSum(root.left,maxi))
            right=max(0,depthSum(root.right,maxi))
            
            maxi[0]=max(maxi[0],left+right+root.val)
            
            return root.val+max(left,right)
        
        maxi=[float('-inf')]
        depthSum(root,maxi)
        return maxi[0]
 
            
        
            
       
        