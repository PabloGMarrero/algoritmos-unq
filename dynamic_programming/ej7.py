def min_convert_string_to(a:str, b:str, length_a:int, length_b:int) -> int:
  if length_a == 0:
    return b
  if length_b == 0:
    return a
  
  if a[-1] == b[-1]:
    return min_convert_string_to(a[:-1], b[:-1], length_a-1, length_b-1)
  
  return 1 + min(
                min_convert_string_to(a + b[-1], b, length_a+1, length_b),
                min_convert_string_to(a[:-1], b, length_a-1, length_b)
            )


"""Sean u y v dos string de caracteres. Queremos transformar u en v con el menor número de operaciones posibles de alguno de los
siguientes tipos:
• borrar un caracter
• agregar un caracter
• cambiar un caracter
Por ejemplo uno puede transformar u = abbac en v = abcbc en tres pasos, (borrar b del segundo lugar de u, agregar b en el
penltimo lugar, cambiar la a que est en el tercer lugar a c).
Es esta forma de transformar u en v óptima?
Escribir un algoritmo de programación dinámica que encuentre el mínimo número de operaciones necesarias para transformar u
en v e informe cuales son las operaciones necesarias. Cuál es la complejidad del algoritmo en función de las longitudes de u y v?"""

cache= []

def convert(u, v, i, j, tot):
  if i == 0 and j == 0:
    return tot
  
  if i == 0 and j > 0:
    return convert(u, v, i, j-1, tot+1)
  
  if i > 0 and j == 0:
    return convert(u, v, i-1, j, tot+1)

  if u[i] == v[j]:
    return convert(u, v, i-1, j-1, tot)
  else:
    return convert(u, v, i-1, j-1, tot+1)
  
def convertC(u, v, i, j, tot):
  if i == 0 and j == 0:
    return tot
  
  if i == 0 and j > 0:
    return convert_cache(u, v, i, j-1, tot+1)
  
  if i > 0 and j == 0:
    return convert_cache(u, v, i-1, j, tot+1)

  if u[i] == v[j]:
    return convert_cache(u, v, i-1, j-1, tot)
  else:
    return convert_cache(u, v, i-1, j-1, tot+1)
  
def convert_cache(u, v, i, j, tot):
  if cache[i][j] == None:
    cache[i][j] = convertC(u, v, i, j, tot)

  return cache[i][j]
  
def init_cache(init_value, n, m):
    R = []
    for _ in range(0, n):
        R = R + [[init_value] * m]
    return R

def convert_iterativo(u, v):
  len_u = len(u)
  len_v = len(v)

  i, j = 0, 0

  while i < len_u or j < len_v:            
    if i == len_u and j < len_v:
      cache[i][j] = cache[i][j-1] + 1
      j= j+1
      
    elif i < len_u and j == len_v:
      cache[i][j] = cache[i-1][j] + 1
      i= i+1

    elif u[i] == v[j]:
      cache[i][j] = cache[i-1][j-1]
      i= i+1
      j= j+1
    else:
      cache[i][j] = cache[i-1][j-1] + 1
      i= i+1
      j= j+1
  

  return cache[len_u][len_v]

if __name__ == "__main__" :
  u:str = "abb"
  v:str = "abcccccc"

  
  cache = init_cache(0, len(v), len(v))
  #tot = convert(u, v, len(u)-1, len(v)-1, 0)
  #tot = convertC(u, v, len(u)-1, len(v)-1, 0)
  tot = convert_iterativo(u, v)
  print(tot)

 