user_input = input("Give me a number from 0 to 99: ")
user_input = user_input.replace(' ', '')

if user_input.isnumeric():
	user_input = int(user_input)
	if 0 <= user_input <= 99:
		first_digit = user_input // 10
		second_digit = user_input % 10
		
		first_list = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
		second_list = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
		third_list = ['десять', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
		
		i = -1
		k = -1
		
		while first_digit != i:
			i += 1
			if first_digit == i:
				while second_digit != k:
					k += 1
					if second_digit == k:
						if first_digit == 0:
							if second_digit == 0:
								print("ноль")
							else:
								print(second_list[k])
						elif first_digit == 1:
							print(third_list[k])
						else:
							print(first_list[i - 1] + ' ' + second_list[k])
	else:
		print("This number is not in the range.")
else:
	if user_input != '':
		if user_input[0] == '-':
			user_input = user_input[1:]
			if user_input.isnumeric():
				print("This number is not in the range.")
			else:
				print("The input is either not a number or is something complex (e.g. --1) that the program cannot handle yet.")
	else:
		print("It's not a number.")
