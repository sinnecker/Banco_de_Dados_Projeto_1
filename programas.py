from rotinas import*
from classe_Matriz import*

import numpy as np

# Manipular a lista ############################################################

def add_matrix(matrix_list):
  
  ### Rotina que adiciona uma matriz nova na lista passada ###
  

  add_matriz = True

  while add_matriz:

    #Entrada do tipo de matriz
    tipo_da_matriz = input(" Digite 1 para Matriz Retangular \n Digite 2 para Matriz Quadrada \n Digite 3 para Matriz Simétrica \n Digite 4 para Matriz Triangular Inferior \n Digite 5 para Triangular Superior \n Digite 6 para Diagonal \n ")

    if tratamento_opcao(tipo_da_matriz,6):
      print("Opção inválida, entre novamente")

    else:
      
      #Entrada da dimensão caso seja retangular
      if tipo_da_matriz == '1':
        tamanho = input("Insira o tamanho da matriz na forma mxn ")
        linhas, colunas = tamanho.split('x')
        while tratamento_numerico(linhas) and tratamento_numerico(colunas):
          print("Entrada inválida")
          tamanho = input("Insira o tamanho da matriz na forma mxn ")

        M = Matriz_Retangular(int(linhas), int(colunas))
        add_regular(M)

      else:

        #Entrada da dimensão da matriz Quadrada
        linhas = input("Insira o número de linhas da matriz ")
        while tratamento_numerico(linhas):
          print("Entrada inválida")
          linhas = input("Insira o número de linhas da matriz ")
        linhas = int(linhas)


        if tipo_da_matriz == '2':
          M = Matriz_Quadrada(linhas)
          add_regular(M)

        if tipo_da_matriz == '3':
          M = Matriz_Simetrica(linhas)
          add_simetric(M)

        if tipo_da_matriz == '4':
            M = Matriz_Triangular_Inferior(linhas)
            add_triangular(M)

        if tipo_da_matriz == '5':
            M = Matriz_Triangular_Superior(linhas)
            add_triangular(M,'sup')

        if tipo_da_matriz == '6':
          M = Matriz_Diagonal(linhas)
          add_diag(M)

      controle = input("Digite 1 para adicionar outra matriz \n Digite 2 para parar ")
      while tratamento_opcao(controle,2):
        print("entrada_invalida")
        controle = input("Digite 1 para adicionar outra matriz \n Digite 2 para parar ")

      if controle=='1':
        matrix_list.append(M)
      else:
        matrix_list.append(M)
        add_matriz = False

  return None

def del_matrix(matrix_list):
  
  ### Rotina para deletar uma única matriz da lista ###
  
  if len(matrix_list)==0:
    print("Lista vazia")
    return []
  else:
    controle = True
    while controle:
      #Escolhe qual matriz quer tirar
      index = input("Entre o indice da matriz que deseja excluir")
      
      if tratamento_numerico(index):
        print("Entrada inválida")  
      else:
        if int(index)>=len(matrix_list) or int(index)<0:
          print("Indice fora da lista ou inválido")
        else:
          controle = False
    index = int(index)
    matrix_list = matrix_list[:index]+matrix_list[index+1:]
    
    return matrix_list

def lista_func():
 
  ### Le a lista de matrizes de um arquivo ###

  matriz_list = []
  
  with open("listadematrix.txt","r") as f:
    lines = f.readlines()
  
  
  num_matrizes = int(lines[0])
  
  for line in lines[1:]:
    #Separa as informações de cada matriz e cria os objetos da classe Matriz
    tipo,dimensao,entradas = line.split(sep="; ")
    linhas_matrix,colunas_matrix = dimensao.split(sep="x")
    linhas_matrix  = int(linhas_matrix)
    colunas_matrix = int(colunas_matrix)
    dados = entradas.split(sep = ",")
    dados = [float(k) for k in dados]

    if  tipo == "1":
        M = Matriz_Retangular(linhas_matrix,colunas_matrix) 
        M.Read_data(dados)
        matriz_list.append(M)
    
    elif tipo == "2":
        M = Matriz_Quadrada(linhas_matrix)
        M.Read_data(dados)
        matriz_list.append(M)
    
    elif tipo == "3":
        M = Matriz_Simetrica(linhas_matrix)
        M.Read_data(dados)
        matriz_list.append(M)
    
    elif tipo == "4":
        M = Matriz_Triangular_Inferior(linhas_matrix)
        M.Read_data(dados)
        matriz_list.append(M)
    
    elif tipo == "5":
        M = Matriz_Triangular_Superior(linhas_matrix)
        M.Read_data(dados)
        matriz_list.append(M)
    
    elif tipo == "6":
        M = Matriz_Diagonal(linhas_matrix)
        M.Read_data(dados)
        matriz_list.append(M) 

  print(f"Número de matrizes : {num_matrizes}")
    
  for matriz in matriz_list:
    print(matriz)
    
    
  return matriz_list

