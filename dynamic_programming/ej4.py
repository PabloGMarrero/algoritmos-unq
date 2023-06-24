import time

def opVector(vector, num, size_vector, total):
  if size_vector == 0:
    print("num", num)
    print("total_init", total)
    return num == total
  
  return opVector(vector, num, size_vector-1, vector[size_vector-1]+ total) or opVector(vector, num, size_vector-1, vector[size_vector-1] * (1 if num==0 else num)) or opVector(vector, num, size_vector-1, vector[size_vector-1] ** (1 if num==0 else num))

if __name__ == "__main__" :

  vector = [3, 1, 5, 2, 1]
  num = 400
  total_init = 0
  #current_time = time.time()
  #print(current_time)

  print(opVector(vector, num, len(vector), total_init))
  #print(time.time()-current_time)
 

