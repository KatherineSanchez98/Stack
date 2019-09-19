'''
----------------------------------
#Developed by                     |
@user: Katherine Sánchez          |
#id: 201612408                    |
#e-mail: sanchezkathy29@gmail.com |
----------------------------------
This example demonstrates how to build a stack,
we only need 2 classes: 
1)Node: only has a constructor that assigns the value
to the attribute @data of the node and the link to the next
node.
2)Stack: our Stack class has 4 methods 
	2.1)push()
	2.2)peek()
	2.2)pop()
	2.2)print_list().
Finally to put our stack to the
test, we instanciate it, we add values, delete the last one and print.
'''


class Node:
	def __init__ (self, data): #constructor of class Node
		self.data = data #assign the value sent as a parameter to our class atribute
		self.next =  #initialize the pointer link to None (null)

class Stack:
	def __init__(self): 	#constructor of class Stack
		self.head = None 	# initialize our stack empty.

	#Add method
	def push(self, Current_Node): 
		if self.head is None: 			#verify if our stack is empty
			self.head = Current_Node 	#if is empty assign the first node to our head (Current_Node)
		else:
			temp = self.head 			#assign our head to temp.
			while temp.next is not None:#iterate through our list until we reach the end of it
				temp = temp.next 		#assign the pointer link of the last
			temp.next = Current_Node 	#element to our new element

	#Peek method
	def peek(self):
		if self.head is None:			#verify if our stack is empty
			print("Empty list")			#if is empty print(empty)
		else:
			temp = self.head			#assign our head to temp.
			while temp.next is not None:#iterate through our list until we reach the end of it
				temp = temp.next		#assign the pointer link of the last
			print(temp.data, end=' ')	#print our last element
			print("\n")

	#Pop method
	def pop(self):
		if self.head is None:			#verify if our stack is empty
			return
		elif self.head.next is None:	#if head next is null
			self.head = None			#assign null to head
		else:
			temp = self.head			#assign our head to temp.
			prev = self.head			#assign our head to previous.
			while temp.next is not None:#iterate through our list until we reach the end of it
				prev = temp				#assign temp to previous
				temp = temp.next		#assign the following temporary to temporary
			prev.next = None			#assign the following previous null

	#Print method
	def print_list(self):
		if self.head is None:			#verify if our stack is empty
			print("Empty list")			#if is empty print(empty)
		else:
			temp = self.head			#assign our head to temp.
			while temp.next is not None:#iterate through our list until we reach the end of it
				print(temp.data, end=' ')#print our data
				print('->', end=' ')
				temp = temp.next		#assign the following temporary to temporary
			print(temp.data, end=' ')	#print our data
			print("\n")
	

newStack = Stack()			#create a ner stack
newStack.push(Node("a"))	#add element a
newStack.push(Node("b"))	#add element b
newStack.push(Node("c"))	#add element c
newStack.push(Node("d"))	#add element d
newStack.print_list()		#print list
newStack.peek()				#peek method
newStack.pop()				#pop method
newStack.print_list()		#print list

