from data_structs.trees.create_tree import tree, Node

import unittest


class test_create_tree(unittest.TestCase):
    def test_tree(self):
        s = '1 4 N 4 2'

        self.assertIsInstance(tree(s), Node)  # case 1: normal tree

        # case 2: no string so return None
        s = ''
        self.assertIsNone(tree(s))

        s = 'N'
        self.assertIsNone(tree(s))
