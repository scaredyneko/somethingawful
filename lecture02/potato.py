user_input = input('Give me a number from 0 to 99: ')
user_input = user_input.replace(" ", "")
if user_input.isnumeric():
	user_input = int(user_input)
	if 0 <= user_input <= 99:
		first_digit = user_input // 10
		second_digit = user_input % 10
		first_list = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
		second_list = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
		if first_digit == 0:
			if second_digit == 0:
				print(second_list[0])
			elif second_digit == 1:
				print(second_list[1])
			elif second_digit == 2:
				print(second_list[2])
			elif second_digit == 3:
				print(second_list[3])
			elif second_digit == 4:
				print(second_list[4])
			elif second_digit == 5:
				print(second_list[5])
			elif second_digit == 6:
				print(second_list[6])
			elif second_digit == 7:
				print(second_list[7])
			elif second_digit == 8:
				print(second_list[8])
			elif second_digit == 9:
				print(second_list[9])
		elif first_digit == 1:
			if second_digit == 0:
				print("десять")
			elif second_digit == 1:
				print("одинадцать")
			elif second_digit == 2:
				print("двенадцать")
			elif second_digit == 3:
				print("тринадцать")
			elif second_digit == 4:
				print("четырнадцать")
			elif second_digit == 5:
				print("пятнадцать")
			elif second_digit == 6:
				print("шестнадцать")
			elif second_digit == 7:
				print("семнадцать")
			elif second_digit == 8:
				print("восемнадцать")
			elif second_digit == 9:
				print("девятнадцать")
		elif first_digit == 2:
			if second_digit == 0:
				print(first_list[-8])
			elif second_digit == 1:
				print(first_list[-8] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-8] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-8] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-8] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-8] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-8] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-8] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-8] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-8] + " " + second_list[9])
		elif first_digit == 3:
			if second_digit == 0:
				print(first_list[-7])
			elif second_digit == 1:
				print(first_list[-7] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-7] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-7] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-7] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-7] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-7] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-7] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-7] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-7] + " " + second_list[9])
		elif first_digit == 4:
			if second_digit == 0:
				print(first_list[-6])
			elif second_digit == 1:
				print(first_list[-6] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-6] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-6] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-6] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-6] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-6] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-6] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-6] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-6] + " " + second_list[9])
		elif first_digit == 5:
			if second_digit == 0:
				print(first_list[-5])
			elif second_digit == 1:
				print(first_list[-5] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-5] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-5] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-5] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-5] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-5] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-5] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-5] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-5] + " " + second_list[9])
		elif first_digit == 6:
			if second_digit == 0:
				print(first_list[-4])
			elif second_digit == 1:
				print(first_list[-4] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-4] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-4] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-4] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-4] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-4] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-4] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-4] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-4] + " " + second_list[9])
		elif first_digit == 7:
			if second_digit == 0:
				print(first_list[-3])
			elif second_digit == 1:
				print(first_list[-3] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-3] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-3] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-3] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-3] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-3] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-3] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-3] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-3] + " " + second_list[9])
		elif first_digit == 8:
			if second_digit == 0:
				print(first_list[-2])
			elif second_digit == 1:
				print(first_list[-2] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-2] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-2] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-2] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-2] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-2] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-2] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-2] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-2] + " " + second_list[9])
		elif first_digit == 9:
			if second_digit == 0:
				print(first_list[-1])
			elif second_digit == 1:
				print(first_list[-1] + " " + second_list[1])
			elif second_digit == 2:
				print(first_list[-1] + " " + second_list[2])
			elif second_digit == 3:
				print(first_list[-1] + " " + second_list[3])
			elif second_digit == 4:
				print(first_list[-1] + " " + second_list[4])
			elif second_digit == 5:
				print(first_list[-1] + " " + second_list[5])
			elif second_digit == 6:
				print(first_list[-1] + " " + second_list[6])
			elif second_digit == 7:
				print(first_list[-1] + " " + second_list[7])
			elif second_digit == 8:
				print(first_list[-1] + " " + second_list[8])
			elif second_digit == 9:
				print(first_list[-1] + " " + second_list[9])
	else:
		print("This number is not in the range.")
else:
	if user_input != "":
		if user_input[0] == "-":
			user_input = user_input[1:]
			if user_input.isnumeric():
				print("This number is not in the range.")
			else:
				print("The input is either not a number or it's something complex (e.g. --1) that the program cannot handle yet.")
	else:
		print("It's not a number.")