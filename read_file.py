#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will open a file and read it line by line, process each line,
# and write the processed line to standard out.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def process_line(l):
    # Place any line processing code here.
    
    return l


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
# Open a file for reading. Use 'rb' instead of 'r' if the file is binary.
infile = open('infilename.txt', 'r')

# Processing text files by line is typical but processing binary files by line
# is not. When processing binary files use .read(), .seek(), and .tell()
for line in infile:
    # Strip any line endings from the line(\r, \n, or \r\n) then process the
    # line using the process_line function
    data = process_line(line.rstrip('\r\n'))

    # Write the processed line to standard out.
    print data

# Close the file because we are done with it.
infile.close()