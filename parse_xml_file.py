#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will read an XML file and parse out the data using the
# xml.dom.minidom library that is included in the standard library. 
#
# There are two methods for doing XML parsing, the DOM method loads the XML
# file into a tree structure in memory and the SAX method reads the XML file
# as a stream of text. The DOM method is fast but only works on small files
# that will fit in memory. The SAX method can work on arbitrary lenght files.
# I will be using the DOM method below because I wanted to do this tutorial
# using the tools in the standard library. There are a number of XML parsing
# options available in Python. If you plan to work with large files, or a
# large number of small files, then I would suggest looking at the lxml
# library, which is based on libxml2 and libxslt. You can get more information
# about lxml at  http://lxml.de/index.html. Other options are available at
# wiki.python.org/moin/PythonXml
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
# We need the minidom module
import xml.dom.minidom


#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def process_line(l):
    # Place any line processing code here.
    
    return l


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------

# Read in the URL you defined.
# Also note that this handles SSL as well.
geturl = urllib.urlopen(URL_TO_PARSE)

# Save the contents of the URL in its entirety for analysis.
readurl = geturl.read()

# Close geturl. We don't need it again.
geturl.close()

# We could do a lot more interesting stuff with this,
# but let's stay generic and just get all of the URLs
# from the contents.

#Parse the contents with lxml.
parse_readurl = lxml.html.fromstring(readurl)

# Select the URL in href for all a tags using XPath.
# Returns a list of URLs.
readurl_urls = parse_readurl.xpath("//a/@href")

# Since readurl_urls is a list, let's iterate 
# over it and print the URLs.
for url in readurl_urls:
    print url
