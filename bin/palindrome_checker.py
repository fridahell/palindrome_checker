#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import re

def main():
	try:
		# If called without arguments, get string on standard input.
		if len(sys.argv) == 1:
			# Set string variable to first command line argument
			string = str(raw_input("Enter string to check: "))
		# Otherwise, make sure the program is called with exactly one argument.
		# sys.argv is the number of args + 1 because
		# the program's name is in sys.argv[0]
		elif len(sys.argv) != 2:
			print "invalid arguments (%d), usage: %s [string]" % (len(sys.argv), sys.argv[0])
			return 1
    	
    	
		# Compile regex matching digits, punctuation characters and blanks.
		special_characters = re.compile( '[,;.:_!?0-9 -]+')
    	
		# Remove special characters from string and set our string varialble
		# to the resulting string returned.
		string = special_characters.sub( '', string)
    	
		# Because the lower() method does not support unicode,
		# remove any non supported characters before comparing.
		invalid_characters = re.compile( '[^a-zA-Z]')
    	
		# Replace invalid characters with a dot character.
		string = invalid_characters.sub( '.', string)
    	
		# Convert all upper case characters to lower case.
		string = string.lower()
    	
		# Reverse string.
		reversed_string = string[::-1]
    	
		# Check if string is equal to the reversed string.
		if reversed_string == string:
			# The string is a palidrome.
			print "yes"
		else:
			# The string is not a palidrome.
			print "no"
		return 0
	except:
		print "unknown error, usage: %s [string]" % sys.argv[0]
		return 2

sys.exit(main())
