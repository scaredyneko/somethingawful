# taking the value of n and checking whether it fits the criteria
while True:
    n = input("Give me an integer greater than 2: ")
    
    if not n.isnumeric():
        print("It's not a number.")
        continue
    else:
        n = int(n)
        if n < 3:
            print("It's not in the range.")
            continue
    
# a list to store composite numbers
excluded = []

# sieve of eratosthenes algorithm
for element in range(2, n):
    for number in range(element + 1, n):
        if number % element == 0:
            if number not in excluded: 
                excluded.append(number)
    # printing the prime to the file
    if element not in excluded:
        if element == 2:
            with open('primes.txt', 'w'):
                pass
        with open('primes.txt', 'a+') as primes:
            primes.write(str(element) + '\n')