def limpar_lista_func():

  ### Reseta a lista de matrizes e limpa o arquivo ###
  
  with open("listadematrix.txt","a+") as f:
    f.truncate(0)
    f.write('0')
  return []

def save_file(matrix_list):
  
  ### Salva a lista de matrizes em um arquivo txt ###
  
  with open("listadematrix.txt","a+") as f:
    f.truncate(0)
    f.write(str(len(matrix_list)))
    f.write('\n')
    for m in matrix_list:
      info = m.get_data()
      f.write(info)
      f.write('\n')
  return None
# Opera as matrizes da lista ###################################################


def matrix_traco(matrixes_list):
  
  ### Escolhe uma matriz e calcula o traço ###
  
  m1 = T1_matrixes(matrixes_list)

  M = matrixes_list[m1]
  if isinstance(matrixes_list[m1], Matriz_Quadrada):
    return M.traco()
  else:
    print("Matriz não Quadrada")

def matrix_det(matrixes_list):
  
  ### Escolhe uma matriz e calcula o determinante ###
  
  m1 = T1_matrixes(matrixes_list)

  M = matrixes_list[m1]
  if isinstance(matrixes_list[m1], Matriz_Quadrada):
    return M.det()
  else:
    print("Matriz não Quadrada")

def matrix_inv(matrixes_list):
  
  ### Escolhe uma matriz e calcula a inversa ###
  
  m1 = T1_matrixes(matrixes_list)
  M = matrixes_list[m1]
  if isinstance(matrixes_list[m1], Matriz_Quadrada):
    if M.det()!=0:
      return M.inversa()
    else:
      print("Matriz Singular")
  else:
    print("Matriz não Quadrada")

def matrix_diag(matrixes_list):
  
  ### Escolhe uma matriz e calcula a diagonalização ###
  
  m1 = T1_matrixes(matrixes_list)

  M = matrixes_list[m1]
  if isinstance(matrixes_list[m1], Matriz_Simetrica):
    return  M.diagonalizacao()
  else:
    print("Matriz não Simetrica")



def Operador(matrixes_list):

  ### Programa para controlar e realizar as operações matriciais na lista ###

  controle = True

  while controle:

    result = None
    
    #Escolhe a operação
    p = input("Menu de Operações \n Digite 1 para somar \n Digite 2 para multiplicar por escalar \n Digite 3 para combinaçao linear \n Digite 4 para multiplicar matrizes \n Digite 5 para transpor uma matriz \n Digite 6 para calcular o traco \n Digite 7 para calcular o determinante \n Digite 8 para calcular a inversa \n Digite 9 para diagonalizar \n Digite 10 para terminar a operação \n")
    if tratamento_opcao(p,10):
      print("Opçao inválida")

    if p == '1':
      result = soma_matrizes(matrixes_list)
    if p == '2':
      result = escalar_mult(matrixes_list)
    if p == '3':
      result = combinacao_linear(matrixes_list)
    if p == '4':
      result = matrix_mult(matrixes_list)
    if p == '5':
      result = matrix_transp(matrixes_list)
    if p == '6':
      result = matrix_traco(matrixes_list)
    if p == '7':
      result = matrix_det(matrixes_list)
    if p == '8':
      result = matrix_inv(matrixes_list)
    if p == '9':
      result = matrix_diag(matrixes_list)
    if p == '10':
      controle = False
    if result != None:
       print(result)
    
    #se o resultado for uma Matriz oferece a opção de salvar
    if isinstance(result, Matriz):
      save = input("Digite 1 para adicionar a matriz a lista ou 2 para não salvar: ")
      while tratamento_numerico(save):
        save = input("Digite 1 para adicionar a matriz a lista: ")
      if save == '1':
        matrixes_list.append(result)

  globals().update(locals())
  return None

