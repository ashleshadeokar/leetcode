# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # res = []            
        # for q in queries:
        #     ans = [float('-inf'), float('inf')]
        #     node = root

        #     while node:
        #         if q == node.val:
        #             ans = [q, q]
        #             break
        #         if q > node.val:
        #             ans = [max(ans[0], node.val), ans[1]]
        #             node = node.right
        #         else:
        #             ans = [ans[0], min(ans[1], node.val)]
        #             node = node.left

        #     mini = ans[0] if ans[0] != float('-inf') else -1
        #     maxi = ans[1] if ans[1] != float('inf') else -1
        #     res.append([mini, maxi])
        # return res

        def inOrder(self, root, sortedTree):
            if root:
                self.inOrder(root.left, sortedTree)
                sortedTree.append(root.val)
                self.inOrder(root.right, sortedTree)
        
        def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
            sortedTree = []
            result = []
            self.inOrder(root, sortedTree)

            for i in queries:
                idx = bisect_left(sortedTree, i)

                if idx > 0 and (idx == len(sortedTree) or sortedTree[idx] > i):
                    mini = sortedTree[idx - 1]
                elif idx < len(sortedTree) and sortedTree[idx] == i:
                    mini = i
                else:
                    mini = -1

                if idx < len(sortedTree):
                    maxi = sortedTree[idx]
                else:
                    maxi = -1

                result.append([mini, maxi])

            return result
