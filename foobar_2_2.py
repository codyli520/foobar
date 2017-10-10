def answer(h,q):
	num_node = 2**h - 1
	num_leaf = 2**(h-1)

	nodes = [x+1 for x in range(num_node)]

	tree= {}

	while len(nodes)>2:
		node = nodes.pop()
		left_child = nodes.pop(len(nodes)/2-1)
		right_child = nodes.pop(len(nodes)-1)
		tree[node] = {"left":left_child,"right":right_child}
		
	
	return tree


if __name__ == "__main__":

	print answer(3,10)
