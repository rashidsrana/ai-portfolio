from python_dsa.binary_tree import BinaryTree, Node


def test_traversals(capsys):
    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)

    bt.inorder(bt.root)
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 1 3"
