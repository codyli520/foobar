def answer(n,b):
	num_hash = {}

	while True:
		x = ''.join(sorted(n,reverse=True))
		y = ''.join(sorted(n))

		if x == y:
			return 1

		n = int(x,b)-int(y,b)
		s = ""
		while n:
			s = str(n % b) + s
			n /= b

		if s in num_hash:
			if num_hash[s]+1 > 2:
				break
			num_hash[s] += 1
		else:
			num_hash[s] = 1

		n = s

	count = 0
	for key,value in num_hash.iteritems():
		if value > 1:
			count +=1
	return count

if __name__ == "__main__":

	print answer("1211",10)
