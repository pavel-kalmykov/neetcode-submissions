from typing import List


class TreeNode:

    def __init__(
        self,
        key: int,
        val: int,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:

    def __init__(self):
        self.tree = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not (node := self.tree):
            self.tree = new_node
            return
        while node:
            if key < node.key:
                if not node.left:
                    node.left = new_node
                    break
                else:
                    node = node.left
            elif key > node.key:
                if not node.right:
                    node.right = new_node
                    break
                else:
                    node = node.right
            else:
                node.val = val
                break

    def get(self, key: int) -> int:
        value = -1
        node = self.tree
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                value = node.val
                break
        return value

    def _getMin_node(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        return self._getMin_node(self.tree).val if self.tree else -1

    def _getMax_node(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node

    def getMax(self) -> int:
        return self._getMax_node(self.tree).val if self.tree else -1

    def _remove_rec(self, node: TreeNode | None, key: int) -> TreeNode | None:
        if not node:
            pass
        elif key < node.key:
            node.left = self._remove_rec(node.left, key)
        elif key > node.key:
            node.right = self._remove_rec(node.left, key)
        elif not node.left:
            node = node.right
        elif not node.right:
            node = node.left
        else:
            right_min = self._getMin_node(node.right)
            node.right = self._remove_rec(node.right, right_min.key)
            right_min.left = node.left
            right_min.right = node.right
            node = right_min
        return node

    def remove(self, key: int) -> None:
        self.tree = self._remove_rec(self.tree, key)

    def _getInorderKeys_rec(
        self,
        node: TreeNode | None,
        inorder: List[int],
    ) -> List[int]:
        if node:
            self._getInorderKeys_rec(node.left, inorder)
            inorder.append(node.key)
            self._getInorderKeys_rec(node.right, inorder)
        return inorder

    def getInorderKeys(self) -> List[int]:
        return self._getInorderKeys_rec(self.tree, [])
