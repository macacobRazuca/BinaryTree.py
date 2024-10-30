class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        if data is not None:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=' ')  # Corrigido para exibir o valor do nó

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0  # Altura de árvore vazia é -1
        # Verifique se node.left e node.right são válidos antes da recursão
        left_height = self.height(node.left) if node.left else -1
        right_height = self.height(node.right) if node.right else -1
        return 1 + max(left_height, right_height)


if __name__ == '__main__':
    # Exemplo de uso da árvore
    tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print("Raiz:", tree.root)
    print("Nó à direita da raiz:", tree.root.right)
    print("Nó à esquerda da raiz:", tree.root.left)

    print("\nPercurso em Pós-Ordem:")
    tree.postorder_traversal()
    print("\nAltura da árvore:", tree.height())
