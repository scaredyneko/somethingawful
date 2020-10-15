temperature = input("Provide a temperature: ")

if temperature[-1] not in ['C', 'F'] or len(temperature) < 2:  # 1C
    print("Wrong input. Specify a scale (C or F).")
    exit(1)

if not temperature[:-1].isdigit():
    if temperature.count('-') == 1 and temperature[0] == '-':
        if not temperature[1:-1].isdigit():
            if '.' not in temperature or len(temperature) < 5 or temperature.count('.') > 1:  # -0.1C
                print("Wrong input. It should be a number in base-10 number system.")
                exit(2)
            if not temperature[1:temperature.find('.')].isdigit() or not temperature[
                                                                        temperature.find('.') + 1:-1].isdigit():
                print("Wrong input. It should be a number in base-10 number system.")
                exit(3)
    else:
        if '.' not in temperature or len(temperature) < 4 or temperature.count('.') > 1:  # 0.1C
            print("Wrong input. It should be a number in base-10 number system.")
            exit(2)
        if not temperature[:temperature.find('.')].isdigit() or not temperature[
                                                                     temperature.find('.') + 1:-1].isdigit():
            print("Wrong input. It should be a number in base-10 number system.")
            exit(3)

numeric_part = float(temperature[:-1])

if temperature[-1] == "C":
    print(f"Converted to Fahrenheit it would be: {numeric_part * 9 / 5 + 32}F")
    if numeric_part < -273.15:
        print("Although it's not likely that this kind of temperature is possible in nature though.")
else:
    print(f"Converted to Celsius it would be: {(numeric_part - 32) * 5 / 9}C")
    if numeric_part < -459.67:
        print("Although it's not likely that this kind of temperature is possible in nature though.")