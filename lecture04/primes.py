import datetime

# получение значения n и проверка на наличие ошибок
appropriate = False

while not appropriate:
    n = input("Give me a number greater than 2: ")
    n = n.strip()
    n = n.replace(',', '.')

    for char in n:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if char != '.' or '.' not in n[1:] or len(n) < 3 or n.count('.') > 1:
                print("Try again.")
                break
        if char == n[-1]:
            appropriate = True

    if appropriate:
        n = int(n[:n.find('.') if n.count('.') == 1 else len(n)])
        if n <= 2:
            print("Try again.")
            appropriate = False

start_time = datetime.datetime.now()

# создание нового файла и/или удаление из него содержимого
with open('primes.txt', 'w'):
    pass

# список для хранения простых чисел
prime_numbers = list(range(2, n))

# поиск простых чисел с помощью алгоритма "решето эратосфена"
for element in prime_numbers:
    if element * element >= n:
        break
    for number in prime_numbers[prime_numbers.index(element * element):]:
        if number % element == 0:
            prime_numbers.remove(number)

# запись простых чисел в файл
for prime in prime_numbers:
    with open('primes.txt', 'a') as text_file:
        text_file.write(str(prime) + '\n')

end_time = datetime.datetime.now()

# уведомление о завершении работы
print("Done.")

print(end_time - start_time)
