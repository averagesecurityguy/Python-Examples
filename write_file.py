#-----------------------------------------------------------------------------
# This example will open a file and read it line by line, process each line,
# and write the processed line to standard out.
#-----------------------------------------------------------------------------

# Open a file for writing
outfile = open('jenny.txt', 'w')

# Create some data to write to a file. Need some numbers, text and a list
num = 867
num2 = 5309
txt = 'Jenny'
txt2 = 'Tommy Tutone'
list = ['Everclear', 'Foo Fighters', 'Green Day', 'Goo Goo Dolls']

outfile.write('%d-%d/%s was sung by %s\n' % (num, num2, txt, txt2))
outfile.write('and was covered by:\n')

for l in list:
    outfile.write('%s\n' % (l))

# Close the file because we are done with it.
outfile.close()