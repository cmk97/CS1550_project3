#!/usr/bin/env python

import sys, getopt
from collections import OrderedDict
import math #for math.log(base, num)



# args: -n, -p, -s

def get_args():
	arguments = {}
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'n:p:s:')
	except getopt.GetoptError as e:
		print(e)
		sys.exit()

	for o, a in opts:
		print(o)
		print(a)
		try:
			if o == '-p':
				arguments['numframes'] = int(a)
			elif o == '-n':
				arguments['pagesize'] = int(a)
			elif o == '-s':
				arguments['mem_split'] = a
		except ValueError as e:
			print("Couldn't parse arg {} into integer".format(a))
			sys.exit()

	arguments['tracefile'] = sys.argv[-1]
	return arguments


def read_trace(filename):
	with open(filename) as tracefile:
		lines = []
		for line in tracefile:
			frm_data = line.strip().split()
			lines.append(frame(frm_data[0], frm_data[1], frm_data[2]))

		return lines

	


class frame(object):

	def __init__(self, mode, addr, process_id):
		self._addr_str = addr
		self._mode = mode
		self._process_id = process_id

	@property
	def addr_str(self):
		return self._addr_str

	@property
	def addr(self):
		""" returns the decimal value of the hex address"""
		return int(self._addr_str, 16)	

	@property
	def mode(self):
		return self._mode

	@property
	def process_id(self):
		return self._process_id

	def page_number(self, offset):
		return self.addr >> offset


	def __repr__(self):
		return '{} | {} | {}'.format(self.mode, self.addr, self.process_id)

	def __str__(self):
		return '{} | {} | {}'.format(self.mode, self.addr, self.process_id)

class VMSim(object):
	def __init__(self, trace):
		self.mem_trace = trace





def main():
	args = get_args()
	print(args)
	mem_trace = read_trace(args['tracefile'])
	for tr in mem_trace:
		print(tr.page_number(12), tr.addr, tr.addr_str)
		


if __name__ == '__main__':
	main()


