from create_tree import tree


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


if __name__ == "__main__":
    main()
