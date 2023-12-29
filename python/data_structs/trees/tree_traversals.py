from create_tree import tree
import collections


def pre_order(root, li):
    if root is None:
        return
    else:
        li.append(root.val)
        pre_order(root.left, li)
        pre_order(root.right, li)


def post_order(root, li):
    if root is None:
        return
    else:
        post_order(root.left, li)
        post_order(root.right, li)
        li.append(root.val)


def in_order(root, li):
    if root is None:
        return
    else:
        in_order(root.left, li)
        li.append(root.val)
        in_order(root.right, li)


def level_order(root, level_list):
    if root is None:
        return None

    q = collections.deque()
    q.append(root)

    while q:
        node1 = q.popleft()
        level_list.append(node1.val)

        if node1.left is not None:
            q.append(node1.left)

        if node1.right is not None:
            q.append(node1.right)

    return level_list


def main():
    root = tree('1 4 N 4 2 ')

    pre_list = []
    pre_order(root, pre_list)
    print("the pre-order traversel is as follows", pre_list)

    post_list = []
    post_order(root, post_list)
    print("the post-order traversel is as follows", post_list)

    in_list = []
    in_order(root, in_list)
    print("the in-order traversel is as follows", in_list)

    level_list = []
    level_list = level_order(root, level_list)
    print("the level-order traversel is as follows", level_list)


if __name__ == "__main__":
    main()
