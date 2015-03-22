def scan(input):
  words = input.split()
  sentence = []
  for word in words:
    if word == 'north' or word == 'south' or word == 'east':
      item = ('direction', word)
    elif word == 'go' or word == 'kill' or word == 'eat':
      item = ('verb', word)
    elif word == 'the' or word == 'in' or word == 'of':
      item = ('stop', word)
    else:
      item = ('noun', word)
    sentence.append(item)
  return sentence