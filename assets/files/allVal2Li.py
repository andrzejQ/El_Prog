def allValuesList(d):
  ''' Lista wartości ze złożonej struktury, z pomijaniem pewnych kluczy i wartości None
>>> x = {'a':'aaa', 'b':'bb', 0:None, 'arr':[{'a':'AAA','b':'BB'},{'c':'CCC'}], '..':'..', 123:[1,2,3]}
>>> list(allValuesList(x))
['aaa', 'bb', 'AAA', 'BB', 'CCC', '1', '2', '3']
>>> list(allValuesList( [4,5] ))
['4', '5']
>>> list(allValuesList( {'a':None} ))
[]'''
  if isinstance(d, dict):
    for k,v in d.items():
      if k not in ['...','..']:
        yield from allValuesList(v)
  elif not isinstance(d,str) and hasattr(d,'__iter__'):
    for v in d: 
      yield from allValuesList(v)
  else:
    if not (d is None):
      yield str(d)

if __name__ == "__main__":
  import doctest
  doctest.testmod()
