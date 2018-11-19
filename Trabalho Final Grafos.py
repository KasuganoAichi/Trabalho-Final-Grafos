"""NOTA MUITO IMPORTANTE:
   PARA A EXCEUÇÃO DO ALGORTIMO DE CYK A ENTRADA É ESPERADA JUNTO
   AO ARQUIVO QUE CONTÉM A GRAMATICA, A MESMA DEVE ESTAR NA
   PRIMEIRA LINHA, LINHA QUE CONTÉM O COMENTÁRIO "#Terminais"
   A PALAVRA DEVE TER "W" ANTES DE SEU PRIMEIRO VALOR E
   SEUS ITENS NÃO DEVEM SER SEPARADOS POR ESPAÇO
   EXEMPLO DE ENTRADA ESPERADA:
   "#Terminais	W[ a ][ dog ][ runs ][ in ][ the ][ park ]"
   VALE LEMBRAR QUE SE OUVER ESPAÇO ENTRE OS TERMINAIS, O ALGORITMO
   NÃO IRÁ FUNCIONAR, POIS O MESMO NÃO FAZ O TRATAMENTO DE ESPAÇOS
   AQUEM DOS QUE SEPARAM O VALOR DO TERMINAL DOS COLCHETES"""

"""biblioteca usada na função para retirada as produções vazias"""

from itertools import permutations

"""Parte 1 - Gerador de Gramática
   Programa cria um set()gramatica
   E escreve na tela o conteudo do set()
   Cada item da gramatica é uma string ou set"""

"""listacomandos lista os comandos na tela
   para o usuário escolher"""

def listacomandos():
    print("Lista de Comandos:")
    print("1 - Gerar Gramatica")
    print("2 - Simplifcar a Gramatica")
    print("3 - Algoritmo de CYK")
    print("4 - Terminar Programa")

"""Retira os terminais do arquivo
   utiliza a função rstrip() para
   exclusão do '\n', demais funções
   "gera" utilizam o mesmo metodo"""

def palavra (f):
    pos = 0
    palavra = list()
    palavraaux = list()
    lido = f.readline()
    if 'W' in lido:
        pos = lido.find('W')
        lido = lido[pos+1:]
        lido = lido.rstrip('\t')
        while not (lido == '\n'):
            pos = lido.find(']')
            stringaux = lido
            lido = lido[:pos+1]
            stringaux = stringaux[pos+1:]
            palavraaux.append(lido)
            lido = stringaux
        palavra.append(palavraaux)
    else:
        palavra = ''
    return palavra

def geraterminais(f):
    terminais = set()
    lido = 't'
    while lido != '#Variaveis':
        lido = f.readline()
        lido = lido.rstrip('\n')
        lido = lido.rstrip('\t')
        if lido != '#Variaveis':
            terminais.add(lido)
    return terminais    

"""a partir daqui a variavel "lido" será sempre
   iniciada para prevenir erros, ela terá
   seu valor correto colocado assim que
   entrar no laço while"""

"""Retira as variaveis do arquivo"""

def geravariaveis(f):
    variaveis = set()
    lido = ''
    while lido != '#Inicial':
        lido = f.readline()
        lido = lido.rstrip('\n')
        lido = lido.rstrip('\t')
        if lido != '#Inicial':
            variaveis.add(lido)
    return variaveis

"""Retira a variavel inicial do arquivo"""

def gerainicial(f):     
    inicial = set()
    lido = ''
    while lido != '#Regras':
        lido = f.readline()
        lido = lido.rstrip('\n')
        lido = lido.rstrip('\t')
        if lido != '#Regras':
            inicial.add(lido)
    return inicial

"""Retira o conjunto de regras do arquivo"""

def geraregras(f):
    regras = set()
    lido = 'v'
    aux = ' '
    while lido != '':
        lido = f.readline()
        lido = lido.rstrip('\n')
        lido = lido.rstrip('\t')
        if lido != '':
            regras.add(lido)
    return regras

"""Parte 2, a contar daqui são realizadas as operações de simplificação"""

"""remove produções vazias(sim, ficou mega complicado, a gente sabe)"""

