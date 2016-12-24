class Stack:
	def __init__(self):
		self.items = []

	def Push(self,item):
		self.items.append(item)

	def Pop(self):
		return self.items.pop()

	def is_Empty(self):
		return(self.items == [])

def eval_postfix(expr):
	import re
	token_list = re.split("([^0-9])", expr)
	stack = Stack()

	for item in token_list:
		if item == '' or item == " ":
			continue
		if item == '+':
			sum1 = stack.Pop() + stack.Pop()
			stack.Push(sum1)
		elif item == '*':
			prod1 = stack.Pop() * stack.Pop()
			stack.Push(prod1)	
		else:
			stack.Push(int(item))
	return stack.Pop()		

t = raw_input()
print eval_postfix(t)	