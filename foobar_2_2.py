def answer(h,q):
	num_node = 2**h - 1
	num_leaf = 2**(h-1)

	tree_dict = {}
	nodes = [num_node]
	level = 1
	while len(nodes)>0:
		node = nodes.pop(0)
		left_child = node/2
		right_child = node - 1

		if left_child>0 and right_child>0:
			tree_dict[node] = {"l_child":left_child,"r_child":right_child}
			level+=1
			if level<h:
				nodes.append(left_child)
				nodes.append(right_child)
		
	
	return tree_dict



if __name__ == "__main__":

	print answer(4,10)
