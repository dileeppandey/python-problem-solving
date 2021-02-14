"""
Class Definition for Trees
"""

from typing import TypeVar, Generic, Any
from enum import auto, Enum

class Order(Enum):
    """Describes the order of tree traversal
    """
    PREORDER = auto()
    INORDER = auto()
    POSTORDER = auto()


class BinaryTreeNode():
    """Describes a node in a Binary Tree
    """

    def __init__(self, val: Any, left:BinaryTreeNode, right:BinaryTreeNode) -> None:
        self._val = val
        self._left  = left
        self._right = right

    def _insert(self, node: BinaryTreeNode, is_left: bool=True) -> None:
        """Insert a node in Binary Tree

        Args:
            node: BinaryTreeNode, instance of BinaryTreeNode to be added
            is_left: bool, if True add as left child else the right child

        Returns:
            None

        Raise:
            ValueError: if node is None
        """
        if node is None:
            raise ValueError('The passed node is None')

        if is_left:
            self._left = node
        else:
            self._right = node


class BinaryTree():
    """Describes a Binary Tree
    """

    def __init__(self, node: BinaryTreeNode=None) -> None:
        self._root = node

    def _serialize(self, nodes: list<BinaryTreeNode>, order:Order=Order.INORDER) -> None:
        """Given a list of nodes in  a
        """
        pass
