'''  a,b=list(strArr[0]), list(strArr[1])
  for x in b:
    if x == "-B":
      b.pop() if b else None
    else:
      b.append(x)
    
  ''.join(b)
  printable1=
  '''

##**************************************


  def EquivalentKeypresses(strArr):
  a=[]
  b=[]
  for x in strArr[0].split(','):
    if x =='-B':
      a.pop() if a else None
    else:
      a.append(x)

  for y in strArr[1].split(','):
    if y == '-B':
      b.pop() if b else None
    else:
      b.append(y)

  string1=''.join(a)
  string2=''.join(b)
  # code goes here
  return string1==string2


# keep this function call here 
print(EquivalentKeypresses(input()))

#*******************************************


def DifferentCases(strParam):


  

  # code goes here
  hold=''
  cap=True
  for item in strParam:
    if item.isalpha():
      if cap:
        hold += item.upper()
        cap= False
      else:
        hold += item.lower()
    else:
      cap= True

  return hold

# keep this function call here 
print(DifferentCases(input()))