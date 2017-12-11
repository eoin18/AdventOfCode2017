#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.parent = None
		self.children = []

	def __eq__(self, other):
		return self.value == other.value

def main():
	nodes = {}
	with open('data.txt') as f:
		lines = f.readlines()
		for line in lines:
			split = line.split(' ')
			if split[0] not in nodes:
				nodes[split[0]] = Node(split[0])
			node = nodes[split[0]]
			if len(split) > 2:
				for i in range(3, len(split)):
					child_val = split[i].strip('\n').strip(',')
					if child_val not in nodes:
						nodes[child_val] = Node(child_val)
					child_node = nodes[child_val]
					node.children.append(child_node)
					child_node.parent = node
		for node in nodes.itervalues():
			if node.parent is None:
				print node.value

if __name__ == "__main__":
	main()