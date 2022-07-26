"""
232. Implement Queue using Stacks
Easy

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue)
 as long as you use only a stack's standard operations.


Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
"""


class MyQueue(object):
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        n = len(self.s1)
        if n == 0:
            self.s1.append(x)
        else:
            self.s2.extend(self.s1)
            for i in range(n):
                self.s1.pop()
            self.s1.append(x)
            # print(self.s1, self.s2)
            # tmp = len(self.s2) - n + 1
            self.s1.extend(self.s2)
            for i in range(len(self.s2)):
                self.s2.pop()
            # print(self.s1, self.s2, "_____")
        return self.s1

    def pop(self):
        """
        :rtype: int
        """
        n = len(self.s1)
        if n == 0:
            return None
        front = self.s1.pop()
        return front
        # n = len(self.s1)
        # if n == 0: return None
        # self.s2.extend(self.s1[1:])
        # res = self.s1[0]
        # # self.s1.clear() # can use in python3
        # for i in range(n):
        #     self.s1.pop()
        # tmp = len(self.s2)-n+1
        # self.s1.extend(self.s2[tmp:])
        # print(self.s1, res)
        # return res

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
