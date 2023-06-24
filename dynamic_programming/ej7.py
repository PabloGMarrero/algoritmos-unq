import time

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
  
if __name__ == "__main__" :

  a:str = "abbac"
  b:str = "abcbc"
  current_time = time.time()
  print(current_time)
  #print(a + b[-1])
  tot = min_convert_string_to(a, b, len(a), len(b))
  print(tot)
  print(time.time()-current_time)
 