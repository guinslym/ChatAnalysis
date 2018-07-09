import random


def shuffle():
	with open("QAs.txt", "r+", encoding = "utf-8") as f:
		lines = f.read().strip().split("\n\n")

	shuffled = random.sample(lines, len(lines))
	print(len(shuffled))

	write_file(shuffled,"shuffled")


def write_file(data, data_name):
	print(data_name)
	with open("%s.txt" %data_name, 'wb') as text_file:
		for line in data: 
			line = line + '\n\n'
			line = line.encode('utf-8')
			text_file.write(line)

## shuffle()