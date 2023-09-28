from typing import Optional
from collections import deque
from Node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    if not p and not q:
        return True
    
    queue = deque([(p, q)])
    while queue:
        node1, node2 = queue.popleft()

        if not node1 or not node2 or node1.val != node2.val:
            return False
        
        if node1.left or node2.left:
            queue.append((node1.left, node2.left))

        if node1.right or node2.right:
            queue.append((node1.right, node2.right))
            
    return True