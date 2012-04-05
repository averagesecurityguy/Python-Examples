#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will open a file and read it line by line, process each line,
# and write the processed line to standard out.
#-----------------------------------------------------------------------------

# Open a file for writing. Use 'a' instead of 'w' to append to the file.
outfile = open('jenny.txt', 'w')

# Create some data to write to a file. Need some numbers, text and a list
num = 867
num2 = 5309
txt = 'Jenny'
txt2 = 'Tommy Tutone'
list = ['Everclear', 'Foo Fighters', 'Green Day', 'Goo Goo Dolls']

# The 2.x version of Python formats strings using the method below. The 3.x
# version of python uses .format(). The method below will be phased out of 
# python eventually but I use it here because it is compatible with Python 
# 2.x, which is the default version of python in Ubuntu and BT5.
#
# UPDATE: The .format() string formatting method is supported in Python 2.6
# and higher.
outfile.write('%d-%d/%s was sung by %s\n' % (num, num2, txt, txt2))
outfile.write('and was covered by:\n')

for l in list:
    outfile.write('%s\n' % (l))

# Close the file because we are done with it.
outfile.close()