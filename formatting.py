import os
import psutil
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter 
from io import open
import encoding
import sampling
import util
import buildTesting as build


def process(args):
	f = util.loadFile(args.input)
	output_dir = './output'
	if args.output:
		output_dir = args.output

	util.writeDir(output_dir)
		
	
	#encoding
	print('---encoding')
	e = encoding.encode(f, args.token)
	userID = e.get_userID()
	itemID = e.get_itemID()
	adjlist = e.get_adjlist()
	user_train, item_train, value_train = e.output4FM()
	
	if args.format == 'FM': 
		if args.sampling == True:
			#zero sampling
			print('---Zero samping')
			zero_user, zero_item, zero_value = sampling.get_zero( sampling.zeroSampling(adjlist) )
			user_train.extend(zero_user)
			item_train.extend(zero_item)
			value_train.extend(zero_value)


		#Testing
		print('---Create Testing Data')
		test_user, test_item, test_value = build.build(len(userID), len(itemID))

	#save
	print('---Save')
	util.saveFile('{0}/userID'.format(output_dir), userID)
	util.saveFile('{0}/itemID'.format(output_dir), itemID)

	if args.format == 'deepwalk-bipartite':
		#deepwalk
		util.saveFile('{0}/adjlist'.format(output_dir), adjlist)
	elif args.format == 'FM':
		#FM
		util.saveFile('{0}/rel-user'.format(output_dir), ['0 {0}:1'.format(i) for i in range(len(userID))])
		util.saveFile('{0}/rel-item'.format(output_dir), ['0 {0}:1'.format(i) for i in range(len(itemID))])
		util.saveFile('{0}/rel-user.train'.format(output_dir), user_train)
		util.saveFile('{0}/rel-item.train'.format(output_dir), item_train)
		util.saveFile('{0}/ans.train'.format(output_dir), value_train)
		util.saveFile('{0}/rel-user.test'.format(output_dir), test_user)
		util.saveFile('{0}/rel-item.test'.format(output_dir), test_item)
		util.saveFile('{0}/ans.test'.format(output_dir), test_value)

def main():
	parser = ArgumentParser('formatting', formatter_class=ArgumentDefaultsHelpFormatter)
	
	parser.add_argument( '--input', nargs='?', required=True, help='input file')
	parser.add_argument( '-f', '--format', choices=['FM', 'deepwalk-bipartite'], help='output format' )
	parser.add_argument( '-s', '--sampling', action='store_true')
	parser.add_argument( '-t', '--token', help='split token')
	
	parser.add_argument( '-o', '--output', help='the directory of output files')
	args = parser.parse_args()

	process(args)

if __name__ == '__main__':
	sys.exit(main())