def producoesvazias (regras):

    conjuntoaux = set(regras)
    alcancaV = set()
    x = 0
    y = 0
    z = 0
    pos = 0
    regraaux = ''
    "Busca nas Regras todas as produções que chegam em V"

    for item in conjuntoaux:
        tupleconjunto = tuple(conjuntoaux)
        if "[ V ]" in tupleconjunto[x]:
            alcancaV.add(tupleconjunto[x])
            x=x+1
        else:
            x=x+1
    " ================================================== "

    " Retira o que tem após > do conjunto que chega em V "

    conjuntoV = set()
    alcancaVaux = list(alcancaV)
    
    for item in alcancaVaux:
        regraaux = alcancaVaux[y]
        pos = regraaux.find(']')
        regraaux = regraaux[:pos+1]
        y = y+1
        conjuntoV.add(regraaux)
    " ================================================== "

    " Busca as regras que chegam no conjunto que chega em V "
    
    listaV = list(conjuntoV)
    conjuntoV2 = set()
    y = 0
    for item in listaV:
        for item in regras:
            conjuntoFinal = list(regras)
            regraaux2 = conjuntoFinal[y]
            pos = regraaux2.find(']')
            regraaux2 = regraaux2[pos-4:pos+1]
            possivelregra = regraaux2
            if regraaux2 == listaV[z]:
                y=y+1
            else:
                regraaux2 = conjuntoFinal[y]
                pos = regraaux2.find('>')
                regraaux2 = regraaux2[pos+1:]
                if listaV[z] in regraaux2:
                    if possivelregra in listaV:
                        y=y+1
                    else:
                        conjuntoV2.add(possivelregra)
                        y=y+1
                else:
                    y=y+1
        y = 0
        z = z + 1

    conjuntoV.update(conjuntoV2)

    " Construção das novas Regras e adiciona ao conjunto "
    
    z = 0
    y = 0
    retira = 0
    strconjunto = ''
    strregra = ''
    regras = list(regras)
    conjuntoV = list(conjuntoV)
    conjuntoVaux = conjuntoV

    for item in conjuntoVaux:
        strconjunto = conjuntoVaux[z]

        for item in regras:
            strregra = regras[y]
            pos = strregra.find('>')
            strregra = strregra[pos+2:]

            if strconjunto in strregra:
                retira = 0
                break
            else:
                retira = 1
            y = y + 1

        if retira == 1:
            conjuntoV.remove(strconjunto)
        z = z + 1
        y = 0


    vazia = 1
    outrasregras = set()
    novasregras = list()
    produz = list()
    produzaux = list()
    posproduz = list()
    permlist = list()
    stringlist = list()
    stringlistaux = list()
    straux = ''
    straux2 = ''
    strconjuntoaux = ''
    strproduz = ''
    string = ''
    auxstring = ''
    stringaux = ''
    stringaux2 = ''
    caracter = ''
    remover = 0
    nproduz = 0
    nproduzaux = 0
    pos = 0
    posaux = 0
    i = 0
    j = 0
    x = 0
    z = 0
    count = 0
    eleregra = 0
    eleregraux = 0
    repete = 0

    
    """cria as novas regras de produção"""
    for item in conjuntoV:
        strconjunto = conjuntoV[z]

        for item in regras:
            strregra = regras[y]
            pos = strregra.find('>')
            strregra = strregra[pos+2:]

            if strconjunto in strregra:
                straux = strregra

                while vazia != 0:
                    straux2 = straux
                    pos = straux.find(']')
                    straux = straux[pos+2:]
                    eleregra = eleregra + 1
                    straux2 = straux2[:pos+1]
                    produz.append(straux2)
                    
                    if strconjunto == straux2:
                        repete = repete + 1
                        
                    if not straux:
                        break

                strconjuntoaux = strconjunto
                
                if repete == 1:
                    strregra = regras[y]
                    pos = strregra.find('>')
                    strregra = strregra[pos+1:]
                    strregra = strregra.replace(strconjuntoaux, '')
                    strregra = strregra.replace('  ', ' ')
                    straux = regras[y]
                    pos = straux.find('>')
                    straux = straux[:pos+1]
                    straux = straux + strregra
                    novasregras.append(straux)
                else:
                    produzaux = list()
                    i = 0
                    for item in produz:
                        produzaux.append(produz[i])
                        i = i + 1
                    strregra = regras[y]
                    pos = strregra.find('>')
                    strregra = strregra[:pos+2]
                    straux = strregra
                    i = 0
                    
                    for item in produz:
                        if strconjunto == produz[i]:
                            posproduz.append(i)
                        i = i + 1
                    i = 0
                    nproduz = len(posproduz)
                    nproduzaux = nproduz
                    """caso para retirada de 1 simbolo vazio"""
                    j = 0
                    for item in posproduz:
                        produz.pop(posproduz[j])
                        for item in produz:
                            nproduz = len(produz)
                            strregra = strregra + produz[i]
                            nproduz = nproduz - 1
                            if nproduz > 0:
                                strregra = strregra + ' '
                            i = i + 1
                        novasregras.append(strregra)
                        strregra = straux
                        produzaux = list()
                        i = 0
                        for item in produzaux:
                            produz.append(produzaux[i])
                            i = i + 1
                        i = 0
                        j = j + 1
                    j = 0
                    """caso para retirada de todos os simbolos"""
                    eleregraaux = eleregra - nproduzaux
                    eleregra = eleregra - 2

                    i = 0
                    j = 0
                    x = 0
                    if eleregraaux > 0:
                        
                        while eleregraaux > 0:
                            permsList = set(permutations(produz, eleregra))
                            permsList = list(permsList)
                            x = 0
                            i = 0

                            for item in permsList:
                                auxstring = permsList[x]
                                lenlist = len(auxstring) - 1
                                for item in auxstring:
                                    string = string + auxstring[i]
                                    if i != lenlist:
                                        string = string + ' '
                                    i = i + 1
                                stringlist.append(string)
                                string = ''
                                i = 0
                                x = x + 1

                            eleregra = eleregra - 1
                            eleregraaux = eleregraaux - 1
                            x = 0
                            i = 0
                                
                            j = len(stringlist)
                            while j > 0:
                                string = stringlist[x]
                                count = string.count(strconjunto)
                                if count >= eleregra:
                                    stringlist.remove(string)
                                else:
                                    x = x + 1
                                i = i + 1
                                j = j - 1

                            stringlistaux = list(stringlist)
                            i = 0
                            j = 0
                            x = 0
                            stringaux = ''
                            stringaux2 = ''
                            caracter = ''
                            pos = 0
                            remover = 0

                            
                            for item in stringlistaux:
                                string = stringlist[i]
                                stringaux = string
                                stringaux2 = string
                                pos = stringaux.find(']')
                                stringaux = stringaux[:pos+1]
                                stringaux2 = stringaux2[pos+2:]
                                for item in produz:
                                    caracter = produz[j]
                                    if caracter in string:
                                        if caracter in stringaux:
                                            stringaux = stringaux2
                                            pos = stringaux.find(']')
                                            stringaux = stringaux[:pos+1]
                                            stringaux2 = stringaux2[pos+2:]
                                        x = x +  1
                                    if not stringaux:
                                        remover = 0
                                        break
                                    else:
                                        remover = 1
                                    j = j + 1
                                if remover == 1:
                                    stringlist.pop(i)
                                else:
                                    i = i + 1
                                j = 0
                                x = 0

                            for item in stringlist:
                                nproduz = len(stringlist)
                                strregra = strregra + stringlist[x]
                                nproduz = nproduz - 1
                                if nproduz > 0:
                                    strregra = strregra + ' '
                                novasregras.append(strregra)
                                strregra = straux
                                x = x + 1
                            stringlist = list()
                                
            y = y + 1
            repete = 0
            eleregra = 0
        z = z + 1
        y = 0
    
    stringlist = list()
    x = 0
    y = 0

    for item in regras:
        strregra = regras[y]
        pos = strregra.find('>')
        strregra = strregra[pos+2:]
        straux = regras[y]
        pos = straux.find('>')
        straux = straux[:pos+2]
        while fim < 1:
            pos = strregra.find(']')
            stringaux = strregra[:pos+1]
            strregra = strregra[pos+2:]
            if not stringaux:
                break
            else:
                stringlist.append(stringaux)

        """THANK YOU COMENTARIO-KUN"""
        i = 0
        j = 0
        strregra = ''
        for item in stringlist:
            for item in stringlist:
                if j == i:
                    strregra = strregra.replace('ESPACO', ' ')
                    strregra = strregra + stringlist[j]
                    strregra = strregra + 'ESPACO'
                elif stringlist[j] not in conjuntoV:
                    strregra = strregra.replace('ESPACO', ' ')
                    strregra = strregra + stringlist[j]
                    strregra = strregra + 'ESPACO'
                j = j + 1
            i = i + 1
            strregra = strregra.replace('ESPACO', '')
            strregra = straux + strregra
            novasregras.append(strregra)
            strregra = ''
            j = 0
        stringlist = list()
        
        y = y + 1
        
            
    i = 0
    for item in regras:
        novasregras.append(regras[i])
        i = i + 1
    i = 0
    novasregras = set(novasregras)

    return novasregras

