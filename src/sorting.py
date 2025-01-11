class SortingAlgorithms:
    """Handles sorting algorithms and generators."""

    def __init__(self):
        self.highlight_indices = (-1, -1)

    # Sorting algorithms as generators
    def bubble_sort(self, data):
        """Bubble Sort"""
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.highlight_indices = (j, j + 1)
                self.status_message = f"Comparing indices {j} and {j + 1}"
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                yield

    def quick_sort(self, low, high, data):
        """Quick Sort"""
        if low < high:
            pivot_index = yield from self.partition(low, high, data)
            yield from self.quick_sort(low, pivot_index - 1, data)
            yield from self.quick_sort(pivot_index + 1, high, data)

    def partition(self, low, high, data):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            self.highlight_indices = (j, high)
            self.status_message = f"Comparing index {j} with pivot {high}"
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
            yield
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def merge_sort(self, left, right, data):
        """Merge Sort"""
        if left < right:
            mid = (left + right) // 2
            yield from self.merge_sort(left, mid, data)
            yield from self.merge_sort(mid + 1, right, data)
            yield from self.merge(left, mid, right, data)

    def merge(self, left, mid, right, data):
        temp = data[left : right + 1]
        i, j, k = 0, mid - left + 1, left
        while i <= mid - left and j <= right - left:
            self.highlight_indices = (left + i, left + j)
            self.status_message = f"Merging indices {left + i} and {left + j}"
            if temp[i] <= temp[j]:
                data[k] = temp[i]
                i += 1
            else:
                data[k] = temp[j]
                j += 1
            k += 1
            yield
        while i <= mid - left:
            data[k] = temp[i]
            i += 1
            k += 1
            yield
        while j <= right - left:
            data[k] = temp[j]
            j += 1
            k += 1
            yield

    def insertion_sort(self, data):
        """Insertion Sort"""
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                self.highlight_indices = (j, i)
                self.status_message = f"Inserting element {i} at position {j}"
                data[j + 1] = data[j]
                j -= 1
                yield
            data[j + 1] = key
            yield
