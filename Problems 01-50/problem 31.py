

target = 200
count = 0

for pounds in (0, 1,2):
	print(f"{pounds} pounds")
	pound_total = pounds * 100
	if (pound_total > target):
		break

	for fifty_pence in (0,1,2,3,4):
		fifty_total = pound_total + (fifty_pence * 50)
		if (fifty_total > target):
			break

		for twenty_pence in range(0, target):
			twenty_total = fifty_total +  (twenty_pence * 20)
			if (twenty_total > target):
				break

			for ten_pence in range(0, target):
				ten_total = twenty_total +  (ten_pence * 10)
				if (ten_total > target):
					break

				for five_pence in range(0, target + 1):
					total = ten_total + (five_pence * 5)
					if (total > target):
						break

					for two_pence in range(0, target + 1):
						total = ten_total + (five_pence * 5) +  (two_pence * 2)
						if (total > target):
							break

						for one_pence in range (0, target + 1):
							total = ten_total + (five_pence * 5) +  (two_pence * 2) + (one_pence * 1)
							if (total > target):
								break

							if (total == target):
							#	print(f"{pounds} pounds, {fifty_pence} fifty pences, {twenty_pence} twentys, {ten_pence} tens, {five_pence} fives, {two_pence} twos and {one_pence} pence")
								count = count + 1

print(count)