"""insere '[ V ]' na linguagem"""

def colocaVinicial(regras,inicial):
    
    inicial = list(inicial)
    regras = list(regras)
    z = 0
    y = 0
    for item in regras:
        stregras = regras[y]
        pos = stregras.find('>')
        stresq = stregras[:pos+2]
        if inicial[z] in stresq:
            final = stresq + '[ V ]'
            break
        y = y+1
    regras = set(regras)
    regras.add(final)

    return regras

"""realiza a remoção dos caracteres '[ V ]' presentes no conjunto de regras, enviandos para uma
   dimensão inacalnçavel"""

def remocaodeV (regras):

    y = 0
    regras = list(regras)
    for item in regras:
        strregra = regras[y]
        strregra = strregra.replace('[ V ]', '')
        strregra = strregra.replace('  ', ' ')
        regras.remove(regras[y])
        regras.append(strregra)

    regras = set(regras)

    return regras

"""remove produções do tipo '[ S ] > ', pois seria o mesmo que '[ S ] > [ V ]' """

def remocaodeVazio (regras):
    y = 0
    regras = list(regras)
    regrasaux = list()
    for item in regras:
        regrasaux.append(regras[y])
        y = y + 1

    y = 0
    for item in regrasaux:
        strregra = regras[y]
        pos = strregra.find('>')
        strregra = strregra[pos+2:]
        if not strregra:
            regras.remove(regras[y])
        else:
            y = y + 1

    regras = set(regras)

    return regras

