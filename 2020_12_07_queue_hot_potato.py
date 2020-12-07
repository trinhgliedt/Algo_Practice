class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def printQueue(self):
        for item in self.items:
            print(item)

# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# q.dequeue()
# q.printQueue()

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 1))
print(hot_potato(["Bill", "David", "Susan"], 1))

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