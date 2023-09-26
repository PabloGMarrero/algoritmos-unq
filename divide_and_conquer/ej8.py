def parejas(a):
  if len(a)==2:
    if a[0]>a[1]:
      return (1, [a[1],a[0]])
    else:
      return (0, a)
  
  pivot = int(len(a)/2)

  ai = parejas(a[0:pivot])
  ad = parejas(a[pivot:len(a)])

  res = 0
  while not len(ai[1])==0 and not len(ad[1])==0:
    if ai[1][len(ai[1])-1] > ad[1][0]:
      res = res + 1#len(ai[1])
      ai = (ai[0], ai[1][1:])
    else:
      ad = (ad[0], ad[1][1:])

  return res + ai[0] + ad[0]

if __name__ == "__main__" :
  array = [9,5,3,4]
  print(parejas(array))