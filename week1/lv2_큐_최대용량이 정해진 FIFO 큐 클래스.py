class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size()

    def push(self, item):
        if self.stack1.size() >= max_size:
            return False
        self.stack1.push(item)
        return True

    def pop(self):
        while self.stack1.size() > 0:
            self.stack2.push(self.stack1.pop())
        if self.stack2.size() > 0:
            item = self.stack2.pop()
            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())
            return item
        else: return False
    

n, max_size = map(int, input().strip().split(' '))
queue=MyQueue(max_size)

for i in range(n):
    order=input().strip().split(' ')
    if order[0]=='PUSH':
        print(queue.push(order[1]))
    elif order[0]=='POP':
        print(queue.pop())
    elif order[0]=='SIZE':
        print(queue.qsize())