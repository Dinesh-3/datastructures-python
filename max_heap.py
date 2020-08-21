class MaxHeap:
    def __init__(self, collection=None):
        self._heap = []

        if collection is not None:
            for el in collection:
                self.push(el)

    def push(self, value):
        self._heap.append(value)
        _sift_up(self._heap, len(self) - 1)

    def pop(self):
        _swap(self._heap, len(self) - 1, 0)
        el = self._heap.pop()
        _sift_down(self._heap, 0)
        return el

    def __len__(self):
        return len(self._heap)

    def print(self, idx=1, indent=0):
        print("\t" * indent, f"{self._heap[idx - 1]}")
        left, right = 2 * idx, 2 * idx + 1
        if left <= len(self):
            self.print(left, indent=indent + 1)
        if right <= len(self):
            self.print(right, indent=indent + 1)


def _swap(L, i, j):
    L[i], L[j] = L[j], L[i]


def _sift_up(heap, idx):
    parent_idx = (idx - 1) // 2
    # If we've hit the root node, there's nothing left to do
    if parent_idx < 0:
        return

    # If the current node is larger than the parent node, swap them
    if heap[idx] > heap[parent_idx]:
        _swap(heap, idx, parent_idx)
        _sift_up(heap, parent_idx)


def _sift_down(heap, idx):
    child_idx = 2 * idx + 1
    # If we've hit the end of the heap, there's nothing left to do
    if child_idx >= len(heap):
        return

    # If the node has a both children, swap with the larger one
    if child_idx + 1 < len(heap) and heap[child_idx] < heap[child_idx + 1]:
        child_idx += 1

    # If the child node is smaller than the current node, swap them
    if heap[child_idx] > heap[idx]:
        _swap(heap, child_idx, idx)
        _sift_down(heap, child_idx)


def heap_sort(collection):
    heap = MaxHeap(collection)
    sorted_arr = []
    while len(heap) > 0:
        sorted_arr.append(heap.pop())
    return sorted_arr
