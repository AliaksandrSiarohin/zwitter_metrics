#!/usr/bin/env python3

import sys

def main():
	old_key = None
	total = 0
	for line in sys.stdin:
		key, value = line.split()
		value = int(value)
		if key != old_key:
			if old_key is not None:
				print (old_key, total)
			old_key = key
			total = 0 
		total += value
	print (old_key, total)

if __name__ == '__main__':
	main()
