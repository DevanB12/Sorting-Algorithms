import random

def mergeSort(alist):
        print("Splitting ", alist)
        if len(alist)>1:
                mid = len(alist)//2
                lefthalf = alist[:mid]
                righthalf = alist[mid:]

                mergeSort(lefthalf)
                mergeSort(righthalf)

                i=0
                j=0
                k=0
                while i < len(lefthalf) and j<len(righthalf):
                        if lefthalf[i]<righthalf[j]:
                                alist[k]=lefthalf[i]
                                i=i+1
                        else:
                                alist[k]=righthalf[j]
                                j=j+1
                        k=k+1

                while i<len(lefthalf):
                        alist[k]=lefthalf[i]
                        i=i+1
                        k=k+1

                while j<len(righthalf):
                        alist[k]=righthalf[j]
                        j=j+1
                        k=k+1
        



def ShellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        #print("\nAfter increments of size %d, the list is:"%sublistcount)
        #print(alist)

        sublistcount = sublistcount//2
        

def gapInsertionSort(alist, start, gap):

    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue



def insertionSort(alist):
    
    for index in range(1, len(alist)):
        curr = alist[index]
        pos = index

        while pos>0 and alist[pos-1]>curr:
            alist[pos]=alist[pos-1]
            pos = pos-1

        alist[pos] = curr



def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        alist[positionOfMax],alist[fillslot] = alist[fillslot], alist[positionOfMax]


def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				alist[i], alist[i+1] = \
                                          alist[i+1],alist[i]
