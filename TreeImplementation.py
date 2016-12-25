class Tree:
	def __init__(self, data, left = None, right = None):
		self.val = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)

def total(tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.val	

def printPostOrderTraversal(tree):
	if tree == None: return
	printPostOrderTraversal(tree.left)
	printPostOrderTraversal(tree.right)
	print tree.val,

def printInOrderTraversal(tree):
	if tree == None: return
	printInOrderTraversal(tree.left)
	print tree.val,
	printInOrderTraversal(tree.right)

def printPreOrderTraversal(tree):
	if tree == None: return
	print tree.val,
	printPreOrderTraversal(tree.left)
	printPreOrderTraversal(tree.right)
# for an expression 1 + 2 * 3
def getTotalOfExpression():
	tree = Tree(1, Tree(2), Tree(3))
	print total(tree)		

def printTraversals():
	tree = Tree('+', Tree(1), Tree('*',Tree(2),Tree(3)))
	printPostOrderTraversal(tree)
	#Newline for better output representation
	print
	printInOrderTraversal(tree)
	print
	printPreOrderTraversal(tree)

def getTokenlist(expr):
	l = list(expr)
	new_list = []
	for value in l:
	    if value.isdigit():
	    	new_list.append(int(value))
	    else:
	    	new_list.append(value)	
	new_list.append('end')    	
	return new_list

def get_token(tokenList, expected):
	if tokenList[0] == expected:
		del tokenList[0]
		return True
	else:
		return False	

def get_number(tokenList):
	if get_token(tokenList,'('):
		x = get_sum(tokenList)
		if not get_token(tokenList,')'):
			raise 'Missing Parentheses'
		return x
	else:
		x = tokenList[0]
		if type(x)!=type(0): return None
		tokenList[0:1] = []
		return Tree(x,None,None)	

def get_sum(tokenList):
	a = get_product(tokenList)
	if get_token(tokenList,'+'):
		b = get_sum(tokenList)
		return Tree('+',a,b)
	else:
		return a	

def get_product(tokenList):
	a = get_number(tokenList)
	if get_token(tokenList,'*'):
		b = get_product(tokenList)
		return Tree('*',a,b)
	else:
		return a		
#Function Calls	
getTotalOfExpression()
printTraversals()
token_list = getTokenlist("(3+7)*9")
token_list1 = [9, '*', '(', 11, '+', 5, ')', '*', 7, 'end']
tree = get_sum(token_list1)
printPostOrderTraversal(tree)
