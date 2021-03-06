#!/usr/bin/env python

import sys

def main():
	total = None

	for line in sys.stdin:
		values = list(map(float, line.split()))
		if total is None:
			total = values
		else:
			for i in range(len(values)):
				total[i] += values[i]
	if total is not None:
		print ('\t'.join(map(lambda x: str(x / total[0]), total[1:])))
	else:
		print (0)
		
if __name__ == '__main__':
	main()

