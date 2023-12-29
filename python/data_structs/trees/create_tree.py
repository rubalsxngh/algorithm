import collections


class Node:
    def __init__(self, val):
        self.val = int(val)
        self.left = None
        self.right = None


def tree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    nodes_val = list(map(str, s.split()))

    root = Node(nodes_val[0])

    q = collections.deque()
    q.append(root)

    i = 1
    while q and i < len(nodes_val):
        node = q.popleft()

        if nodes_val[i] != 'N':
            node.left = Node(nodes_val[i])
            q.append(node.left)

        i += 1

        if i >= len(nodes_val):
            break

        if nodes_val[i] != 'N':
            node.right = Node(nodes_val[i])
            q.append(node.right)

        i += 1

    return root


def main():
    s = input()
    root = tree(s)

    print(root)

if __name__ == "__main__":
    main()
