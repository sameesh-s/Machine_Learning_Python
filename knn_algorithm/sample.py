import math

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
def most_common(lst):
    return max(set(lst), key=lst.count)

num = raw_input().split()
num = [int(x) for x in num]

with open("dataset.txt") as textFile:
	lines = [line.split(',') for line in textFile]
length=lines.__len__()

n = 3#number of nighbours

neighbour = [[89563245.0 for x in range(n)] for x in range(2)]
top = 2

print neighbour

print "Length of training set :"+ str(length)
for i in range(len(lines)):
	lines[i][3]=lines[i][3].strip('\n')
	lines[i] = [int(numeric_string) for numeric_string in lines[i]]
	print lines[i]
	print "Distance class"
	distance = euclideanDistance(num, lines[i], 3)
	clas=lines[i][3]
	print distance,clas
	top = 2
	print top
	print distance <=neighbour[0][top] and top > -1
	while ( distance <= neighbour[0][top] and top > -1 ):
		top=top-1
	top=top+1
	while(top < n):
		#swap element
		tempD=neighbour[0][top]
		tempC=neighbour[1][top]
		neighbour[0][top]=distance
		neighbour[1][top]=clas
		distance=tempD
		clas=tempC
		top = top + 1
		print "inside while"
		print neighbour
print most_common(neighbour[1])
