#!/usr/bin/python2.7

# Jordan Friedlnad
# Physics 91SI Spring 2015
# Lab #12

# Contacts list reader

import sys
import os
import re


def read_contacts(file):
	"""Reads contacts from the given file object, returning them as a list."""
	regex = re.compile(r"([A-Z][a-zA-Z]+,?\s[A-Z][a-zA-Z]+)\s+\((\w+@\w+\.[a-z]*)\)\s+(\(?[0-9]?\)?-?[0-9]{3}-[0-9]{4})")
	contacts = []

	for line in file:
		match = regex.match(line)
		if match:
			person = match.groups()
			contacts.append(person)
	return contacts


def print_contacts(contacts):
	"""Prints contacts from a list, one per line."""
	for person in contacts:
		last, first = person[0:2]		
		name = last.split(",")
		print "%s%s: %s" % (name[0], name[1], first)


def main():
	"""Read in contacts from a file, and print them to the terminal.
	Contacts are printed one per line, in the format:
	John Doe: username@domain.com

	Usage: python contacts.py filename"""

	filename = sys.argv[1]
	contacts_file = open(filename)
	contacts = read_contacts(contacts_file)
	print_contacts(contacts)

	contacts_file.close()


if __name__ == '__main__':
	main()
