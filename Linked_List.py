class Node:
	def __init__(self, data=None, Next=None):
		self.data = data
		self.next = Next

	def __str__(self):
		return str(self.data)

def printList(node):
	while node:
		print node,
		node = node.next
	print	
def printBackward(list):
  if list == None: 
  	return
  head = list
  tail = list.next
  printBackward(tail)
  print head,
def deleteElement(list):
	if list==None:return
	first = list
	second = first.next
	first.next = second.next
	second.next = None
	print second

def addElement(list,x):
	nodex = Node(x)
	if list==None:return
	first = 0
	while list.next is not None:
		first = list.next
		list = first
	first.next = nodex
	nodex.next = None
def addElementAtPosition(list,x,n):
	nodex = Node(x)
	if list==None:return
	first = 0
	while list is not None and n>0:
		first = list
		list = first.next
		n-=1
	nodex.next = first.next	
	first.next = nodex

def deleteElementAtPosition(list,n):
	while list is not None and n>0:
		first = list
		list = first.next
		n-=1
	x = first.next	
	first.next = x.next
	x.next = None

node1 = Node(1)	
node2 = Node(2)
node3 = Node(3)		
node1.next=node2
node2.next=node3
#print "Printing one by one - ", node1, node2, node3
printList(node1)
#printBackward(node1)
#deleteElement(node1)
#addElement(node1,4)
#printList(node1)
#addElementAtPosition(node1,4,1)
#printList(node1)
#deleteElementAtPosition(node1,1)
#printList(node1)