"""remove as produções unitárias"""

def ProducoesUnitarias(regras,terminais,inicial):
    terminaisaux = list(terminais)
    y = 0
    vazia = 1
    regras = list(regras)
    eleregra = 0
    regraunica = set()
    regrasnovas = set()
    for item in regras:
        strregra = regras[y]
        pos = strregra.find('>')
        strregra = strregra[pos+2:]
        straux = strregra
        strregraaux = strregra

        while vazia != 0:
            pos = straux.find(']')
            straux = straux[pos+2:]
            eleregra = eleregra + 1
            if not straux:
                if eleregra == 1:
                    pos = strregraaux.find(']')
                    strregraaux = strregraaux[:pos+2]
                    regraunica.add(strregraaux)
                break
                
                
        eleregra = 0
        y = y+1
    regraunica = list(regraunica)
    x = 0
    y = 0
    for item in terminaisaux:
        for item in regraunica:
            if regraunica[y] == terminaisaux[x]:
                regraunica.remove(terminaisaux[x])
            y = y+1
        x = x+1
        y = 0

    y = 0
    x = 0
    stregras = set()
    regrasinserir = list()
    for item in regraunica:
        for item in regras:
            stregras = regras[y]
            pos = stregras.find('>')
            stregras = stregras[:pos]
            if regraunica[x] in stregras:
                stregras = regras[y]
                pos = stregras.find('>')
                stregras = stregras[pos+2:]
                regrasinserir.append(stregras)
            
            y = y + 1

        v = 0
        z = 0
        conjuntoteste = set()
        for item in regras:
           stregras = regras[v]
           pos = stregras.find('>')
           stregras = stregras[pos+2:]
           straux = stregras
           if regraunica[x] in stregras:
               while vazia != 0:
                   pos = straux.find(']')
                   straux = straux[pos+2:] 
                   eleregra = eleregra + 1
                   if not straux:
                       if eleregra == 1:
                           straux = regras[v]
                           pos = straux.find('>')
                           straux = straux[:pos+1]
                           for item in regrasinserir:
                              strfinal = straux + ' ' + regrasinserir[z]
                              conjuntoteste.add(strfinal)
                              z = z + 1
                           regrasnovas = regrasnovas.union(conjuntoteste)   
                       break                                 
               eleregra = 0
               z = 0
           v = v + 1
        list.clear(regrasinserir)    
        x = x + 1
        y = 0

    regras = set(regras)
    regras = regrasnovas.union(regras)
    regras = list(regras)
    y = 0
    x = 0
    for item in regraunica:
        for item in regras:
            stregras = regras[y]
            pos = stregras.find('>')
            stregras = stregras[pos+2:]
            straux = stregras
            if regraunica[x] in stregras: 
                pos = straux.find(']')
                straux = straux[pos+2:]
                if not straux:
                    regras.remove(regras[y])
            y = y + 1
        x = x + 1
        y = 0

    regras = set(regras)
    regras = colocaVinicial(regras,inicial)

    return regras

