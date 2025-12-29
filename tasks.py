# This file contains queue class that implelments a queue to control core operations
class Queue:
    """A simple FIFO queue for storing tasks (strings)"""
    _arr: list

    def __init__(self):
        """Constructor for initailisng Queue"""
        self._arr = []

    def enqueue(self, s: str):
        """Function for adding task in queue"""
        self._arr.append(s)

    def dequeue(self) -> str:
        """Function for completing task in queue"""
        if not self._arr:
            raise ValueError("Queue is Empty")
        return self._arr.pop(0)

    def peek(self) -> str:
        """Function for displaying the current task"""
        if not self._arr:
            raise ValueError("Queue is Empty")
        return self._arr[0]
    
    def items(self) -> list:
        """Function for returning all tasks"""
        return self._arr.copy()

    def count(self) -> int:
        """Function returning the number of pending tasks"""
        return len(self._arr)