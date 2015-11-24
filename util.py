import os
from io import open

def loadFile( file_ ):
	with open( file_) as f:
		return [item[1] for item in enumerate(f)]

def saveFile( fname, file_ ):
	with open( fname, 'wb' ) as f:
		for item in file_:
			f.write( '{0}\n'.format(item) )

def writeDir( path ):
	try:
		if not os.path.exists(path):
			os.makedirs(path)
	except OSError:
		print('OSError')
