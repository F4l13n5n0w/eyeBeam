#!/usr/bin/python

import glob


output_path = '/tmp/eyeBeam_output/Laptop/'

copyfile('/root/myCodes/eyeBeam/popup.js', output_path)
copyfile('/root/myCodes/eyeBeam/style.css',output_path)

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
	print file
	htmlfile.write(('<TR><TD><img src="'+file+'" width=200 height=200/></TD>'))
	htmlfile.write(('<TD><div onmouseout="clearPopup()" onmouseover="popUp(event,\''+file+'\');">'))
	htmlfile.write(('<a href="http://test.com">http://test.com/</a></div></TD></TR>\n'))

htmlfile.write('</table></body></html>')
htmlfile.close()