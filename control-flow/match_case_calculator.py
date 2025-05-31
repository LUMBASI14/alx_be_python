first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))
operation = str(input("Choose the operation (+, -, *, /):"))
                       
match operation:
  case "+":
    sum = first_number + second_number
    print("the result is " + str(sum))
  case "-":
    subtraction = first_number - second_number
    print("the result is" + str(subtraction))
  case "*":
    multiplication = first_number * second_number
    print("the result is" + str(multiplication))
  case "/":
    if second_number >0:
      division = first_number / second_number
      print("the result is" + str(division))
    print("you cannot divide by 0")
    
