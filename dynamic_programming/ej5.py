import time

def costo(mes, produccion):
  switch_costo = {
    1: 100,
    2: 100,
    3: 12,
  }

  return switch_costo.get(mes) * produccion

def inventario(mes, produccion):
  switch_inventario = {
    1: 1.5,
    2: 1.5,
    3: 1.5,
  }

  return switch_inventario.get(mes) * produccion

def plan_radios(mes, stock, demanda):
  if mes == 1:
    return costo(mes, stock) + inventario(mes, stock - demanda[mes-1])
  min = 0

  for produccion in range(stock):
    aux_min = costo(mes, produccion) + inventario(mes, stock - demanda[mes-1]) + plan_radios(mes-1, stock-produccion+demanda[mes-1], demanda)
    if aux_min< min:
      min = aux_min

    return min
  
if __name__ == "__main__" :

  mes = 3
  stock = 300 
  demanda=[200, 200, 300]
  print(plan_radios(mes, stock, demanda))

