class LinkedList:
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def get(self, index: int) -> int:
        if self is None:
            return -1

        while index >= 0:
            if self.next is None:
                return -1
            self = self.next           
            index = index -1
        return self.value

    def insertHead(self, val: int) -> None:
        newNode = LinkedList(val)
        newNode.next = self

    def insertTail(self, val: int) -> None:
        while self.next is not None:
            self = self.next
        newNode = LinkedList(val)
        self.next = newNode

    def remove(self, index: int) -> bool:
        

    def getValues(self) -> List[int]:
        

