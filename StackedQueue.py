class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Stack()
        self.queue_reverse = Stack()
        self.len = 0
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.push(x)
        for i in range(self.len):
            v = self.queue_reverse.pop()
            self.queue.push(v)
        self.queue_reverse.push(x)
        for i in range(self.len):
            v = self.queue.pop()
            self.queue_reverse.push(v)
        self.len += 1
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.len -= 1
        return self.queue_reverse.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue_reverse.top()
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.len == 0:
            return True
        else:
            return False

class Stack(object):
    def __init__(self):
        self.stack = []
        self.len = 0
        
    def push(self,x):
        self.stack.append(x)
        self.len += 1
        
    def pop(self):
        self.len -= 1
        return self.stack.pop()
        
    def top(self):
        return self.stack[self.len - 1]
    
    def size(self):
        return self.len
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
