'''I will introduce the data structure called link list. It is essentially a collection of nodes
which point to the next element. The singly linked list is undirected, it is completely linear. '''
#from one import Empty

class Empty(Exception):
    def __init__(self, prompt):
        self.prompt = prompt
        super().__init__(self.prompt)
'''Doubly linked list allows for forward and backward 
navigation. There is also a circular linked list where in 
 the last element is linked to the first element. 
 single linked list has a data and link, this are 
 the constituent parts of the node. Pointers are useful
 for accessing the first nodes of a linked list.'''

# now for the linked list LIFO stack implementation.

class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

test = LinkedStack()
test.push(100)
test.push(200)
#print(test.top())
'''The Node class is representitive of
a singly linked node. The initial 
head is null with the size being 0 
it is when the push function is called
when the head private variable is set to be an
instance if the node class. the variable size
is also increased, this is necessary for the length 
function. The the top function returns the
head element variable, since it is the elements 
of elements and next, next is set to the head, and returned 
this is essentially sets the n-1 head as the nth head'''

# there is also the queue implementation of the singly linked list

class LinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next



    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
         raise Empty("Queue Is Empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue Is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None

        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


'''This is essentially a queue data structute that is representative 
of the linked list, where dequeue and enqueue are added and removing 
nodes. '''

# I will now introduce the circular linked list, where the last node is not null and points to the beginning

class CircularQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue Is Empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue Is Empty")
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

'''This is the queue implementation of the circular linked 
list, it is somewhat self explanatory, however each enqueue
of some new node needs to have the circulation property be initialized 
this is represented as the newest variable, which points to the next 
head, each new node points to a head with the newst node becoming a tail
this allows the last node to point to the last element thus creating a circular 
linked list. '''

if __name__ == '__main__':
    tester = CircularQueue()
    tester.enqueue(100)
    tester.enqueue(200)
    tester.enqueue(300)

# I will now introduce the doubly linked list
class _DoublyLinkedBase:
    class _Node:
        __slots__ = "_element", "_next", "_prev"
        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDequeue(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty('Deque Is Empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque Is Empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque Is Emtpty')
        return self._delete_node(self._header._next)



'''if __name__ == '__main__':
    tester = LinkedDequeue()
    tester.insert_first(100)
    tester.insert_last(200)
    tester.insert_last(300)
    print(tester.first())'''

'''The positional list allows for the abstraction of position 
within our doubly linked list, this allows for modifications of the
linked list in regards to nodal position. '''

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)


    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

'''There is another algorithm called insertion sort algorithm, essentially it sorts a list into ascending order based on 
comparisons to the next value, if the one to the right is larger it swaps, this process eventually leads to a 
sorted list'''

def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

# I will omit favorites list and favorites list mtf









