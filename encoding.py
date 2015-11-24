from collections import defaultdict, deque

class encode:
	def __init__(self, uilist, token=' '):
		self.uilist = uilist
		self.token = token
		self.adjlist = defaultdict(list)
		self.userID = []
		self.itemID = []
		self.relUser = deque()
		self.relItem = deque()
		self.relValue = deque()
		self.encode()


	def encode(self):
		for item in self.uilist:
			s = item.split( self.token )
				
			if s[0] not in self.itemID:
				self.itemID.append(s[0])

			if s[1].strip() not in self.userID:
				self.userID.append(s[1].strip())
			
			self.adjlist[self.userID.index(s[1].strip())].append(self.itemID.index(s[0]))
			self.relUser.append(self.userID.index(s[1].strip()))
			self.relItem.append(self.itemID.index(s[0]))
			self.relValue.append(s[2].strip())
		
	def get_userID(self):
		return self.userID
	
	def get_itemID(self):
		return self.itemID

	def get_adjlist(self):
		return ['{0} {1}'.format(key, ' '.join(map(str, self.adjlist.get(key)))) for key in self.adjlist.keys()]

	def output4FM(self):
		return self.relUser, self.relItem, self.relValue 
