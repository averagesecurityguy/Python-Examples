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
# Open a file for reading
infile = open('infilename.txt', 'r')

for line in infile:
    # Strip any line endings from the line(\r, \n, or \r\n) then process the
    # line using the process_line function
    data = process_line(line.rstrip('\r\n'))

    # Write the processed line to standard out.
    print data

# Close the file because we are done with it.
infile.close()