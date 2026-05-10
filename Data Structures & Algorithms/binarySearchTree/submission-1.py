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

    def _insert_rec(
        self,
        node: TreeNode | None,
        key: int,
        val: int,
    ) -> TreeNode:
        if not node or key == node.key:
            node = TreeNode(key, val)
        elif key < node.key:
            node.left = self._insert_rec(node.left, key, val)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key, val)
        return node

    def insert(self, key: int, val: int) -> None:
        self.tree = self._insert_rec(self.tree, key, val)

    def _get_rec(self, node: TreeNode | None, key: int) -> int:
        if not node:
            return -1
        elif key < node.key:
            return self._get_rec(node.left, key)
        elif key > node.key:
            return self._get_rec(node.right, key)
        else:
            return node.val

    def get(self, key: int) -> int:
        return self._get_rec(self.tree, key)

    def _getMin_rec(self, node: TreeNode) -> TreeNode:
        return node if not node.left else self._getMin_rec(node.left)

    def getMin(self) -> int:
        return self._getMin_rec(self.tree).val if self.tree else -1

    def _getMax_rec(self, node: TreeNode) -> TreeNode:
        return node if not node.right else self._getMax_rec(node.right)

    def getMax(self) -> int:
        return self._getMax_rec(self.tree).val if self.tree else -1

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
            right_min = self._getMin_rec(node.right)
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
        if not node:
            return inorder
        self._getInorderKeys_rec(node.left, inorder)
        inorder.append(node.key)
        self._getInorderKeys_rec(node.right, inorder)
        return inorder

    def getInorderKeys(self) -> List[int]:
        return self._getInorderKeys_rec(self.tree, [])
