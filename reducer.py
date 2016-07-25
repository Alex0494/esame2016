import sys

def reducer():
		subtotal = 0
		previous_name = None
		for line in sys.stdin:
			line = line.strip('\n')
			actual_name = line.split('\t')[0]
			price = int(line.split('\t')[1])
			if previous_name == None:
				previous_name = actual_name
			if previous_name == actual_name:
				subtotal += price
			if previous_name != actual_name:	
				print previous_name + ', ' + str(subtotal)
				previous_name = actual_name
				subtotal = 0
				subtotal += price
		print previous_name + ', ' + str(subtotal)
		

if __name__ == '__main__':
	reducer()