#Ask the user what conversion to do (C to F or the other way around?)
conversion_input = 0
while conversion_input not in ['C','F']:
    conversion_input = input('Please enter C to convert Celsius to Fahrenheit or F to \
convert Fahrenheit to Celsius: ')

#Asking the number to be converted
converted_value = float(input(f'Please enter the {conversion_input} amount to be converted: '))

if conversion_input == 'C':
    F = (converted_value * 1.80 + 32)
    print(f'The amount of {converted_value} Celsius degrees is {F} degrees of Fahrenheit')
elif conversion_input == 'F':
    C = (converted_value - 32) / 1.80
    print(f'The amount of {converted_value} Fahrenheit degrees is {C} degrees of Celsius')

exit_program = input('Press any key to exit')
if exit_program:
    print('Exiting the Program.')
    exit()
