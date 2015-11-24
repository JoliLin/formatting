import itertools
from collections import deque


def build(numOfUser, numOfItem):
	ui = itertools.product(xrange(numOfUser), xrange(numOfItem))

	user = deque()
	item = deque()

	for element in ui:
		user.append( element[0] )
		item.append( element[1] )

	value = ['0']*(numOfUser*numOfItem)

	return user, item, value
