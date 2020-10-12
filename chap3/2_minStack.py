class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        mini = min(data, self.min())
        self.stack.append((data, mini))

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()[0]

    def peek(self):
        return self.stack[-1][0]

    def min(self):
        return self.stack[-1][1] if not self.isEmpty() else float("inf")

    def isEmpty(self):
        return len(self.stack) == 0

if __name__ == '__main__':
    s = Stack()
    for i in [10, 6, 4, 2, 7, 6, 8]:
        s.push(i)

    print("Min of stack is {}".format(s.min()))
    print("Popped {}".format(s.pop()))
    print("Peeking {}".format(s.peek()))
    print("Min of stack is {}".format(s.min()))
    s.push(1)
    print("Min of stack is {}".format(s.min()))

