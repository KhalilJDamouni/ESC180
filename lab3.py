import lab3_utilities

def rotate_90_degrees(image_array, direction):
	'''
	Given an square image array (rgb or grayscale) and a direction, 
	this function returns a 90-degree rotated image.
	Direction = -1 means a counter-clockwise rotation.
	Direction =  1 means a clockwise rotation.

	(list, int) -> list

	>>> rotate_90_degrees([[1, 1, 0],[0, 0, 0],[0, 0, 1]], 1)
	[[0, 0, 1], [0, 0, 1], [1, 0, 0]]
	>>> rotate_90_degrees([[1, 1, 0],[0, 0, 0],[0, 0, 1]], -1)
	[[0, 0, 1], [1, 0, 0], [1, 0, 0]]
	'''	

	output_array = []
	for x in range(len(image_array)):
			output_array.append([])
			for y in range(len(image_array[x])):
				output_array[x].append(image_array[x][y])

	if(direction == 1):
		length = len(output_array)
		for y in range(0, length):
			for x in range(0, length):
				output_array[y][-1-x] = image_array[x][y]

	if(direction == -1):
		length = len(output_array)
		for y in range(0, length):
			for x in range(0, length):
				output_array[-1-y][x] = image_array[x][y]

	return output_array

def flip_image(image_array, axis):
	'''
	Flips an image (rgb or grayscale) across the indicated axis.
	axis = -1 means along the diagonal (x = y).
	axis = 0 means along the y-axis.
	axis = 1 means along the x-axis.

	(list, int) -> list

	>>> flip_image([[1, 1, 0],[0, 0, 0],[0, 0, 1]], 1))
	[[0, 0, 1], [0, 0, 0], [1, 1, 0]]
	>>> flip_image([[1, 1, 0],[0, 0, 0],[0, 0, 1]], -1))
	[[1, 0, 0], [0, 0, 1], [0, 0, 1]]
	'''	
	output_array = []
	for x in range(len(image_array)):
			output_array.append([])
			for y in range(len(image_array[x])):
				output_array[x].append(image_array[x][y])
		
	if(axis == -1):
		length = len(output_array)
		for y in range(0, length):
			for x in range(0, length):
				output_array[-1-y][-1-x] = image_array[x][y]

	if(axis == 0):
		length = len(output_array)
		for y in range(0, length):
			for x in range(0, length):
				output_array[x][-1-y] = image_array[x][y]

	if(axis == 1):
		length = len(output_array)
		for y in range(0, length):
			for x in range(0, length):
				output_array[-1-x][y] = image_array[x][y]

	return output_array

def crop(image_array, direction, n_pixels):
	'''
	Crops an image(rgb or grayscale) a given amount of pixels from an indicated direction.

	(list, string, int) -> list

	>>> crop([[1, 1, 0],[0, 0, 0],[0, 0, 1]], "right", 1))
	[[1, 1], [0, 0], [0, 0]]
	>>> crop([[1, 1, 0],[0, 0, 0],[0, 0, 1]], "down", 1))	
	[[1, 1, 0], [0, 0, 0]]
	'''
	if(direction == "down"):
		output_array = []
		for x in range(len(image_array) - n_pixels):
				output_array.append([])
				for y in range(len(image_array[x])):
					output_array[x].append(image_array[x][y])

	if(direction == "up"):
		output_array = []
		for x in range(len(image_array) - n_pixels):
				output_array.append([])
				for y in range(len(image_array[x])):
					output_array[x].append(image_array[n_pixels + x][y])

	if(direction == "right"):
		output_array = []
		for x in range(len(image_array)):
				output_array.append([])
				for y in range(len(image_array[x]) - n_pixels):
					output_array[x].append(image_array[x][y])
					
	if(direction == "left"):
		output_array = []
		for x in range(len(image_array)):
				output_array.append([])
				for y in range(len(image_array[x]) - n_pixels):
					output_array[x].append(image_array[x][n_pixels + y])

	return output_array

def rgb_to_grayscale(rgb_image_array):
	'''
	Converts an rgb image array to grayscale using the formula:
	Gray = 0.2989 * r + 0.5870 * b + 0.1140 * b

	(list) -> list

	>>> rgb_to_grayscale([[[50,43,20], [88,243,48], [12,88,98]]]))
	[[42.466, 174.4162, 66.4148]]
	>>> rgb_to_grayscale([[[100,243,80], [78,43,84], [21,90,20]]]))
	[[181.651, 58.1312, 61.3869]]
	'''
	output_array = rgb_image_array
	for x in range(len(output_array)):
		for y in range(len(output_array[x])):
			output_array[x][y] =  0.2989 * output_array[x][y][0]\
							    + 0.5870 * output_array[x][y][1]\
							    + 0.1140 * output_array[x][y][2]

	return output_array

def invert_rgb(image_array):
	'''
	Given an rgb image, returns the image with inverted colors.

	(list) -> list

	>>> invert_rgb([[[100,243,80], [78,43,84], [21,90,20]]])
	[[[155, 12, 175], [177, 212, 171], [234, 165, 235]]]
    >>> invert_rgb([[[50,43,20], [88,243,48], [12,88,98]]])
	[[[205, 212, 235], [167, 12, 207], [243, 167, 157]]]
	'''

	output_array = image_array
	for x in range(len(image_array)):
		for y in range(len(image_array[x])):
			for z in range(3):
				output_array[x][y][z] = (255 - image_array[x][y][z])

	return output_array
    
def invert_grayscale(image_array):
	'''
	Given a grayscale image, returns the image with inverted colors.

	(list) -> list

	>>> invert_grayscale([[50,43,200]])
	[[205, 212, 55]]
	>>> invert_grayscale([[5,100,45]])
	[[250, 155, 210]]
	'''
	output_array = image_array
	#output_array = rgb_to_grayscale(image_array)
	for x in range(len(output_array)):
		for y in range(len(output_array[x])):
			output_array[x][y] = 255 - image_array[x][y]

	return output_array 

def histogram_equalization(img_array):
	'''
	Digitally enhances the image using the method of histogram equalization.

	(list) -> list

	>>> histogram_equalization([[[100,100,100]], [[78,78,78]], [[21,21,21]]])
	[[[255, 255, 255]], [[170, 170, 170]], [[85, 85, 85]]]
	>>> histogram_equalization([ [[66,66,66]], [[44,44,44]], [[121,121,121]]])
	[[[170, 170, 170]], [[85, 85, 85]], [[255, 255, 255]]]
	'''
	bins = []
	for i in range(256):
		bins.append(0)

	for i in range(len(img_array)):
		for j in range(len(img_array[0])):
			bins[img_array[i][j][0]] += 1
	
	total = len(img_array) * len(img_array[0])
	
	for k in range(256):
		bins[k] /= total

	for k in range(1,255):
		bins[k] += bins[k - 1]

	for i in range(len(img_array)):
		for j in range(len(img_array[0])):
			for k in range(3):
				img_array[i][j][k] = int(bins[img_array[i][j][k]] * 255)
				
	return img_array



if (__name__ == "__main__"):
	file = 'robot.png'
	#rev4




