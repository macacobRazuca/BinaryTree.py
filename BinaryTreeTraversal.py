from tree_pós_ordem import BinaryTree, Node


def inorder_example_tree():
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    return tree
    # tree.simetric_traversal()
    # print()

    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e'
    #           /   \
    #         'c'   'd'

    # (a + (b * ((c/d) - e)))


# Vídeo Percurso em Pós-Ordem:
def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node('G')
    n2 = Node('a')
    n3 = Node('b')
    n4 = Node('r')
    n5 = Node('i')
    n6 = Node('e')
    n7 = Node('l')
    n8 = Node('2')
    n9 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree


if __name__ == "__main__":
    tree = postorder_example_tree()
    print("Percurso em pós ordem:")
    tree.postorder_traversal()
    print("Altura: ", tree.height())
