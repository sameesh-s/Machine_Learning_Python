import math

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


num = raw_input().split()
num = [int(x) for x in num]

with open("dataset.txt") as textFile:
	lines = [line.split(',') for line in textFile]
print lines[0][0]
length=lines.__len__()
print "Length of training set :"+ str(length)
for i in range(len(lines)):
	lines[i][3]=lines[i][3].strip('\n')
	lines[i] = [int(numeric_string) for numeric_string in lines[i]]
	print lines[i]
	distance = euclideanDistance(num, lines[i], 4)
	print distance

