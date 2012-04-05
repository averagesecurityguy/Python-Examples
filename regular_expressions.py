#!/usr/bin/env python
#-----------------------------------------------------------------------------
# This example will show the basic uses of regular expressions.
#
# A note on regular expressions from the Python Tutorial at python.org
# Regular expressions use the backslash character ('\') to indicate special 
# forms or to allow special characters to be used without invoking their 
# special meaning. This collides with Python's usage of the same character 
# for the same purpose in string literals; for example, to match a literal 
# backslash, one might have to write '\\\\' as the pattern string, because 
# the regular expression must be \\, and each backslash must be expressed as 
# \\ inside a regular Python string literal.
#
# The solution is to use Python's raw string notation for regular expression 
# patterns; backslashes are not handled in any special way in a string literal 
# prefixed with 'r'. So r"\n" is a two-character string containing '\' and 
# 'n', while "\n" is a one-character string containing a newline. Usually 
# patterns will be expressed in Python code using this raw string notation.
#
# Common regular expression patterns
# ^  - matches beginning of line
# $  - matches end of line
# .  - matches any character
# +  - match if an item occurs 1 or more times
# *  - match if an item occurs 0 or more times
# [] - match the set of characters within the braces (no escaping needed)
# \s - matches white space
# \w - matches words (lower, upper, digits, and _)
#
# Additional Resources
# http://docs.python.org/library/re.html
# http://docs.python.org/howto/regex.html
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Import any needed libraries below
#-----------------------------------------------------------------------------
# We need the re module
import re

#-----------------------------------------------------------------------------
# Place any necessary functions below this.
#-----------------------------------------------------------------------------
def print_match(m):
    # match() and search() return a MatchObject not a string. MatchObject will
    # be True if a match exists and False if it doesn't. We will print the 
    # match if it exists.
    if m:
        print m.group(0)
    else:
        print "Nothing to print."


#-----------------------------------------------------------------------------
# Begin the main program.
#-----------------------------------------------------------------------------
str1 = 'abbcccdddd'
str2 = 'How now brown cow.'
str3 = 'String of numbers: 11 22   33  44   55'

# match() only matches at the beginning of the string. It's as if you append ^
# to the beggining of your pattern. Nothing will be printed because the match
# fails.
m1 = re.match(r'bb', str1)
print_match(m1)

# This will print.
m2 = re.match(r'abb', str1)
print_match(m2)

# search() matches anywhere in the string and returns the first match found.
# Will find and print the first occurrence of 'ow'.
m3 = re.search(r'ow', str2)
print_match(m3)

# findall() returns a list containing all the matching non-overlapping strings
# find all occurrences of 'ow' in str2
m4 = re.findall(r'ow', str2)
print m4

# find all occurrences of two digits followed by one or more whitespace
# characters (space or tab).
m5 = re.findall(r'\d\d', str3)
print m5

# find all occurrences of two digits followed by one or more spaces. Capture
# the digits in a group. This will return a list of all the digits. Notice
# that 55 is not in the list because 55 is not followed by whitespace.
m6 = re.findall(r'(\d\d)\s+', str3)
print m6

# same as above but put the digits in one group and the spaces in another.
# This will return a list of tuples. Each tuple will have the digits and 
# the spaces. Again, 55 will not be in this list because it is not followed
# by whitespace.
m7 = re.findall(r'(\d\d)(\s+)', str3)
print m7
