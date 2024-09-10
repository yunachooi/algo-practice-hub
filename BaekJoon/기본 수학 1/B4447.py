n = int(input())

for _ in range(n):
  NAME = input()
  name = NAME.lower()
  g = name.count("g")
  b = name.count("b")
  
  if g > b:
    print(NAME, "is GOOD")
  elif g == b:
    print(NAME, "is NEUTRAL")  
  else:
    print(NAME, "is A BADDY")
