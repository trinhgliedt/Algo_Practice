class OrderedList:
    def __init__(self):
        self.head = None

def is_empty(self):
        return self.head == None
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

# • Queues can assist in the construction of timing simulations.
# • Simulations use random number generators to create a real-life situation and allow us to
# answer “what if” types of questions.
# • Deques are data structures that allow hybrid behavior like that of stacks and queues.
# • The fundamental operations for a deque are add_front, add_rear, remove_front, remove_
# rear, and is_empty.
# • Lists are collections of items where each item holds a relative position.
# • A linked list implementation maintains logical order without requiring physical storage
# requirements.
# • Modification to the head of the linked list is a special case.