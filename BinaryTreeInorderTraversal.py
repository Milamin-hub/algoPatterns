from typing import Optional, List
from Node import TreeNode

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:

    res = []
    stack = []

    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res