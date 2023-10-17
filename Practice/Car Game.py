print("")
print("Welcome to the Car Game, Please type help for instructions")
command = ""
state = False
while True:
  command = input("-->").lower() 
  if command == "start":
    if state:
       print("The car is already running")
    else: 
      state = True 
      print("The Car has Started...")
  elif command == "stop":
    if not state:
       print("Car is already stopped")
    else:
      state = False   
      print("The Car has Stopped...")
  elif command == "help":
    print("""
To Start the car type: start
To Stop the car type: stop
To exit the car type: quit
          """)
  elif command == "quit":
        break
  else: 
      print("I don't Understand")
