def main():
  number = user_input()
  result = is_positive(number)
  print(f"You entered a {result} number")

def is_positive(number):
  if number > 0:
    return "positive"
  elif number == 0:
    return "Number is 0"
  else:
    return "Negative"
  
def user_input():
  while True:
    try:
      value = input("Enter a Number")
      number = float(value)
      return number
    except ValueError:
      print("Please Enter a valid number")

main()  

