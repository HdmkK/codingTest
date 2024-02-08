class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.max_size = k
        self.cur_size = 0

    def insertFront(self, value: int) -> bool:
        
        #큐에 여유공간 있다면
        if not self.isFull():

            #새로운 노드 생성
            new_node = Node(value)

            #큐가 비었을 때
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
                
            #큐가 비지 않았을 때
            else:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
            
            self.cur_size+=1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        #큐에 여유공간 있다면
        if not self.isFull():

            #새로운 노드 생성
            new_node = Node(value)

            #큐가 비었을 때
            if self.isEmpty():
                self.head = new_node
                self.tail = new_node
                
            #큐가 비지 않았을 때
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            
            self.cur_size+=1
            return True
        else:
            return False


    def deleteFront(self) -> bool:
        
        #큐가 비지 않았다면
        if not self.isEmpty():

            #큐 사이즈 1
            if self.cur_size == 1:
                self.head = None
                self.tail = None
                

            #큐 사이즈 > 1
            else:
                self.head = self.head.next
                self.head.prev.next = None
                self.head.prev = None

            self.cur_size-=1
            return True
        else:
            return False
                


    def deleteLast(self) -> bool:
        
        #큐가 비지 않았다면
        if not self.isEmpty():

            #큐 사이즈 1
            if self.cur_size == 1:
                self.head = None
                self.tail = None
                

            #큐 사이즈 > 1
            else:
                self.tail = self.tail.prev
                self.tail.next.prev = None
                self.tail.next = None

            self.cur_size-=1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.head.value
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.tail.value
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.cur_size == 0
        

    def isFull(self) -> bool:
        return self.cur_size == self.max_size
         

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()