"""realiza a remoção dos simbolos inuteis"""

def SimbolosInuteis (regras, inicial,terminais,variaveis):
    
     vazia = 1
     y = 0
     regras = list (regras)
     inicial = list(inicial)
     conjuntouteis = set()
     variaveis = list(variaveis)
     primeirosinuteis = set()
     x = 0

        
     for item in variaveis:
         for item in regras:
             stregras = regras[y]
             pos = stregras.find('>')
             stresq = stregras[:pos]
             if variaveis[x] not in stresq:
                 varaux = 1
             else:
                 varaux = 0
                 break
             y = y + 1
         if varaux == 1:
             primeirosinuteis.add(variaveis[x])
            
         y = 0
         x = x + 1

     z = 0
     x = 0
     w = 0
     y= 0
     regras = list(regras)
     primeirosinuteis = list(primeirosinuteis)
     for item in primeirosinuteis:
         for item in regras:
             if primeirosinuteis[z] in regras[x]:
                 regras.remove(regras[x])
                 for item in variaveis:
                     for item in regras:
                         stregras = regras[y]
                         pos = stregras.find('>')
                         stresq = stregras[:pos]
                         if variaveis[w] not in stresq:
                             varaux = 1
                         else:
                             varaux = 0
                             break
                         y = y + 1
                     if varaux == 1:
                         primeirosinuteis.append(variaveis[w])
                     w = w + 1
                     y = 0
                 w = 0
             else:
                 x = x + 1
         z = z + 1
         x = 0


     y = 0
     for item in regras:
            stregras = regras[y]
            pos = stregras.find('>')
            stresq = stregras[:pos]
            strdir= stregras[pos+2:]
            if inicial[0] in stresq:
                while vazia != 0:
                    pos = strdir.find(']')
                    varconjunto = strdir[:pos+1]
                    strdir = strdir[pos+2:]
                    conjuntouteis.add(varconjunto)
                    if not strdir:
                        break
            y = y + 1

     y = 0
     z = 0
     
     conjuntouteisaux = set()
     for item in conjuntouteis:
         for item in conjuntouteis:
             conjuntouteis = list(conjuntouteis)
             for item in regras:
                 stregras = regras[y]
                 pos = stregras.find('>')
                 stresq = stregras[:pos]
                 strdir= stregras[pos+2:]
                 if conjuntouteis[z] in stresq:
                     while vazia != 0:
                         pos = strdir.find(']')
                         varconjunto = strdir[:pos+1]
                         strdir = strdir[pos+2:]
                         conjuntouteis.append(varconjunto)
                         if not strdir:
                             break
                 y = y + 1
             y = 0
             z = z + 1
             conjuntouteis = set(conjuntouteis)
         z = 0

     inicial = set(inicial)   
     conjuntouteis = set(conjuntouteis)
     
     conjuntouteis = conjuntouteis.union(inicial)

     conjuntouteis = list(conjuntouteis)
     conjuntouteisaux = conjuntouteis
     terminais = list(terminais)
     y = 0
     for item in terminais:
         if terminais[y] in conjuntouteis:
             conjuntouteis.remove(terminais[y])
         else:    
             y = y + 1
     conjuntouteis = set(conjuntouteis)

     x = 0
     y = 0
     conjuntouteis = list(conjuntouteis)
     regras = list(regras)
     conjuntoinuteis = set()
     terminaiseliminar = set()
     variaveis = list(variaveis)
     
     for item in variaveis:
         if variaveis[x] not in conjuntouteis:
             conjuntoinuteis.add(variaveis[x])
         x = x + 1
     conjuntoinuteis = set(conjuntoinuteis)   

     z = 0
     y = 0
     conjuntoinuteisaux = list(conjuntoinuteis)
     regras = list(regras)
     for item in regras:
         for item in conjuntoinuteisaux:
             if conjuntoinuteisaux[z] in regras[y]:
                 regras.remove(regras[y])
             z = z + 1
         y = y + 1
         z = 0

     regras = set(regras)
     regras = colocaVinicial(regras,inicial)
     return regras

