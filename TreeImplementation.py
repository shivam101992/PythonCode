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

#Function Calls	
getTotalOfExpression()
printTraversals()