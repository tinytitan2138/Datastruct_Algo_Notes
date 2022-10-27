'''You can use classes to create abstractions of data themselves, such as iterables.
a data strucutre is just a way to organize and access data, algorithms are just step-by-step
instruction given a finite time'''
import time
import functools
import sys
import ctypes
def ExperimentalTime(algo):
    @functools.wraps(algo)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        rv = algo(*args, **kwargs)
        t2 = time.time()
        print(f"Finished in {t2-t1} seconds")
        return rv
    return wrapper

@ExperimentalTime
def testalgo(x, y):
    z = x^2 + y^2
    k = x + y
    return z, k

print(testalgo(5,5))
# You can use the time module to make experimental approximations for time complexity, simply vary the input size
# and graph the different times, and boom, you have an approximate big O value.

# I will now detail the most import functions
'''f(n) = c constant, x = log_b n or b^x = n the log function, f(n) = n the linear function,
 f(n) = nlog(n) the n log n function, f(n) = n^2 the quadratic function, f(n) = n^3 the cubic function,
 f(n) = a_0 + a_1n + a_2n^2 + ... + a_dn^d' the polynomial function, f(n) = b^n the exponential function
 actual big O functions are approximate by just eyeballing the amount of primite operations 
for some input size n, you are chaterizing O based on the term with the largest effect, so 
you ignore other terms and even leading coefficients. You can also use big Omega notation to describe
fucntions of greater than size, and big Theta to describe equal rates. All of these are Asymptotic approaches.
different complexcities can be directly compared with tables through something called comparative analysis'''


def Count(list):
    count = 0
    for ele in list:
        count = count + ele
    print(count)
Count(otherlist := [1,2])
#O(n)

def Mult(Strl):
    emp = ""
    for i in Strl:
        for j in i:
            emp = emp + j

    return emp

print(Mult(string := ["hello", "world"]))
#O(n^2)

class factorialValueError(Exception):
    def __int__(self, prompt):
        super.__init__(prompt)
        #return self.message

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        raise factorialValueError("Input something greater than 0")
    else:

        return n * factorial(n-1)


print(factorial(3))
#an example of a properly defined recursive function.
'''Recursive functions are properly defined if they have initial conditions, this essentially 
builds a type of tree that calls back to the initial conditon, allowing for the implementation 
of self referanced functions'''

def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

'''this is the recursive binary search algorithm, it works by taking in some sorted list and then
starting with the middle value, if the middle value is greater than the target value it recures backwards,
or forwards if its less, or returns it if it is the target value, this has log(n) time complexity'''
mydata = [1,5,2,3,8,7,9,6,4,0, 10]
mylist = sorted(mydata)
print(binary_search(data= mylist, target=10, low=0, high=len(mylist) - 1))
'''it is useful to describe file systems with recursion as their structure is fundamentally 
self referenced. It should be noted that induction and the functions commonly seen in induction 
problems are quite useful when analyzing algorithms with big O. So you take cases where n = 1, 2, 4, etc
and arrive at lets say the geometric summation, which would be exponentially complex, which is insanely
ineffecient. '''
class fibTermException(Exception):
    def __int__(self, prompt):
        super.__init__(prompt)


def fib_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise fibTermException("You must input a value that is above 0")
    else:
        return fib_1(n-2) + fib_1(n-1)

print(fib_1(5))
# this implimintation is quite complex
'''taking n = 3, it cycles to 2 then to 1, however, each step itself is a cycle, therefor it is additive 
from the initial values, getting exponential time complexity '''

def fib_2(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = fib_2(n-1)
        return (a+b, a)

print(fib_2(3))

'''fib 2 is much better as it utilizes linear recursion, only calling itself once, allowing for a 
better time complexity'''

print(sys.getrecursionlimit())

'''• If a recursive call starts at most one other, we call this a linear recursion.
• If a recursive call may start two others, we call this a binary recursion.
• If a recursive call may start three or more others, this is multiple recursion.'''

#194
def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * power(x, n-1)


#O(n) time complex power function
'''There are binary recursive algorithms in which there are 2 traces for the recursive call 
'''
def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

print(binary_sum(list := [1,2,3,4,5,6,7,8,9,10], 0, 10))
'''This is an example of a binary recursive function, it uses the binary recursive call
to sum up the elements in the list given some indices'''

'''There are also multiple recursion algorithms that call more than twice'''

'''In general, an algorithm that uses recursion typically has the following form:
• Test for base cases. We begin by testing for a set of base cases (there should
be at least one). These base cases should be defined so that every possible
chain of recursive calls will eventually reach a base case, and the handling of
each base case should not use recursion.
• Recur. If not a base case, we perform one or more recursive calls. This recursive step may involve a test that decides which of several possible recursive
calls to make. We should define each possible recursive call so that it makes
progress towards a base case.'''

'''A good way to design recursive functions is by parameterizing it, that is different aspects
of the algorithms are represented trough variables, like binary search being parameterized into 
start mid target data, as opposed to target and data'''

'''You can elimate recursion within recursive functions by making them iterable, though that can usually
only be done if the final return statement doest referance itself'''




'''As useful array concept is that of the dynamic array, it is to be implemented 
by hand but the property of its size can be changed at runtime, hence the name'''
class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("Invalid Index")
        return self._A[k]

    def append(self, object):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = object
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

# This is a dynamic array
# A is current memory, n is number of elements, capacity is maximum elements that can be stored
# rezise just rezises the dynamic array object, the make array function just returns an array of size n
# Amortizatition analysis is just analyzing space complexity approximately, interestingly enough, the append class is O(1)
# It should be noted that the list class in python employs dynamic arrays.
#name = "solomon"
#age = 16
#tuple = "({0}, {1})".format(name, age)
#print(tuple) Implement in class to format strings

def insertion_sort(A):
    global cur, k
    for k in range(1, len(A)):
        cur = A[k]

        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1

        A[j] = cur
'''This insertion sort algorithm takes some list with an abritirary length and then sorts it in 
a non descending order'''
insertion_sort(mylist := [10,9,8,7,6,5,4,3,2,1,0,-1])
print(mylist)
#239
mylist = [[1,0,0], [0,1,0], [0,0,1]]
# 3x3 identity matrix
print([[0] * 6] * 3)
#3x6 matrix

#250

'''There are different types of data structures that one may implement, one such data structure is the
stack. The stack follows first in last out, that is, the first element put into the stack
is the last one removed or popped. '''
class Empty(Exception):
    def __init__(self, prompt):
        self.prompt = prompt
        super().__init__(self.prompt)



class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

#if __name__ == '__main__':
 #   raise Empty("Test Complete")

'''The above class is a basic implementation of the stack data structure, we are using the python 
list class as storage, we will recall that the list object is a dynamic array. init just creates 
an empty stack, is empty returns a boolean value, top returns the last element, push and pop are 
self explanatory '''
myStack = ArrayStack()
for i in range(1, 11):
    myStack.push(i)

print(myStack.top())
'''Any program that encorporates first in last out ought to use a stack data type, one good example
is any type of reverse functionality, like that present in undo buttons. '''

'''Another type of data structure is the queue, the queue follows the first in fist in first out
principle, that is, the first element added to a queue is the first one popped. '''

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue Is Empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue Is Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0



'''This is the implementation of the queue data structure within python 
Init creates an empty queue, len return teh length, is empty is a boolean
first returns the first value, and dequeue removes the first element. Queues are 
good for things like responding to requests and such'''

myQueue = ArrayQueue()
for i in range(1, 11):
    myQueue.enqueue(i)

print(myQueue.first())
