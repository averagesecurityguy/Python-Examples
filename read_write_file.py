#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will open a file and read it line by line, process each line,
# and write the processed line to a file.
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
infile = open('infilename.txt', 'r') # Open a file for reading
outfile = open('outfilename.txt', 'w') # Open a file for writing

for line in infile:
    # Strip any line endings from the line(\r, \n, or \r\n) then process the
    # line using the process_line function
    data = process_line(line)

    # Write the processed line to a file
    outfile.write(data)

# Close the files because we are done with them.
infile.close()
outfile.close()    