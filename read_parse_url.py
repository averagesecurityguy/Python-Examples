#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will read in a URL and parse the contents.
# Be aware that URL handling is one of those things that
# has changed drastically between Python 2 and 3.
#
# The HTMLParser is Python's built-in library. 
# It's not that great...and tedious. 
# BeautifulSoup is a good option if you need an environment
# where only pure Python (lxml is done partially in C) is allowed (Google App Engine),
# but let's use lxml. It's fast and easy (insert joke here).
# You can install lxml by running the following command
# in the terminal on almost any UNIX/UNIX-like machine: 
#
# sudo easy_install --allow-hosts=lxml.de,*.python.org lxml
#
# If you have issues with that or you are on Windows see this for guidance:
# http://lxml.de/index.html#download
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
import lxml.html
import urllib


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
# The URL we want to parse.
URL_TO_PARSE = "http://www.reddit.com"

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
