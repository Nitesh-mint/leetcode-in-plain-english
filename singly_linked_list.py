from typing import List


class LinkedList:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # index gauranteed to be greater or equal to 0
    def get(self, index: int) -> int:
        current = self

        while index > 0:
            if current is None:
                return -1
            current = current.next
            index -= 1

        return current.value if current else -1

    def insertHead(self, val: int) -> None:
        new_node = LinkedList(self.value, self.next)
        self.value = val
        self.next = new_node

    def insertTail(self, val: int) -> None:
        current = self

        while current.next is not None:
            current = current.next
        current.next = LinkedList(val)

    # index gauranteed to be greater or equal to 0
    def remove(self, index: int) -> bool:
        i = 0
        current = self

        while i < index - 1 and current:
            i += 1
            current = current.next

        if current and current.next:
            print(f"The index to remove {i + 1} and the value is {current.next.value}")
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        values = []
        current = self
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


sln = LinkedList(1)
sln.remove(0)
sln.get(0)
