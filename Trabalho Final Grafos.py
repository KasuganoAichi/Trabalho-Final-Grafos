"""INPUTCOLLECTOR: COLETA O INPUT DO TECLADO E
   O SALVA EM UMA MATRIZ (LISTA DE LISTAS) PARA ANÁLISE"""

def inputcollector(routers, control):
   """LISTA DE NÚMEROS"""
   grid = list()
   auxlist = list()
   lineaux = ''
   line = ''
   pos = 0
   aux = routers - 1
   aux2 = aux
   """COLETA VALORES E MONTA MATRIZ"""
   while routers > 0:
      line = input()
      lineaux = line
      while aux >= 0:
         if aux == 0:
            auxlist.append(int(lineaux))
            break
         else:
            pos = line.find(' ')
            line = line[:pos]
            auxlist.append(int(line))
            lineaux = lineaux[pos+1:]
            line = lineaux
            aux = aux - 1
      aux = aux2
      grid.append(auxlist)
      routers = routers - 1
   if control == 1:
      return grid
   else:
      print('retornou listbad')
      return auxlist

"""REALIZA A BUSCA DA ARVORE GERADORA
   MINIMA NECESSÁRIA PARA CONECTAR TODOS OS
   CAMPUS DA UNIVERSIDADE E A RETORNA"""

def prim(grid, routers, listbad):
   """INDÍCES DA MATRIZ
      VALORES INICIAM EM 1 POIS
      QUANDO CHAMADOS PELA PRIMEIRA VEZ
      NECESSITAM ESTAR EM 1"""
   i = 0
   j = 0
   
   """MATRIZ SER UTILIZADA"""
   grid2 = list()
   
   """AUXILIARES"""
   auxlist = list(0)
   usedlistbad = list()
   total = 0
   menor = 0
   pos = 0
   aux = 0
   
   while len(auxlist) < routers:
      menor = 999999
      for item in auxlist:
         i = auxlist[aux]
         if i not in usedlistbad:   
            while j <= routers:
               grid2.append(grid[i][j])
               j = j + 1
            j = 0
            for item in grid2:
               if j + 1 not in listbad or i + 1 not in listbad:
                  if grid2[j] < menor:
                     if j not in auxlist and grid2[j] != 0:
                        menor = grid2[j]
                        pos = j
                  j = j + 1
            j = 0
            aux = aux + 1
      total = total + menor
      aux = 0
      auxlist.append(pos)
      if pos in listbad:
         usedlistbad.append(pos)
   return total   
      
   

"""Inicio do main"""

"""NUMERO DE CAMPUS DA UNIVERSIDADE"""
ncampi = int(input())
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

while ncampi >= 0:
   routers = int(input())
   grid = inputcollector(routers, 1)
   nbad = int(input())
   listbad = inputcollector(nbad, 0)
   total = prim(grid, routers, listbad, nbad)
   strfinal = strcampus + str(campi) + str2 + str(total)
   print(strfinal)
   ncampi = ncampi - 1
   campi = campi + 1
