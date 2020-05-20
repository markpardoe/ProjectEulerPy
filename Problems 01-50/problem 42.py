def replace_quotes(word):
	#print(word)
	return word.replace('"', '')

def word_value(word):
	word = word.upper()
	total = 0
	for c in word:
		total = total + ord(c) - 64

	return total


#Generator function for triangular numbers
def get_triangular_numbers():
	n = 1
	while True:
		yield int((n * (n+1)) / 2)
		n += 1  # increment step



triangular_numbers = set()
max_triangular_number = 0
generator = get_triangular_numbers()
count = 0

#text_file = open("C:\Code\ProjectEuler\data\problem18_data.txt", "r")
text_file = open("C:\Code\ProjectEuler\data\p042_words.txt", "r")
lines = text_file.readlines()
text_file.close()


words = lines[0].split(",")

words_uppercase = list(map(replace_quotes, words))


for word in words_uppercase:
	value = word_value(word)
	# if we haven't generated triangular numbers upto the current number
	while (value > max_triangular_number):
		tri = next(generator)
		max_triangular_number = tri
		triangular_numbers.add(tri)

	if (value in triangular_numbers):
		count = count + 1
		print(f"{word} = {value}")

print(count)