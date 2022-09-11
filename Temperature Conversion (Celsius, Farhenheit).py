#Ask the user what conversion to do (C to F or the other way around?)
while True:
    conversion_input = input('Please enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ')

#Adding an OR to exit the programme if input is a wrong value

    if conversion_input in ['C', 'F']:

#Asking the number to be converted
        converted_value = float(input('Please enter the {:s} amount to be converted: '.format(conversion_input)))

        if conversion_input == 'C':
            F = (converted_value * 1.80 + 32)
            print('The amount of {:1.5f} Celsius degrees is {:1.5f} degrees of Fahrenheit'.format(converted_value, F))
            break
        else:
            C = (converted_value - 32) / 1.80
            print('The amount of {:1.5f} Fahrenheit degrees is {:1.5f} degrees of Celsius'.format(converted_value, C))
            break
    else:
        print('Please enter a valid value: C or F')
        continue

exit_program = input("Press any key to exit")
if exit_program :
    print("Exiting the Program.")
    exit()
