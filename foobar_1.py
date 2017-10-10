def answer(data,n):
	occ_hash = {}
	for element in data:
		if element in occ_hash:
			continue
		else:
			count = data.count(element)
			occ_hash[element] = count
		
	for key, value in occ_hash.iteritems():
	
		if value > n:
			for i in range(value):
				data.remove(key)
			


	return data

if __name__ == "__main__":
	data = [5,10,15,10,7]
	n = 1

	print answer(data,n)
