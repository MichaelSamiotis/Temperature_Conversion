#Ask the user what conversion to do (C to F or the other way around?)
conversion_input = input('Please enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ')

#Adding an OR to exit the programme if input is a wrong value
if conversion_input == 'C' or conversion_input == 'F':

#Asking the number to be converted
    conversion_float = float(input('Please enter the {:s} amount to be converted: '.format(conversion_input)))
    converted_value = float(conversion_float)

    if conversion_input == 'C':
        F = (converted_value * 1.80 + 32)
        print('The amount of {:1.5f} Celsius degrees is {:1.5f} degrees of Fahrenheit'.format(converted_value, F))
    else:
        C = (converted_value - 32) / 1.80
        print('The amount of {:1.5f} Fahrenheit degrees is {:1.5f} degrees of Celsius'.format(converted_value, C))

else:
    print('Please enter a valid value: C or F')