# https://projecteuler.net/problem=17

num2words = {0: "", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2wordsTens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

def number(Number):
	print(Number)
	if 1 <= Number <= 19:
		return num2words[Number]
	elif Number >= 20 and Number <= 99:
 		tens, below_ten = divmod(Number, 10)
 		return num2wordsTens[tens]  + num2words[below_ten]
	elif Number >= 100 and Number <= 999:
 		hundreds, other = divmod(Number, 100)

 		word =  num2words[hundreds] + 'hundred'
 		if other > 0:
 			word = word + 'and' +  number(other)  #get wording of remainder

 		return word

	elif Number == 1000:
		return "Onethousand"
	else:
		print("Number out of range")


limit = 1000
total = 0

for i in range(1, limit+1):
	word = number(i)

	print(word + ' = '+ str(len(word)))

	total += len(word)

print(total)