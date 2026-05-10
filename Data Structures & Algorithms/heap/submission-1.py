from typing import List


class MinHeap:

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        h = self.heap
        h.append(val)

        i = len(h) - 1
        while i > 1 and h[i] < h[i // 2]:
            h[i], h[i // 2] = h[i // 2], h[i]
            i //= 2

    def pop(self) -> int:
        h = self.heap
        if len(h) == 1:
            return -1
        if len(h) == 2:
            return h.pop()
        popped, h[1] = h[1], h.pop()
        self._percolate_down()
        return popped

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            self.heap = [0]
            return
        nums.append(nums[0])
        self.heap = nums
        mid = (len(nums) - 1) // 2
        for i in range(mid, 0, -1):
            self._percolate_down(i)

    def _percolate_down(self, i: int = 1):
        h = self.heap
        n = len(h)
        while i * 2 < n:
            cur = h[i]
            l_child = h[i * 2]
            r_child = h[i * 2 + 1] if i * 2 + 1 < n else None
            if r_child is not None and r_child < l_child and r_child < cur:
                h[i * 2 + 1], h[i] = h[i], h[i * 2 + 1]
                i = i * 2 + 1
            elif l_child < cur:
                h[i * 2], h[i] = h[i], h[i * 2]
                i = i * 2
            else:
                break
