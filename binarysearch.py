#BinarySearch class,
#
class BinarySearch:
	def _init_(self,a, b):
		self.a = a
		self.b = b

		length = (self.a)-1
	

def Search(item):
	count = {}

	first = 0
	last = (self.a)-1
	found = False

	while( first <= last and not found):
		mid = (first + last)//2
		if self.a[mid] == item :
			found = True
		else:
			if item < self.a[mid][mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return count



		

  