#P2
#Mars Li
#Feb.28.2020
#10:00


class node:
	def __init__(self,data,nextpointer = None):
		self.data = data
		self. nextpointer = nextpointer

	def getData (self):
		return(self.data)

	def setData(self,newData):
		self.data = newData

	def getNextpointer (self):
		return(self.nextpointer)

	def setNextpointer (self,newNextpointer):
		self.nextpointer = newNextpointer

class linkList:
	def __init__ (self, size= 0, head = None, tail = None):
		self.size = size
		self.head = head
		self.tail = tail

	def getSize (self):
		return(self.data)

	def setSize(self,newSize):
		self.data = newSize

	def getSize (self):
		return(self.head)

	def setHead(self,newHead):
		self.data = newHead

	def getSize (self):
		return(self.tail)

	def setTail(self,newTail):
		self.data = newTail

	def isEmpty(self):
		if(self.getSize()==0):
			return(True)
		return(False)

	def addNode(self,newNode):
		newNode = node(data = newNode)

		if(self.isEmpty()):
			self.setHead(newNode)
		else:
			self.setTail().setNextpointer(newNode)
			self.setTail(newNode)
			self.setSize(self.size +1)




def main():
 	linkL = linkList()
 	linkL.addNode(1000)
 	linkL.addNode(2000)
 	print(linkL.getSize())
 	linkL.addNode("American University")
if __name__ == "__main__":
	main()
