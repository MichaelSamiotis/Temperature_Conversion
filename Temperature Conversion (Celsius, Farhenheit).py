import sys
#Ask the user what conversion to do (Celsius to Fahrenheit or the other way around?)
conversion_input = 0
while True:
    conversion_input = input('Please enter \'C\' to convert Celsius to Fahrenheit or \'F\' to \
convert Fahrenheit to Celsius: ')
    
#Handling the user's input to be accepted if the value is correct
    if conversion_input == 'C' or conversion_input == 'c' \
    or conversion_input == 'celsius' or conversion_input == 'Celsius':
        conversion_input = 'C'
        break
    elif conversion_input == 'F' or conversion_input == 'f' \
    or conversion_input == 'fahrenheit' or conversion_input == 'Fahrenheit':
        conversion_input = 'F'
        break
        
#Asking from the user the preferred temperature number to be converted
converted_value = float(input(f'Please enter the {conversion_input} amount to be converted: '))

#Conversion of the input temperature
if conversion_input == 'C':
    F = round((converted_value * 1.80 + 32),2)
    print(f'The amount of {converted_value} Celsius degrees is {F} degrees of Fahrenheit')
elif conversion_input == 'F':
    C = round(((converted_value - 32) / 1.80),2)
    print(f'The amount of {converted_value} Fahrenheit degrees is {C} degrees of Celsius')
    
#Handling of the program exit
exit_program = input('Press any key to exit')
if exit_program:
    sys.exit()
