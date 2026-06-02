class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = nums1[0 : m + 1]
        R = nums2

        l = r = i = 0

        while i < m + n:
            if r >= n or (l < m and L[l] <= R[r]):
                nums1[i] = L[l]
                l += 1
            else:
                nums1[i] = R[r]
                r += 1
            i += 1
