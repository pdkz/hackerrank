"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        print(node.info, end=' ')
        dfs(node.right)
    dfs(root)
