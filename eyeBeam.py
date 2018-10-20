#!/usr/bin/python
#
# This is a tool to take screenshot of web/url, similar as eyeWitness.
#
# by F4l13n5n0w
#
# version 1.0


import argparse
import sys
import heimdall
from progress.bar import Bar

#is_verbose = 0
output_base = '/tmp/eyeBeam_output/'
width = '800'
height = '600'

def run(args):
	
	input_file = args.input.readlines()
	device = args.device
	output_path = output_base + device + '/'

	bar = Bar('Processing', max=len(input_file), suffix='%(index)d/%(max)d')

	for target_url in input_file:
		url = "http://" + target_url.strip()
		bar.next()
		heimdall.png(url, device=device, width=width, height=height, save_dir=output_path)

	bar.finish()
	print "[*] Finished!!"
	print "[*] Results saved in " + output_path
'''
	if args.verbose:
		is_verbose = args.verbose
		if is_verbose in range(1,3):
			print is_verbose
		else:
			print "eyeBeam: error: unrecognized arguments: -" + 'v'*is_verbose
'''


def main():
	try:
		parser=argparse.ArgumentParser(
			description='''This is a script similar function as eyewitness, but more easier.''',
			epilog="""Good luck... :P""",
			prog='eyeBeam')

		parser.add_argument('-i', '--input-file', help='Read targets from a file', type=file, dest='input', required=True)
		parser.add_argument('-d', '--device', help='Assign which device is used, default is "Laptop"', default='Laptop', dest='device', \
			choices=['Laptop','Desktop','iPhone','iPad','Galaxy','Surface'], required=False)
#		parser.add_argument('-o', '--output-path', help='Assign the path to store the screenshots (default path is "/tmp/eyeBeam_output/")', 
#			type=str, dest='output', default="/tmp/eyeBeam_output/", required=False)
		parser.add_argument('-v', '--verbose', help='Print verbose details, -vv for more debug information', dest='verbose', action='count')
		parser.add_argument('-V', '--version', help='Print current version', action='version', version='%(prog)s v1.0')

		parser.set_defaults(func=run)
		args=parser.parse_args()

		if len(sys.argv) < 2:
			parser.print_help()
		else:
			args.func(args)
	except IOError as err:
		print('Error: {0}'.format(err))
	except:
		raise
		


if __name__ == "__main__":
	main()