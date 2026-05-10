class SegmentTreeNode:
    def __init__(self, total: int, l_idx: int, r_idx: int) -> None:
        self.sum = total
        self.left: Optional["SegmentTreeNode"] = None
        self.right: Optional["SegmentTreeNode"] = None
        self.l_idx = l_idx
        self.r_idx = r_idx


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], l_idx: int, r_idx: int):
        if l_idx == r_idx:
            return SegmentTreeNode(nums[l_idx], l_idx, r_idx)

        mid_idx = (l_idx + r_idx) // 2
        root = SegmentTreeNode(0, l_idx, r_idx)
        root.left = self.build(nums, l_idx, mid_idx)
        root.right = self.build(nums, mid_idx + 1, r_idx)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        def update_helper(node: SegmentTreeNode):
            if node.l_idx == node.r_idx:
                node.sum = val
                return
            assert node.left and node.right
            m_idx = (node.l_idx + node.r_idx) // 2
            if index > m_idx:
                update_helper(node.right)
            else:
                update_helper(node.left)
            node.sum = node.left.sum + node.right.sum

        update_helper(self.root)

    def query(self, L: int, R: int) -> int:
        def query_helper(node: SegmentTreeNode, l_idx: int, r_idx: int):
            if l_idx == node.l_idx and r_idx == node.r_idx:
                return node.sum
            assert node.left and node.right
            m_idx = (node.l_idx + node.r_idx) // 2
            if l_idx > m_idx:
                return query_helper(node.right, l_idx, r_idx)
            elif r_idx <= m_idx:
                return query_helper(node.left, l_idx, r_idx)
            else:
                return query_helper(node.left, l_idx, m_idx) + query_helper(
                    node.right, m_idx + 1, r_idx
                )

        return query_helper(self.root, L, R)
