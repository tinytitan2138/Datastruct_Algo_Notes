'''I will not introduce the tree data type,
trees in comp sci are upside down, with the root
being the top node, each node may have children which
derive from it, it can be a leaf if it has no children
and it can have a parent node from which it is derived
from. '''
from two import LinkedQueue


class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0


# this is essentially an abstract class that describes the tree data strucuture

'''There are also binary trees which have a total of 
two children for each parent node, being divided into 
the left child or right child. Proper trees have 0 or
2 child nodes per parent node. There are also neigboring sibling nodes for every parent node
'''

class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


'''One implementation of the binary tree is that of the 
linked tree structure, such that som parent node has its adresss 
being pointed to bu its children node, and has 2 points pointing to 
its left and right child node'''

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ =  "_element", "_parent", "_left", "_right"
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child

            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t2.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)


'''if __name__ == '__main__':
    tester = LinkedBinaryTree()
    tester._add_root(100)
    tester._add_right(tester.root(), 50)
    print(tester.right(tester.root()))'''

# the code is self-explanatory but the attachment function bassicly describe a tree merger


'''The array based implementation of the binary tree was omited 
there are ways in which to search through trees such as preorder
travel which searches from root down in revursive fasion 
there is also postorder which searches revursively but instead 
starts from the bottom and works up to the root. There is also
breadth first search wich begins at depth d then searches all of the nodes
then searches at d+1. There is inorder traversal which searches at 
position p only after all its left children were searched, it essentially
searches from left to right. An interesting note is that 
binary search trees can be representitive of relational data, 
for example all the elements to the left of some node could be less than, 
where as all the elements to the right are greater than. '''

# I have implemented breadth-first search and have omitted the rest.

'''another interesting application of trees are expression
trees, where in mathematical operations can be represented with tree, 
the bottom up nature also incorporates order like pemdas. '''

'''There is another datastructure called the priority queue, 
it basically abstracts things within queue, so you may
not have something strictly of the FIFO principle, you may 
need to take certain factors and variables into account. '''
# I will omit priority queues, however, they are an important concept

'''The most effecient implementation of priority queues are with 
a datastructure called heaps, they are essentially binary trees with relational
components, that is, every position p that isnt the root has keys
that are greater than or equal to its parents, aswell, the root of
the binary tree has a minimum key value. The heapq module already
includes heap based priority queues. There is also a selection 
sort algorithm where each minimum value is placed at the beginning 
and then omitted in the comparison. Priority queues may need to 
be dynamic in deletion and insertion and thus something like locators 
is needed in order to properly find the elements in some queue without
having to do a linear search. '''

'''The dict class in python is basically a map, that is, 
it has key words with values associated with them. Most implementations of the 
map take the form of the hashtable which allows for constant time complexity 
when returning the key values. '''

'''A skip list is often implemented when doing a
search within a map, it basically randomizes the values
then uses a binary search type algorithm to search through it, 
this allows for logarithmic time complexity. '''
#481
'''Binary search trees are abstract ways in order 
to sort sorted maps, their nodes are representative of key value pairs, 
each pair to the left of some node p have key values less than that value, 
right of the node has key value pairs greater than it. '''
'''Treemap are naturally sorted by the value of the key, but not
by the values at said key themself. '''

'''Certain binary search trees may have heights proportional to 
n, thus worst case scenario is O(n), there are other 
searching algorithms which randomize the structure of the tree 
to get a worse case complexcity apporaching log(n) Rotations 
can be implemented in order to sort them, an example being trinode 
restructuring which switches parent grandparent and child nodes in such
an order that is random. One such balancing technique is the AVL tree
which garuntees that its child node at any position p differs in height by 1 
only, where height is defined as the number of nodes on the longest possible
path. '''

'''There is another technique called splaying in which the bottom most 
node that is being reffered to is moved to the top, essentially, 
the most commonly used nodes are moved to the top. '''
# There are multinodal trees with more than 2 children. Use multiway search.

'''A 2-4 tree is a tree in which all leaves have the same depth 
and all internal nodes have degree 2, 3, or 4. '''

'''There are also red-black trees that has its root being black, the child of a red
node being black, all nodes with 0 or 1 children habe the same  black depth. '''
# no children = black

'''I will introduce some sorting algorithms, these are designed in order to 
sort list in ascending order. One such algorithm is the merge sort algorithm which 
divides and conqueres the list, it constantly splits the list then sorts its constintuent parts 
then recombines them, this process is fundamentally recursive in nature. This can be applied to 
linked list and stuff like that. '''
'''There is a similar sorting algorithm folloowing 
divide and conquer called quick sort, quick sort 
 works by choosing some pivot element and dividing up arrays 
 into those less than (left) then adding them back up again, greater than values
 are placed to the right and sorted as well, for each 
 sequential array created a new pivot element in chosen. This 
 is repeated recursively until the array is sorted. '''

#583 

'''Another interesting algorithm is the pattern matching algorithm. Essentially, if you have some 
string and some pattern you may find the instances in which this pattern exists, this is represented through index 
values. One such algorithm is the Boyer-Moore alogorithm, a brute force algorithm is just an algorithm that takes up 
the possible combinations of some given data and then chooses the best possible combination depending on what you are
actually trying to do with the data. 
'''

'''A good alternative to the Boyer Moor algorithm is the Knuth-Morris-Pratt algorithm. It is essentially works 
 by calculating the highest index to shift to, it does this with something called the failure function. That is, if the 
 last index starting from the pattern is a mismatch then it is obvious that you may omit a certain number of character before 
 it. This is because knowing information from previous attempts and knowing whether some character is a match or not
 allows us to deduce information about the characters in-front of it. '''

'''There are such algorithms called greedy choice algorithms, they essentially work by creating a tree 
of optimal choices based off of some process, they either maximize of minimize some property within some structure. 
Thus greedy algorithms are usually used when you are trying to optimize something. Another way to think about them is 
the series of all optimal choices. One interesting greedy algorithm is huffman encoding. The process is lengthy but 
you are basically building a tree that is binary encoded, each subsequent node is the sum of the least 2 occurring characters
or nodes. The tree is later encoded with each left child being 0 and the right being 1. I will note that each right child
is made when you add some internal node with another character. '''


