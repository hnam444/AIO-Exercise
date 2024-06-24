#Question 2
import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        ### Your Code Here
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum(dim=0)

data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[-1].item(), 2) == 0.26
output

#Question 3
import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        ### Your Code Here
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum(dim=0)

data = torch.Tensor([1, 2, 3000000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[0].item(), 2) == 0.0
output

#Question 9
class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = []

    def is_full(self):
        return len(self._stack) == self._capacity

    def push(self, value):
        if not self.is_full():
            self._stack.append(value)

stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.is_full())

#Question 10
class MyStack:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stack = []

    def is_full(self):
        return len(self._stack) == self._capacity

    def push(self, value):
        if not self.is_full():
            self._stack.append(value)

    def top(self):
        return self._stack[-1]

stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.top())

#Question 11
class MyQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = []

    def is_full(self):
        return len(self._queue) == self._capacity

    def enqueue(self, value):
        if not self.is_full():
            self._queue.append(value)

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())

#Question 12
class MyQueue:
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = []

    def isEmpty(self):
        return len(self._queue) == 0

    def is_full(self):
        return len(self._queue) == self._capacity

    def dequeue(self):
        if not self.isEmpty():
            return self._queue.pop(0)

    def enqueue(self, value):
        if not self.is_full():
            self._queue.append(value)

    def front(self):
        if not self.isEmpty():
            return self._queue[0]

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())
