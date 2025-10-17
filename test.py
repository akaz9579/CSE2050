class Solution(object):
    
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if self.levelOrder(q) == self.levelOrder(p):
            return True
        else:
            return False


    out = []  

    def levelOrder(self, x):
        if x is None
            return [
        if x.left:
            out.append(x.left.val)
        
            
        


        
