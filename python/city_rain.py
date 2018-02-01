total_rain = {}
while True:
  city_name = input("Enter city name: ")
  if not city_name:
    break
  rainfall = input("Enter amount of rain: ") # input returns a string even if a number was entered
  
  if rainfall.isdigit(): # We need this to turn string numbers into ints
    rainfall = int(rainfall) 
  else:
    print("You didnt give me a number")
    continue
  total_rain[city_name] = total_rain.get(city_name, 0) + rainfall
for key, value in total_rain.items():
  print("{}: {}".format(key, value))
