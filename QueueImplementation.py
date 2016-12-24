class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

#Without the concept of keeping last index of the element of the queue
class Queue:
	def __init__(self):
		self.length = 0
		self.head = None

	def is_Empty(self):
		return self.length == 0

	def Enqueue(self,data):
		node = Node(data)	
		if self.head is None:
			self.head = node
		else:
			last = self.head
			while last.next:
				last = last.next
			last.next = node
		self.length += 1			

	def Dequeue(self):
		data = self.head
		self.head = self.head.next
		self.length -= 1
		return data


#Keeping last index of the element of the queue	

class Queue1:
	def __init__(self):
		self.length = 0
		self.head = None
		self.last = None

	def is_Empty(self):
		return self.length == 0

	def Enqueue(self,data):
		node = Node(data)	
		if self.head is None:
			self.head = node
			self.last = node
		else:
			last = self.last
			last.next = node
			self.last = node
		self.length += 1			

	def Dequeue(self):
		data = self.head.data
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.last = None
		return data