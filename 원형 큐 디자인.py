class MyCircularQueue:
    
    def __init__(self, k: int):
        self.c_queue = [0 for _ in range(k+1)]
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.c_queue[self.tail] = value
            self.tail = (self.tail+1)%len(self.c_queue)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = (self.head+1)%len(self.c_queue)
            return True
        else:
            return False
        
            
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.c_queue[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            next_tail = self.tail - 1
            if next_tail < 0:
                next_tail = len(self.c_queue)-1
            return self.c_queue[next_tail]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return ((self.tail+1)%len(self.c_queue)) == self.head
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()