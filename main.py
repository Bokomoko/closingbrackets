# returns true if the pair of opening/close is valid

def is_valid(code):
  # pairs of opening and closing brackets 
  openers = {'(': ')', '[': ']', '{': '}'}

  stack = []
  for piece in code:
    if piece in openers: # is it an opener ? 
      stack.append(openers[piece])  # let´s stack the closer for it and move on
      continue
    if piece in openers.values() : # is it a closer? 
      last = stack.pop()   # let´s see what's the next closer should be ...
      if last != piece:    # is it a match? no!!!
        return False       # sorry, closing something that´s not opened

  return len(stack) == 0   # is there any opener remaining? 


print(is_valid('{ [] ( ) }') is True)
print(is_valid('{ [(] ) }') is False)
print(is_valid('{ [ }') is False)
print(is_valid('{ [ ] } { (') is False)

