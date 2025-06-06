
def perform_operation(num1, num2, operation):
  def addition(num1, num2):
    return num1 + num2

  def subtraction(num1, num2):
    return num1 - num2

  def multiplication(num1, num2):
    return num1 * num2

  def division(num1, num2):
    if (num2 == 0):
      return "math error"
    return num1 / num2

  def calculation(num1, num2, operation):
    match operation:
      case "add":
        return addition(num1, num2)
      case "subtract":
        return subtraction(num1, num2)
      case "multiply":
        return multiplication(num1, num2)
      case "divide":
        return division(num1, num2)
      case _:
        return "Invalid operations"
        
