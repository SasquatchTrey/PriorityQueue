from ast import Delete
from asyncio.windows_events import NULL
from collections import defaultdict
from queue import PriorityQueue
import sys
from turtle import pos, position


class heapNode():
    def __init__(self, data, pri):
        self.data = data
        self.pri = pri


class minHeap():
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [NULL]*(self.maxsize+1)
        #self.root
        self.position = {}


    def parentIndex(self,pos):
        return (pos - 1)//2

    def rightChildIndex(self,pos):
        return (2*pos)+2

    def leftChildIndex(self,pos):
        return (2*pos)+1

    def swap(self,pos1,pos2):
        node1 = self.heap[pos1]
        node2 = self.heap[pos2]

        temp = self.heap[pos1]
        self.heap[pos1] = self.heap[pos2]
        self.heap[pos2] = temp

        #index1 = self.heap.index(self.heap[pos1])
        #index2 = self.heap.index(self.heap[pos2])


        self.position[node1.data] = pos2
        self.position[node2.data] = pos1
    
    def hasParent(self,pos):
        return self.parentIndex(pos) >= 0

    def hasLeftChild(self,pos):
        return self.leftChildIndex(pos) < self.size

    def hasRightChild(self,pos):
        return self.rightChildIndex(pos) < self.size
    
    def parent(self,pos):
        return self.heap[self.parentIndex(pos)]
    
    def leftChild(self,pos):
        return self.heap[self.leftChildIndex(pos)]
    
    def rightChild(self,pos):
        return self.heap[self.rightChildIndex(pos)]
    
    def findMin(self):
        if(self.size == 0):
            raise("queue is empty")
        item = self.heap[0]
        return item.pri

    def insert(self,node):
        if(self.size >= self.maxsize):
            return
        #self.heap[self.size] = item
        self.heap[self.size] = node
        self.position.update({node.data : self.size})
        self.size += 1
        self.heapifyUp(0)
        return node
    
    def heapifyDown(self,pos):
        while(self.hasLeftChild(pos)):
            smallerChildPos = self.leftChildIndex(pos)
            if(self.hasRightChild(pos) and self.rightChild(pos).pri < self.leftChild(pos).pri):
                smallerChildPos = self.rightChildIndex(pos)
            if(self.heap[pos].pri < self.heap[smallerChildPos].pri):
                break
            else:
                self.swap(pos,smallerChildPos)
            pos = smallerChildPos


    def heapifyUp(self,pos):
        pos = self.size -1
        while(self.hasParent(pos) and self.parent(pos).pri > self.heap[pos].pri):
            self.swap(self.parentIndex(pos), pos)
            pos = self.parentIndex(pos)

    def extractMin(self):
        if(self.size == 0):
            raise("queue is empty")
        item = self.heap[0]
        self.deleteIndex(0)
        return item.data
    
    def deleteIndex(self,index):
        #toRemove = list(self.position.keys())[list(self.position.values()).index(index)]
        nodeData = self.heap[index].data
        self.heap[index] = self.heap[self.size-1]
        self.size -=1
        self.position.pop(nodeData)
        self.heapifyDown(index)
        return nodeData


    def deleteItem(self,node):
        toRemove = node.data
        index = self.heap.index(node)
        self.deleteIndex(index)
        return index
    
    def changeKey(self,node,newValue):
        index = self.heap.index(node)
        oldValue = self.heap[index].pri
        self.heap[index].pri = newValue
        if(oldValue > newValue):
            self.heapifyUp(index)
        else:
            self.heapifyDown(index)
    
    def printHeap(self):
        for i in range(0,(self.size)):
            print("parent : "+ str(self.heap[i].pri))
            if(self.hasLeftChild(i)):
                print("left child : "+ str(self.heap[2*i+1].pri))
            if(self.hasRightChild(i)):
                print("right child : "+ str(self.heap[2*i+2].pri))

                

if __name__ == '__main__':

    print("_______________________\n")
    node0 = heapNode(12,2)
    node1 = heapNode(4,1)
    node2 = heapNode(94,6)
    node3 = heapNode(17,5)
    node4 = heapNode(56,4)
    node5 = heapNode(11,3)
    node6 = heapNode(23,8)
    node7 = heapNode(35,0)
    minHeap = minHeap(8)
    minHeap.insert(node1)
    minHeap.insert(node0)
    minHeap.insert(node2)
    minHeap.insert(node3)
    minHeap.insert(node4)
    minHeap.insert(node5)
    minHeap.insert(node6)
    minHeap.insert(node7)
    minHeap.printHeap()
    print("_______________________\n")
    print("current min : " + str(minHeap.findMin()))

    print("_______________________\n")

    print("min extracted : " + str(minHeap.extractMin()))
    print("_______________________\n")
    
    minHeap.printHeap()

    print("_______________________\n")

    minHeap.changeKey(node1,9)

    print("dictionary : " , str(minHeap.position))

    print("_______________________\n")

    minHeap.printHeap()