def main():
  number = function1()
  function2(number)
  
# Checks if number is +ve and if negative keeps asking

def function1():
  while True:
    n = int(input("what is value of x?"))
    if n > 0:
      break
  return n   
  
# Create the print function

def function2(n):  
  for x in range(n):
    print("Check out Functions and Loops")
    
main()
