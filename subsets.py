

def split(data, n):

	train_len, val_len, test_len = set_len(num_lines, n)
	
	train = data[ :train_len +1]
	print(len(train))
	validation = data[train_len +1 : train_len +val_len +1]
	test = data[num_lines - test_len : ]
	
	# write_file(train, "train")
	# write_file(validation, "validation")
	# write_file(test, "test")
	# print("done")



## Take 1/n th of data as traing set, 1/n th as validation set, and the rest as test set
def set_len(length, n):
	train_len = int(length / n)
	val_len = int(length / n)
	test_len = num_lines - train_len - val_len
	# print(train_len, val_len, test_len)
	return train_len, val_len, test_len


def write_file(data, data_name):
	print(data_name)
	with open("%s.txt" %data_name, 'wb') as text_file:
		for line in data: 
			line = line + '\n\n'
			line = line.encode('utf-8')
			text_file.write(line)



if __name__ == "__main__": 
	
	with open("shuffled.txt", "r+", encoding = "utf-8") as f:
		lines = f.read().strip().split("\n\n")
	
	num_lines = len(lines)
	print(num_lines)
	
	split(lines, 5)
