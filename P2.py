#P2
#Mars Li
#March.4.2020
#1:30h


class node:
	def __init__(self,data,nextPointer = None):
		self.data = data
		self.nextPointer = nextPointer
	

	def getData (self):
		return(self.data)

	def setData(self,newData):
		self.data = newData

	def getNextPointer (self):
		return(self.nextPointer)

	def setNextPointer (self,newNextPointer):
		self.nextPointer = newNextPointer



class linkList:
	def __init__ (self, size= 0, head = None, tail = None):
		self.size = size
		self.head = head
		self.tail = tail

	def getSize (self):
		return(self.size)

	def setSize(self,newSize):
		self.size = newSize

	def getHead (self):
		return(self.head)

	def setHead(self,newHead):
		self.head = newHead

	def getTail (self):
		return(self.tail)

	def setTail(self,newTail):
		self.tail = newTail

	def isEmpty(self):
		if(self.size == 0):
			return(True)
		return(False)	

	def addNode(self,d):
		newNode = node(data = d)

		if (self.isEmpty()):
			self.setHead(newNode)
		else:
			self.getTail().setNextPointer(newNode)
			
		self.setTail(newNode)
		self.setSize(self.size +1)
			


def main():
	linkList1 = linkList()
	print("Before adding nodes, does the linklist empty?",linkList1.isEmpty())
	linkList1.addNode(5)  
	print("After add one more node,number of nodes: ", linkList1.getSize())      
	linkList1.addNode(3)
	print("After add one more node,number of nodes: ", linkList1.getSize())
	linkList1.addNode("American University")
	print("After add one more node,number of nodes: ",  linkList1.getSize())
	print("After adding nodes, does the linklist1 still empty?",linkList1.isEmpty())
	


if __name__ == "__main__":
	main()
