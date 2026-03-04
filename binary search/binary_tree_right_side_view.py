# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])  #queue for bfs (starts with root)

        while q: 
            level_size = len(q)

            # Process exactly one level (all nodes currently in queue)
            for i in range(level_size):
                node = q.popleft()   # Remove the front node (FIFO)

                # Add this node's children for the NEXT level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                # The last node processed in this level is the rightmost one
                if i == level_size - 1:
                    res.append(node.val)
                
        return res