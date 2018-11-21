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
      grid.append(line)
      routers = routers - 1
   return grid

"""CONVERTE UMA LISTA DE STRINGS EM UMA
   LISTA DE INTEIROS"""

def converttoint(listint, x):
   i = 0
   j = 0
   straux
   while i <= x:
      while j <= x:
         listint[i][j] = listint[i][j]
         j = j + 1
      i = i + 1
      j = 0
   return listint

"""REALIZA A BUSCA DO MENOR CAMINHO
   NECESSÁRIO PARA CONECTAR TODOS OS
   CAMPUS DA UNIVERSIDADE E O RETORNA"""

def dijsktra(grid, routers, listbad, nbad):
   """INDÍCES DA MATRIZ
      VALORES INICIAM EM 1 POIS
      QUANDO CHAMADOS PELA PRIMEIRA VEZ
      NECESSITAM ESTAR EM 1"""
   i = 1 """COLUNA"""
   imax = 0
   
   """MATRIZ COM OS VÉRTICES A SEREM UTILIZADOS"""
   grid2 = list()
   
   """AUXILIARES"""
   auxlist = list(0)
   menor = 0
   pos = 0
   pred = 0
   
   while routers >= 0:
      grid2 = grid2.append(imax)
      imax = imax + 1
      routers = routers - 1
      
   imax = imax - 1
   
   while i <= imax:
      if (i + 1) in listbad:
         auxlist = auxlist.append(0)
      else:
         auxlist = auxlist.append(grid[0][i])
      i = i + 1
   
   grid2 = grid2.append(auxlist)
   auxlist = list(0)
   i = 0
   
   while i <= jmax:
      if (i + 1) in listbad:
         auxlist = auxlist.append(0)
      else:
         auxlist = auxlist.append('X')
      i = i + 1

   while 'X' in grid2:
      i = 0
      for item in grid2[0]
         if menor > grid2[1][i]:
            if grid2[2][i] != 'X':
               menor = grid2[1][i]
               pos = i
         i = i + 1
      grid2[2][pos] = pred
      pred = pos
      i = 0
      for item in grid2[0]:
         if (i + 1) not in listbad:
            grid2[1][i] = grid2[1][i] + grid[pred][i]
         i = i + 1
   auxlist = grid2[1]
   
   return sum(auxlist)
   

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
strcampi = ""
str2 = ": "
strtotal = ""
strfinal = ""

"""INICIO DAS FUNÇÕES DO PROGRAMA"""

while ncampus >= 0:
   routers = input()
   grid = inputcollector(routers)
   grid = converttoint(grid, routers)
   nbad = input()
   listbad = input()
   line = line.replace(" ", "")
   listbad = list(listbad)
   listbad = map(int, listbad)
   listbad = list(map(int, listbad))
   total = prim(grid, routers, listbad, nbad)
   strfinal = strcampus + str(campi) + str2 + str(total)
   print(strfinal)
   ncampi = ncampi - 1
   campi = campi + 1
