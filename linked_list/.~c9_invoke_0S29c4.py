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
        num_str = []
        for item in self:
            num_str.append(str(item))
        return '[{}]'.format(', '.join(num_str))

    def __len__(self):
        return self.count()

    def __iter__(self):
        current = self.start
        while current:
            yield current.elem
            current = current.next
        raise StopIteration
    
    '''
        self.current = self.start
        return self
        
    def __next__(self):
        
        if not self.current:
            raise StopIteration()
            
        self.num = self.current
        self.current += 1
        
        return self.num
    '''    
        
    #__next__ = next

    def __getitem__(self, index):
        
        if index > self.count() - 1:
            raise IndexError
        
        prev = None
        node = self.start
        i = 0
        
        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1
        
        return node.elem
        # Block ends here

    def __add__(self, other):
        new_list = self._
        for elem in other:
            new_list.append(elem)
        for 

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        
        if self is None or other is None:
            return False
        
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
        
        for x in self:
            counter += 1
        '''
        node_a = self.start
        while node_a is not None:
            counter += 1
            node_a = node_a.next
        '''
        return counter


    def pop(self, index=None):
        
        # If index == None, we want to remove the last node, i.e. node with
        # an index of self.count - 1 (or len(self))
        
        if self.start is None:
            raise IndexError
        
        if index == None:
            index = self.count() - 1
        
        if index > self.count() - 1:
            raise IndexError
        
        prev = None
        node = self.start
        i = 0
        
        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1
            
        if node is not None:
            value_to_return = node.elem    
        
        if prev is None:
            self.start = node.next
        else:
            prev.next = node.next
        
        return value_to_return


'''
class Book(object):
    self.value = 'x'
pass


placeholder = Node(value)
self.end.next = placeholder
self.end = placeholder
'''