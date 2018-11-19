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

"""REALIZA A BUSCA DO MENOR CAMINHO
   NECESSÁRIO PARA CONECTAR TODOS OS
   CAMPUS DA UNIVERSIDADE E O RETORNA"""

def dijsktra(grid, routers, listbad, nbad):
   """LISTA COM OS VÉRTICES A SEREM UTILIZADOS"""
   vertices = list()
   estimativas = list()
   precedentes = list()
   
   
   

"""Inicio do main"""

"""INICIO DAS VARIÁVEIS"""

"""NUMERO DE CAMPUS DA UNIVERSIDADE"""
ncapmi = input()
"""NUMERO DO CAMPI SENDO ANALISADO"""
campi = 1
"""DISTÂNCIA MÍNIMA"""
total = 0
"""STRINGS PARA USO SO STRINGCOMP"""
strcampus = "Campus "
str2 = ": "
strfinal = ""

"""INICIO DAS FUNÇÕES DO PROGRAMA"""

while ncampus >= 0:
   routers = input()
   grid = inputcollector(routers)
   grid = converttoint(grid)
   nbad = input()
   listbad = input()
   line = line.replace(" ", "")
   listbad = list(listbad)
   listbad = converttoint(listbad)
   total = dijsktra(grid, routers, listbad, nbad)
   strfinal = strcampus + campi + str2 + total
   print(strfinal)
   ncampi = ncampi - 1
   campi = campi + 1
