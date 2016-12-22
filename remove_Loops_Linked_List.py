# Node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self, node):
        temp = node
        while(temp):
            print temp.data,
            temp = temp.next

    def getHead(self):
        return self.head
        
    def createLoop(self, n):
        if n==0:
            return None
        temp=self.head
        ptr=self.head
        cnt=1
        while(cnt!=n):
            ptr=ptr.next
            cnt+=1

        while(temp.next):
            temp=temp.next
        temp.next=ptr

def removeTheLoop(head):
    l = 0
    myList = []
    isLoopExists = False
    while head:
        if head.data not in myList:
            myList.append(head.data)
            l+=1
        else:
            isLoopExists = True
        if isLoopExists:    
            break
        head = head.next
    return int(isLoopExists)

if __name__=='__main__':
    t=input()
    for i in range(t):
        n=input()
        arr=map(int, raw_input().strip().split())
        list=LinkedList()
        for i in arr:
            list.push(i)
        ele = input()
        list.createLoop(ele)
        print removeTheLoop(list.getHead())