def binomial_coefficient(n, m):
  if m == 0 or m == n :
    return 1

  c = binomial_coefficient(n-1, m-1) + binomial_coefficient(n-1, m)
  print("c", c)

if __name__ == "__main__" :
  binomial_coefficient(len("ABC"), 2)