import math
import os
import random
import re
class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item) 

    def pop(self):
        if len(self._stack) == 0:
            return None 
        return self._stack.pop()

    def peek(self):
        l = len(self._stack)
        if l == 0:
            return None
        return self._stack[l-1]
    def size(self):
        return len(self._stack)

def isBalanced(s):
    stack = Stack()
    for bracket in s:
        if bracket in ['(', '[', '{']:
            stack.push(bracket)
        else:
            rbracket = bracket
            lbracket = stack.pop()

            if not (lbracket == '(' and rbracket == ')') and \
                not (lbracket == '[' and rbracket == ']') and \
                not (lbracket == '{' and rbracket == '}'):
                return 'NO'

    if stack.size() > 0:
        return 'NO'

    return 'YES'
