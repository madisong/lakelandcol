str = 'an example word:cat!!'

match = re.search(r'word:www', str)

# If-statement after search() tests if it succeeded
  if match:                      
    print 'found', match.group() ## 'found word:cat'

  else:
    print 'did not find'
