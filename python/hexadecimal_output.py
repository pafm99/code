user_input = raw_input("Enter a hex number")

output = 0
for power, hex_digit in enumerate(reversed(user_input)):
  print("{} * 16 ** {}".format(hex_digit, power))
  output += int(hex_digit, 16) * (16 ** power)

print(output)
