def scan(input):
  words = input.split()
  sentence = []
  for word in words:
    direction = ('direction', word)
    sentence.append(direction)
  return sentence