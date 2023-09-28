from typing import Optional
from collections import deque
from Node import TreeNode


def isSymmetric(root: Optional[TreeNode]) -> bool:
        
    q = deque([root])

    while q:

        level = []
        for _ in range(len(q)):

            cur = q.popleft()
            level.append(cur.val if cur else '🐼')

            if cur:
                q.append(cur.left)
                q.append(cur.right)

        if len(level) > 1:

            n = len(level)
            fh, sh = level[:n // 2], level[n // 2:][::-1]

            if fh != sh :
                return False
    return True