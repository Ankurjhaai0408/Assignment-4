class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, task):
        """
        Add a new task to the priority queue.
        :param task: Task object to be added
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Remove and return the task with the highest priority.
        :return: Task object with the highest priority
        """
        if not self.heap:
            raise IndexError("Pop from empty priority queue")

        # Swap the root with the last element and remove the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        task = self.heap.pop()
        self._heapify_down(0)
        return task

    def peek(self):
        """
        Return the task with the highest priority without removing it.
        :return: Task object with the highest priority
        """
        if not self.heap:
            raise IndexError("Peek from empty priority queue")
        return self.heap[0]

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        n = len(self.heap)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def is_empty(self):
        """
        Check if the priority queue is empty.
        :return: True if empty, False otherwise
        """
        return len(self.heap) == 0

    def __len__(self):
        """
        Get the number of tasks in the priority queue.
        :return: Number of tasks
        """
        return len(self.heap)

    def __repr__(self):
        return f"PriorityQueue({self.heap})"
