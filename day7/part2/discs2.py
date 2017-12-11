#!/usr/bin/env python

class Node(object):

	def __init__(self, value, weight = 0):
		self.value = value
		self.weight = weight
		self.parent = None
		self.children = []

	def __eq__(self, other):
		return self.value == other.value

	def calculate_weight(self):
		weight = 0
		current = 0
		for child in self.children:
			child_weight = child.calculate_weight()
			if current != 0 and child_weight != current:
				print child.value
				print child_weight
				print current
			current = child_weight
			weight += child_weight
		weight += self.weight
		return weight

def main():
	nodes = {}
	with open('data.txt') as f:
		lines = f.readlines()
		for line in lines:
			split = line.split(' ')
			if split[0] not in nodes:
				nodes[split[0]] = Node(split[0], int(split[1].strip('\n').strip('(').strip(')')))
			node = nodes[split[0]]
			node.weight = int(split[1].strip('\n').strip('(').strip(')'))
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
				node.calculate_weight()

if __name__ == "__main__":
	main()