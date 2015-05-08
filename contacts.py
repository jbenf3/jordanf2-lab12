#!/usr/bin/python2.7

# Your Name
# Physics 91SI Spring 2013
# Lab #9, Part 2

# Contacts list reader

import sys
import os
import re


def read_contacts(file):
	"""Reads contacts from the given file object, returning them as a list."""
	# Sample regex: replace this with your own
	# don't forget the raw string r prefix!
	regex = re.compile(r"([A-Z][a-zA-Z]+,?\s[A-Z][a-zA-Z]+)\s+\((\w+@\w+\.[a-z]*)\)\s+(\(?[0-9]?\)?-?[0-9]{3}-[0-9]{4})")
	contacts = []	# Start an empty list

	for line in file:
		match = regex.match(line)
		# remember that match returns None if it doesn't match!
		if match:
			####
			# Your code goes here! (replace what's below)
			
			person = match.groups()
			# c_dict = match.groupdict()
			contacts.append(person)

	return contacts


def print_contacts(contacts):
	"""Prints contacts from a list, one per line."""
	# Pretty printing
	# See if you can figure out the formatting syntax from
	# the example below...
	for person in contacts:
		####
		# Your code goes here! (replace what's below)
		####
		last, first = person[0:2]		
		name = last.split(",")

		# This is Python's "string interpolation"
		# for C users, it's very similar to printf
		print "%s%s: %s" % (name[0], name[1], first)


def main():
	"""Read in contacts from a file, and print them to the terminal.
	Contacts are printed one per line, in the format:
	John Doe: username@domain.com

	Usage: python contacts.py filename"""

	filename = sys.argv[1]
	contacts_file = open(filename)

	# Read in contacts and print them, using above methods
	contacts = read_contacts(contacts_file)
	print_contacts(contacts)

	contacts_file.close()


if __name__ == '__main__':
	main()
