class Fifo:
    def __init__(self):
        self._queue = []
    
    def dequeue(self):
        if len(self._queue) == 0:
            return None
        return self._queue.pop(0)
    
    def enqueue(self, item):
        self._queue.append(item)
    
    def front(self):
        if len(self._queue) == 0:
            return None
        return self._queue[0]

queue = Fifo()

data = [row.rstrip().split() for row in sys.stdin.readlines()]
queries = data[1:]

for query in queries:
    op = query[0]

    if op == '1':
        data = query[1]
        queue.enqueue(data)
    elif op == '2':
        queue.dequeue()
    elif op == '3':
        d = queue.front()
        if d:
            print(d)
