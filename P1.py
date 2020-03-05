#P1
#Mars Li
#Feb.28.2020
#15:00


class node:
	def __init__(self,data,nextPointer = None):
		self.data = data
		self. nextPointer = nextPointer

	def getData (self):
		return(self.data)

	def setData(self,newData):
		self.data = newData

	def getNextPointer (self):
		return(self.nextpointer)

	def setNextPointer (self,newNextPointer):
		self.nextPointer = newNextPointer
		

def main():
	print("We can creat some nodes below")
	pass


if __name__ == "__main__":
	main()
