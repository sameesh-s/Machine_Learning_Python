import math

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)




with open("dataset.txt") as textFile:
	lines = [line.split(',') for line in textFile]
print lines[0][0]
length=lines.__len__()
print "Length of training set :"+ str(length)
for i in range(len(lines)):
	lines[i][3]=lines[i][3].strip('\n')
	train_point = [int(numeric_string) for numeric_string in lines[i]]
	print train_point
print lines


#data1 = [2, 2, 'a']
#data2 = [4, 4, 'b']
#distance = euclideanDistance(data1, data2, 2)
#print 'Distance: ' + repr(distance)
