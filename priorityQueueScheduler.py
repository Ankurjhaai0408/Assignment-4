class Task:
    """
    Class to represent an individual task in the priority queue.
    Attributes:
        task_id (int): Unique identifier for the task.
        priority (int): Priority of the task (lower values indicate higher priority in a min-heap).
        arrival_time (str): Time when the task was added.
        deadline (str): Deadline for task completion.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Arrival: {self.arrival_time}, Deadline: {self.deadline})"


class PriorityQueue:
    """
    Priority queue implemented as a binary min-heap.
    Provides operations to insert, extract, and modify task priorities.
    """
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """
        Insert a new task into the heap while maintaining the heap property.
        :param task: Task object to be inserted.
        """
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Remove and return the task with the highest priority (lowest value in a min-heap).
        :return: Task object with the highest priority.
        """
        if self.is_empty():
            raise IndexError("Extract from empty priority queue")

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # Swap root with last element
        task = self.heap.pop()  # Remove the last element
        self._heapify_down(0)  # Restore the heap property
        return task

    def change_priority(self, task_id, new_priority):
        """
        Change the priority of an existing task and adjust its position in the heap.
        :param task_id: ID of the task whose priority is to be updated.
        :param new_priority: The new priority value for the task.
        """
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                old_priority = task.priority
                task.priority = new_priority

                if new_priority < old_priority:
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                return

        raise ValueError(f"Task with ID {task_id} not found in the heap")

    def is_empty(self):
        """
        Check if the priority queue is empty.
        :return: True if empty, False otherwise.
        """
        return len(self.heap) == 0

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

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f"PriorityQueue({self.heap})"


# Example Scheduler Simulation
def scheduler_simulation():
    """
    Simulate task scheduling using the priority queue.
    """
    pq = PriorityQueue()

    # Insert tasks
    pq.insert(Task(1, 5, "10:00", "12:00"))
    pq.insert(Task(2, 3, "10:05", "11:30"))
    pq.insert(Task(3, 8, "10:10", "13:00"))
    pq.insert(Task(4, 1, "10:15", "10:45"))

    print("Initial Priority Queue:", pq)

    # Extract and process tasks in priority order
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Processing {task}")

    print("All tasks processed.")


if __name__ == "__main__":
    scheduler_simulation()

if __name__ == "__main__":
    pq = PriorityQueue()

    # Add tasks to the priority queue
    pq.push(Task(1, 5, "10:00", "12:00"))
    pq.push(Task(2, 3, "10:05", "11:30"))
    pq.push(Task(3, 8, "10:10", "13:00"))
    pq.push(Task(4, 1, "10:15", "10:45"))

    print("Priority Queue:", pq)
    
    # Peek at the task with the highest priority
    print("Peek:", pq.peek())

    # Pop tasks and print them in order
    while not pq.is_empty():
        print("Popped:", pq.pop())
