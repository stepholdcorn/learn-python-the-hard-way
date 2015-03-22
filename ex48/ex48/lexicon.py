def scan(input):
  words = input.split()
  sentence = []
  for word in words:
    if word == 'north' or word == 'south' or word == 'east' or word == 'west':
      item = ('direction', word)
    elif word == 'go' or word == 'kill' or word == 'eat':
      item = ('verb', word)
    else:
      item = ('stop', word)
    sentence.append(item)
  return sentence