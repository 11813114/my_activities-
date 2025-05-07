from typing import List


class Solution:
    def merge(self, arr: List[int], l, m, r):
        l1, l2 = l, m + 1
        temp = []
        while l1 <= m and l2 <= r:
            if arr[l1] <= arr[l2]:
                temp += [arr[l1]]
                l1 += 1
            else:
                temp += [arr[l2]]
                l2 += 1
        temp.extend(arr[l1:m + 1])
        temp.extend(arr[l2:r + 1])
        arr[l:r + 1] = temp[:]

    def mergeSort(self, arr: List[int], l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.merge(arr, l, mid, r)
# Auto commit on 2023-01-12
# Auto commit on 2023-01-10
# Auto commit on 2023-01-12
# Auto commit on 2023-01-11
# Auto commit on 2023-01-12
# Auto commit on 2023-01-13
# Auto commit on 2023-01-11
# Auto commit on 2023-01-13
# Auto commit on 2023-01-11
