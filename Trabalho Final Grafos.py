"""INPUTCOLLECTOR: COLETA O INPUT DO TECLADO E
   O SALVA EM UMA MATRIZ (LISTA DE LISTAS) PARA ANÁLISE"""

def inputcollector(routers):
   """LISTA DE NÚMEROS"""
   grid = list()
   """COLETA VALORES E MONTA MATRIZ"""
   while routers >= 0:
      line = input()
      line = line.replace(" ", "")
      line = list(line)
      grid = grid.append(line)
      routers = routers - 1
   return grid

"""CONVERTE UMA LISTA DE STRINGS EM UMA
   LISTA DE INTEIROS"""

def converttoint(listint):
   listint = map(int, listint)
   listint = list(map(int, listint))
   return

def dijsktra():
   

"""Inicio do main"""

"""NUMERO DO CAMPI SENDO ANALISADO"""
campi = 1
"""DISTÂNCIA MÍNIMA"""
total = 0
"""STRINGS PARA USO SO STRINGCOMP"""
strcampus = "Campus "
str2 = ": "
strfinal = ""

"""C"""
ncapmi = input()
while ncampus >= 0:
   routers = input()
   grid = inputcollector(routers)
   grid = converttoint(grid)
   nbad = input()
   listbad = input()
   line = line.replace(" ", "")
   listbad = list(listbad)
   listbad = converttoint(listbad)
   total = dijsktra(grid, listbad)
   strfinal = strcampus + campi + str2 + total
   print(strfinal)
   ncampi = ncampi - 1
   campi = campi + 1
