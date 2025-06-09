FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9/5

def convert_to_celsius(fahrenheit):
  return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = int(input("Enter temperature to convert: "))
type_temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type_temp == "C":
  convert_temp = convert_to_celsius(temp)
else:
  convert_temp = convert_to_fahrenheit(temp)

print(convert_temp)
