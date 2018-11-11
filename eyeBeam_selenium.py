#!/usr/bin/python
#
# This is a tool to take screenshot of web/url, similar as eyeWitness.
#
# by F4l13n5n0w
#
# version 1.0
#
# argparse manul: https://docs.python.org/2/library/argparse.html#choices
# Errors and Exceptions: https://docs.python.org/3/tutorial/errors.html
# Progress bar: https://github.com/verigak/progress
# Another Progress bar: https://pythonhosted.org/PyPrind/

import os
import argparse
import sys
import glob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from shutil import copyfile
from progress.bar import Bar

#is_verbose = 0
output_base = '/tmp/eyeBeam_output/'
width = '800'
height = '600'

popjs_file = 'popup.js'



def generate_report(output_path):
	copyfile('popup.js', output_path+'popup.js')
	copyfile('style.css',output_path+'style.css')

	target_html = output_path + 'report.html'
	htmlfile = open(target_html, 'w')

	htmlfile.write("<html>\n<title>eyeBeam Http(s) Screenshot report</title>\n<body>\n")
	htmlfile.write('<script type="text/javascript" src="popup.js"></script>\n')
	htmlfile.write('<LINK href="style.css" rel="stylesheet" type="text/css">\n')
	htmlfile.write('<div class="table-title">\n')
	htmlfile.write('<h3>eyeBeam Report:</h3></div>\n')
	htmlfile.write('<table class="table-fill">\n')

	file_list = glob.glob((output_path+"*.png"))

	for file in file_list:
#		url = 'http://' + file.split('/')[4].split('.')[0].replace('_','.')
		url = 'http://' + file.split('/')[4][:-4]
		htmlfile.write(('<TR><TD><div onmouseout="clearPopup()" onmouseover="popUp(event,\''+file+'\');"><img src="'+file+'" width=200 height=200/></TD>'))
		htmlfile.write(('<TD><a href="'+url+'">'+url+'</a></div></TD></TR>\n'))

	htmlfile.write('</table></body></html>')
	htmlfile.close()



def run(args):
	
	input_file = args.input.readlines()
#	device = args.device
#	output_path = output_base + device + '/'
	output_path = output_base + 'firefox/'

	try:
		os.makedirs(output_path.rstrip('/'))
	except OSError:
		print ("[!] Creation of the directory %s failed.." % output_path)
		exit(0)
	else:
		print ("Successfully created the directory %s" % output_path)

	bar = Bar('Processing', max=len(input_file), suffix='%(index)d/%(max)d')

	driver = webdriver.Firefox()

	for target_url in input_file:
		url = "http://" + target_url.strip()
		bar.next()
		driver.get(url)
		driver.save_screenshot((output_path + target_url.strip() + '.png'))
#		heimdall.png(url, device=device, width=width, height=height, save_dir=output_path)

	driver.close()

	bar.finish()
	generate_report(output_path)
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
#		parser.add_argument('-d', '--device', help='Assign which device is used, default is "Laptop"', default='Laptop', dest='device', \
#			choices=['Laptop','Desktop','iPhone','iPad','Galaxy','Surface'], required=False)
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