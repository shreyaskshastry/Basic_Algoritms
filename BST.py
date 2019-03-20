def pre_order(root, nodes):
    nodes.append(root.data)
    if root and root.left:
        pre_order(root.left, nodes)
    if root and root.right:
        pre_order(root.right, nodes)
    return nodes


def in_order(root, nodes):
    if root and root.left:
        in_order(root.left, nodes)
    nodes.append(root.data)
    if root and root.right:
        in_order(root.right, nodes)
    return nodes


def post_order(root, nodes):
    if root and root.left:
        post_order(root.left, nodes)
    if root and root.right:
        post_order(root.right, nodes)
    nodes.append(root.data)
    return nodes

    # Breadth First Search


def level_order(root, nodes):
    queue = [root]
    while queue:
        n = queue.pop(0)
        nodes.append(n.data)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    return nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# create nodes
root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')
n5 = Node('F')

# setup children
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n3.left = n5

print(pre_order(root, []))  # => ['A', 'B', 'D', 'E', 'C']
print(in_order(root, []))  # => ['F','D', 'B', 'E', 'A', 'C']
print(post_order(root, []))  # => ['F','D', 'E', 'B', 'C', 'A']
print(level_order(root, []))  # => ['A', 'B', 'C', 'D', 'E','F']breadth first searc