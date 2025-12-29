class Queue:
    """A simple FIFO queue for storing tasks (strings)"""
    _arr: list

    def __init__(self):
        self._arr = []

    def enqueue(self, s: str):
        self._arr.append(s)

    def dequeue(self) -> str:
        if not self._arr:
            raise ValueError("Queue is Empty")
        return self._arr.pop(0)

    def peek(self) -> str:
        if not self._arr:
            raise ValueError("Queue is Empty")
        return self._arr[0]
    
    def items(self) -> list:
        return self._arr.copy()
        
    def count(self) -> int:
        return len(self._arr)