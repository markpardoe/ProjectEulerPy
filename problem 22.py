
def get_name_score(name):
	total = 0
	for c in name:
		total += ord(c) - 64
	return total


def load_text_file(file_name):
	#text_file = open("C:\Code\ProjectEuler\data\problem18_data.txt", "r")
	text_file = open(file_name, "r")
	lines = text_file.readlines()
	text_file.close()
	return lines


lines = load_text_file("C:\Code\ProjectEuler\data\p022_names.txt")
names = []
names = lines[0].replace('"', '').split(",")
names.sort()
#print(names)

total = 0
for idx, name in enumerate(names):
	total += (get_name_score(name) * (idx+1))

print(total)
