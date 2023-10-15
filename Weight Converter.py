xyz = int(input('Please Enter Weight: '))
unit = input('(L)bs or (K)g:')
if unit.upper == "L":
  converted= xyz * 0.45
  print(f"You are {converted} Kilos")
else:
  converted = xyz // 0.45
  print(f"You are {converted} Pounds")