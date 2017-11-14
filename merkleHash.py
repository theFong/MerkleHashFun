import hashlib 

		
def ceiling(x,y):
	return -(-x/y)

# in place merkle hash -> but whats the point might as well hash entire file and compare
# [1H,2H,3H,4H,5H,6H,7H,8H,9H] 9
# [1H2HH,3H4HH,5H6HH,7H8HH,9H|...] 5
# [1H2HH3H4HHH,5H6HH7H8HHH,9H|...] 3
# [1H2HH3H4HHH5H6HH7H8HHHH,9H|...] 2
# [1H2HH3H4HHH5H6HH7H8HHHH9HH|...] 1
def inLineMerkleHash(inData):
	data = list(inData)
	r = len(data)
	for i in xrange(0,r):
			h = hashlib.md5()
			h.update(data[i])
			data[i] = h.hexdigest()

	end = len(data)
	r = ceiling(r,2)
	while r > 1:
		for i in xrange(0,r):
			h = hashlib.md5()
			h.update(data[2*i])
			if 2*i+1 < end:
				h.update(data[2*i+1])
			data[i] = h.hexdigest()
		end = ceiling(end,2)
		r = ceiling(r,2)
		
	return data[0]

def proofOfConcept():
	data1 = ['1','2','3','4','5','6','7','8','9']
	data2 = ['1','2','3','4','4','6','7','8','9']
	data3 = ['2','1','3','4','5','6','7','8','9']
	print(inLineMerkleHash(data1) == inLineMerkleHash(data1))
	print(inLineMerkleHash(data1) == inLineMerkleHash(data3))
	print(inLineMerkleHash(data2) == inLineMerkleHash(data1))

def binaryMerkleTree(inData):
	data = list(inData)
	
