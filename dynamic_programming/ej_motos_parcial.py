""" 
motos cuesta $4500 por 40 paquetes
autos cuesta $6000 por 60 paquetes

se quiere mandar n paquetes
"""
def costo_envios(paquetes):

  if paquetes<=40:
    return 4500
    
  if paquetes<=60:
    return 6000

  if paquetes - 60 <= 40:
    return 4500 + costo_envios(paquetes-40)
  else: 
    return 6000 + costo_envios(paquetes-60)


def costo_envios_c(paquetes):
  if paquetes<=40:
    return 4500
    
  if paquetes<=60:
    return 6000

  if paquetes - 60 <= 40:
    return 4500 + costo_envios_cache(paquetes-40)
  else: 
    return 6000 + costo_envios_cache(paquetes-60)


def costo_envios_cache(paquetes):

  if cache[paquetes] == None:
    cache[paquetes] = costo_envios_c(paquetes)

  return cache[paquetes]

def costo_envios_BU(paquetes, cache):
  cache[0] = 0
  i = 0

  while paquetes>0:
    if paquetes<=40:
      i = paquetes + i -1
      cache[i] = 4500 + cache[i-60]
      paquetes = paquetes -40
    if paquetes<=60:
      i = paquetes + i -1
      cache[i] = 6000 + cache[i-40]
      paquetes = paquetes - 60
  
    if paquetes > 0:
      if paquetes - 60 <= 40:
        i = paquetes-60-1
        cache[i] = 4500 + cache[i-40]
        paquetes = paquetes - 40
      else: 
        i = paquetes-40-1
        cache[i] = 6000 + cache[i-60]
        paquetes = paquetes - 60
  
  return cache[len(cache)-1]
  

paquetes = 61
cache = [None for x in range(paquetes)]
cache2 = [0 for x in range(paquetes)]

#print(costo_envios(paquetes))
#print(costo_envios_c(paquetes))
print(costo_envios_BU(paquetes, cache2))

 

