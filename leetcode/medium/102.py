from idlelib.tree import TreeNode
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans

#class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         answer = []
#         if root == None:
#             return []
#         self.solve(0, answer, root)
#         return answer
#
#     def solve(self, count: int, answer: list, root: Optional[TreeNode]):
#         if root is None:
#             return answer
#
#         if len(answer) < count + 1:
#             answer.append([])
#
#         answer[count].append(root.val)
#         self.solve(count + 1, answer, root.left)
#         self.solve(count + 1, answer, root.right)


class TestSolution(unittest.TestCase):
    def test01(self):
        root = TreeNode(1)
        answer = [[1]]
        result = Solution().levelOrder(Optional[root])
        print(result)
        assert answer == result