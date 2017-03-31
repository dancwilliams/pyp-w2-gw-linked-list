from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for elem in elements:
                self.append(elem)        

    def __str__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        self.current = self.start
        return self
        
    def __next__(self):
        if not self.current:
            raise StopIteration()
            
        num = self.current
        self.current += 1
        
        return num

    __next__ = next

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        node_a = self.start
        node_b = other.start

        while True:
            if not node_a and not node_b:
                return True

            if not bool(node_a) or not bool(node_b):
                return False

            if node_a.elem != node_b.elem:
                return False

            node_a = node_a.next
            node_b = node_b.next    

    def append(self, elem):
        placeholder = Node(elem)
        
        if self.start is None:
            self.start = placeholder
            self.end = self.start
        else:
            self.end.next = placeholder
            self.end = placeholder


    def count(self):
        counter = 0
        
        
        
        '''
        for _ in self:
            counter += 1
        '''
        return counter

    def pop(self, index=None):
        pass
'''
class Book(object):
    self.value = 'x'
pass


placeholder = Node(value)
self.end.next = placeholder
self.end = placeholder
'''
