import time
import random
from sorting import *
from fractions import *

def insTest(alist):
    timeAvg = 0
    for i in range(10):
        start = time.time()
        insertionSort(alist)
        end = time.time()
        timeAvg += (end-start)
    print('it took', (timeAvg/10), 'seconds to sort (insertion)')
    
def bubTest(alist):
    timeAvg = 0
    for i in range(10):
        start = time.time()
        bubbleSort(alist)
        end = time.time()
        timeAvg += (end-start)
    print('it took', (timeAvg/10), 'seconds to sort (bubble)')
    
def shellTest(alist):
    timeAvg = 0
    for i in range(10):
        start = time.time()
        ShellSort(alist)
        end = time.time()
        timeAvg += (end-start)
    print('it took', (timeAvg/10), 'seconds to sort (shell)')

def selTest(alist):
    timeAvg = 0
    for i in range(10):
        start = time.time()
        selectionSort(alist)
        end = time.time()
        timeAvg += (end-start)
    print('it took', (timeAvg/10), 'seconds to sort (selection)')

def genRandomList(size):
    alist = []
    for i in range(size):
        alist.append(Fraction(random.randint(1,100), random.randint(1,100)))
    return alist[:]

#for i in range(100, 1001, 100):
    #bubTest(genRandomList(i))

#for i in range(1000, 10001, 1000):
    #insTest(genRandomList(i))

for i in range(1000, 10001, 1000):
    selTest(genRandomList(i))

#for i in range(1000, 10001, 1000):
    #shellTest(genRandomList(i))