"""atualiza conjunto de varieveis, excluindo do mesmo as que acabaram por serem retiradas da linguagem
   deixando a mesma mais coesa"""

def atualizacaovariaveis(variaveis, regras):

    x = 0
    y = 0
    variaveis = list(variaveis)
    variaveisaux2 = list()
    regras = list(regras)
    variaveisaux2 = variaveis
    for item in variaveisaux2:
        for item in regras:
            if variaveis[y] not in regras[x]:
                z = 0
            else:
                z = 1
                break
            x = x + 1
        if z == 0:
            variaveis.pop(y)
        else:
            y = y + 1
        
        
        x = 0
    return variaveis

"""atualiza conjunto de terminais caso por algum motivo magico desconhecido ou em algum caso
   algum terminal tenha misticamente desaparecido da linguagem"""

def atualizacaoterminais (terminais, regras):

    x = 0
    y = 0
    terminais = list(terminais)
    terminaisaux2 = list()
    regras = list(regras)
    terminaisaux2 = terminais
    for item in terminaisaux2:
        for item in regras:
            if terminais[y] not in regras[x]:
                z = 0
            else:
                z = 1
                break
            x = x + 1
        if z == 0:
            terminais.pop(y)
        else:
            y = y + 1
        
        
        x = 0
    return terminais

"""realiza a concatenção das variaveis durante a execução do CYK, fazendo todas as combinações necessárias"""

def concatenaVariaveis(palavra, x, count2, regras):
    paux = list()
    listasaida = list()
    row = set()
    celula1 = list()
    celula2 = list()
    novacelula = ''
    i = 0
    j = 0
    y = 0
    pos = 0
    stri = ''
    striaux = ''
    regras = list(regras)
    count = count2
    linha1 = 1  
    coluna1 = 0 
    linha2 = x
    coluna2 = 1
    colunaaux = coluna2
    while count >= 1:
        while linha2 >= 1:
            celula1 = palavra[linha1][coluna1]
            celula2 = palavra[linha2][coluna2]
            for item in celula1:
                for item in celula2:
                    stri = celula1[i] + " "
                    stri = stri + celula2[j]
                    for item in regras:
                        striaux = regras[y]
                        pos = striaux.find('>')
                        striaux = striaux[pos+2:]
                        if stri == striaux:
                            novacelula = regras[y]
                            pos = novacelula.find(']')
                            novacelula = novacelula[:pos+1]
                            row.add(novacelula)
                        y = y + 1
                    y = 0
                    j = j + 1
                i = i + 1
                j = 0
            i = 0
            linha1 = linha1 + 1
            linha2 = linha2 - 1
            coluna2 = coluna2 + 1
        linha1 = 1
        coluna1 = coluna1 + 1
        linha2 = x
        colunaaux = colunaaux + 1
        coluna2 = colunaaux
        count = count - 1
        pos = len(row)
        if pos == 0:
            row.add('[ V ]')
        listasaida.append(list(row))
        row = set()
    return listasaida


"""executa o algoritmo de CYK e bem "desenha" o triângulo resultante.
   quaisquer confusões causadas pelo triângulo, foi porque ficou meio
   ruim de ler as células mesmo"""

