import math
limit = 1000
product = 0



for m in range(1, limit):
	m_sqr = m*m 
	if m_sqr > limit:
		break	# we know that c = n_sqr + m_sqr - so we already know we've exceeded our max value as (a + b + c ) <= limit

	for n in range(m, limit):
		n_sqr = n*n
		a = n_sqr - m_sqr
		b = 2 * m * n
		c = n_sqr + m_sqr

		if (a + b + c > limit):
			break
		
		if (a + b + c == limit):
			product = a * b * c
			print(str(c) + " = " + str(a) + " - " + str(b))
			print(product)