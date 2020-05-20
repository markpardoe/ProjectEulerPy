# https://projecteuler.net/problem=59

text_file = open("G:\Code\ProjectEulerPy\data\p059_cipher.txt", "r")
data = text_file.readline()
text_file.close()

codes = data.split(',')

#print(codes)

# inputs for key
min_char = 97
max_char = 122

# valid ASCI characters for checking
min_check_char = 32
max_check_char = 122 



def is_valid_key(key, first_index, offset, code_to_translate):

	# Test every 3rd letter starting from the initial index
	# check if the character is valid - if not, then return false
	for index in range(first_index, len(code_to_translate), offset):
		new_char_ord = int(code_to_translate[index]) ^ key
		char = chr(new_char_ord)

		# check if translations outside normal range
		#if (new_char >= min_char and new_char <= max_char) or (new_char >= min_char_upper and new_char <= max_char_upper) or new_char == 32:
		if (new_char_ord >= min_check_char and new_char_ord <= max_check_char and new_char_ord != 33):
			pass # don't do anything

		else:
			return False

	return True

def translate_code(a, b, c, code_to_translate):
	#print(code_to_translate)
	keys = [a,b,c]
	key_index = 0
	translation = ""
	asci_total = 0

	for index in range(0, len(code_to_translate)):
		new_char_ord = int(code_to_translate[index]) ^ keys[key_index]
	#	print(f"{new_char_ord} = {chr(new_char_ord)}")
		# update the key index
		key_index += 1
		if (key_index >= len(keys)):
			key_index = 0
	#	print(chr(new_char_ord))
		translation = translation + chr(new_char_ord)
		asci_total += new_char_ord
	return translation, asci_total


a_codes = []
b_codes = []
c_codes = []
	

# get codes for a
for key in range(min_char, max_char+ 1):
	if(is_valid_key(key, 0, 3, codes)):
	#	print(f"{key} = {chr(key)}")
		a_codes.append(key)

# get values for b
for key in range(min_char, max_char+ 1):
	if(is_valid_key(key, 1, 3, codes)):
	#	print(f"{key} = {chr(key)}")
		b_codes.append(key)

# get values for c
for key in range(min_char, max_char+ 1):
	if(is_valid_key(key, 2,3 , codes)):
	#	print(f"{key} = {chr(key)}")
		c_codes.append(key)


print(a_codes)
print(b_codes)
print(c_codes)

for a in a_codes:
	for b in b_codes:
		for c in c_codes:
			print(f"{a}, {b}, {c}")
			translation, total =  translate_code(a, b, c, codes)
			print(translation)
			print(total)