def CYK(palavra, regras, inicial):
    count = 0
    x = 0
    i = 0
    regras = list(regras)
    row = set()
    truerow = list()
    inicial = list(inicial)
    paux = list()
    paux = palavra[0]
    for item in paux:
        for item in regras:
            string = regras[x]
            pos = string.find('>')
            string = string[pos+2:]
            if string == paux[i]:
                string = regras[x]
                pos = string.find(']')
                string = string[:pos+1]
                row.add(string)
            x = x + 1
        row = list(row)
        truerow.append(row)
        row = set()
        i = i + 1
        x = 0
    palavra.append(truerow)
    count = len(palavra[0]) - 1      
    auxcount = count
    x = 1
    while count >= 1:
        palavra.append(concatenaVariaveis(palavra, x, count, regras))
        count = count - 1
        x = x + 1
    x = 0
    for item in palavra:
        x = x + 1
    x = x - 1
    paux = palavra[x][0]
    x = len(palavra)
    
    i = -1
    while x >= 1:
        print(palavra[i])
        i = i - 1
        x = x - 1
    if inicial[0] in paux:
        print("\n\nPalavra pertence à linguagem\n")
    else:
        print("\n\nPalavra não pertence à linguagem\n")
    



"""Inicio do main"""

"""Variável de controle do programa"""
fim = 0
"""Conjunto dos terminais"""
terminais = set()
"""Conjunto das variaveis"""
variaveis = set()
"""Variavel inicial"""
inicial = set()
"""Conjunto das regras"""
regras = set()


"""elfi é o equivalente a ter um else: if condição"""
x = 0
while fim != 1:
    listacomandos()
    comando = input("Digite o valor do comando a ser executado: ")
    if comando == '4':
        fim = 1
    elif comando == '1':
        fname = input("\nInforme nome do arquivo(com o .txt): ")
        f = open(fname,mode = 'r')
        palavraCYK = palavra(f)
        terminais = geraterminais(f)
        variaveis = geravariaveis(f)
        inicial = gerainicial(f)
        regras = geraregras(f)
        f.close()
        f = ''
        print("\nG = Terminais: ", terminais)
        print("\nVariáveis: ", variaveis)
        print("\nVariável Inicial: ", inicial)
        print("\nRegras de Produção: ")
        x = 0
        regras = list(regras)
        for item in regras:
            print(regras[x])
            x = x + 1
        print("\n")
        regras = set(regras)
        print("\n\n\n")
    elif comando == '2':
        regras = producoesvazias(regras)
        regras = remocaodeV(regras)
        regras = remocaodeVazio(regras)
        regras = colocaVinicial(regras,inicial)
        variaveis = atualizacaovariaveis(variaveis, regras)
        terminais = atualizacaoterminais(terminais, regras)
        print("\n")
        print("ETAPA 1 REMOÇÃO DE PRODUÇÕES VAZIAS:")
        print("\nG = Terminais: ", terminais)
        print("\nVariáveis: ", variaveis)
        print("\nVariável Inicial: ", inicial)
        print("\nRegras de Produção: ")
        x = 0
        regras = list(regras)
        for item in regras:
            print(regras[x])
            x = x + 1
        print("\n")
        regras = ProducoesUnitarias(regras,terminais,inicial)
        variaveis = atualizacaovariaveis(variaveis, regras)
        terminais = atualizacaoterminais(terminais, regras)
        print("\n")
        print("ETAPA 2 REMOÇÃO DE PRODUÇÕES UNITÁRIAS:")
        print("\nG = Terminais: ", terminais)
        print("\nVariáveis: ", variaveis)
        print("\nVariável Inicial: ", inicial)
        print("\nRegras de Produção: ")
        x = 0
        regras = list(regras)
        for item in regras:
            print(regras[x])
            x = x + 1
        print("\n")

        regras = set(regras)
        
        regras = SimbolosInuteis(regras,inicial,terminais,variaveis)
        variaveis = atualizacaovariaveis(variaveis, regras)
        terminais = atualizacaoterminais(terminais, regras)
        
        "regras = producoesvazias(regras)"
        "tirainuteis(inicial, regras, variaveis, terminais)"
        print("ETAPA 3 REMOÇÃO DOS SIMBOLOS INUTEIS:")
        print("\nG = Terminais: ", terminais)
        print("\nVariáveis: ", variaveis)
        print("\nVariável Inicial: ", inicial)
        print("\nRegras de Produção: ")
        x = 0
        regras = list(regras)
        for item in regras:
            print(regras[x])
            x = x + 1
        regras = set(regras)
        print("\n")
    elif comando == '3':
        print("\n\nPalavra: ", palavraCYK)
        print("\n\n")
        CYK(palavraCYK, regras, inicial)
        print("\n")
    else:
        print("\n\nComando inexistente\n\n")

print('\n\n\n\n\n')
print("Fim de execução :3")
