#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will read an XML file and parse out the data using the
# xml.etree.ElementTree library that is included in the standard library. 
#
# There are two methods for doing XML parsing, the DOM method loads the XML
# file into a tree structure in memory and the SAX method reads the XML file
# as a stream of text. The DOM method is fast but only works on small files
# that will fit in memory. The SAX method can work on arbitrary length files.
#
# I will be using Python's ElementTree module in the example below because I  
# want to use the tools in the standard library. You can get more information  
# about ElementTree at:
#         http://docs.python.org/library/xml.etree.elementtree.html, and
#         http://effbot.org/zone/element.htm
#
# There are a number of external XML parsing libraries that can be used with 
# Python. Details are available at wiki.python.org/moin/PythonXml. If you plan 
# to do a lot of XML processing, then I would suggest looking at the lxml 
# library. It is based on libxml2 and libxslt and is fast and easy to use. You 
# can get more information about lxml at http://lxml.de/index.html. 
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
# We need the ElementTree module
import xml.etree.ElementTree


#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def print_movie(movie, year):
    print "The movie \"%s\" was released in %s.\n" % (movie, year)


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------

# Load an XML file into the tree and get the root element.
xml = xml.etree.ElementTree.ElementTree(file='movies.xml')
root = xml.getroot()

# Get a list of all the movie elements in the file.
movies = root.findall('movie')

# Parse the movie element to get the "id" attribute, the title element and the 
# released element. 
for movie in movies:
    # Get the value of the "id" attribute
    id = movie.attrib['id']
    print "Parsing movie #" + id
    
    # Get the text inside the first "title" tag. Returns None if the "title" 
    # tag is not found. Returns an empty string is returned if the tag was 
    # found but no text was found in the tag.
    title = movie.findtext('title')
    year = movie.findtext('released')
    
    print_movie(title, year)

