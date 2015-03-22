def scan(input):
  words = input.split()
  sentence = []
  for word in words:
    if word == 'north' or word == 'south' or word == 'east' or word == 'west':
      item = ('direction', word)
    else:
      item = ('verb', word)
    sentence.append(item)
  return sentence