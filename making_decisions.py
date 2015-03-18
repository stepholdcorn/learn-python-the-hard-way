print 'You enter a dark room with two doors. Do you go through door #1 or #2?'

door = raw_input('> ')

if door == '1':
  print 'There is a giant bear eating cake. What do you do?'
  print '1. Take the cake.'
  print '2. Scream at the bear.'

  bear = raw_input('> ')

  if bear == '1':
    print 'The bear eats you, good job.'
  elif bear == '2':
    print 'The bear eats your leg, good job.'
  else:
    print 'Well, doing %s is probably the best thing. Bear runs away!' % bear

elif door == '2':
  print 'There is a giant Pikachu, what do you feed it?'
  print '1. Blueberries.'
  print '2. Cake.'
  print '3. Chocolate.'

  pikachu = raw_input('> ')

  if pikachu == '1' or pikachu == '2':
    print 'Pikachu is happy with the snack, you win!'
  else:
    print 'Pikachu is not happy, and slaps you in the face.'

else:
  print 'You stumble and fall on a knife and die.'