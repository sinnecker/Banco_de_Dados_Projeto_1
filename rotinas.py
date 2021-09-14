import numpy as np


#Rotinas de opções #############################################################

def tratamento_numerico(a):
  
 ### Trata erros de entrada numérica ###

  try:
    a = float(a)
    return False
  except ValueError:
    print("Entrada inválida")
    return True

def tratamento_opcao(a,n):
  
  ### Recebe uma opção e o número de opções e verifica se houve erro de entrada ###
  
  if a not in [str(i+1) for i in range(n)]:
    return True
  else:
    return False

def T2_matrixes(matrixes_list):
  
  ### Seleciona 2 matrizes na lista ###
  
  controle = True

  while controle:

    escolha = input("Entre o indice da primeira matriz: ")
    
    if int(escolha) >= len(matrixes_list):
    
      print("Índice não contido na lista de matrizes, insira outro")

    else:
      controle = False

  m1 = int(escolha)
  controle = True

  while controle:

    escolha = input("Entre o indice da segunda matriz: ")

    if int(escolha) >= len(matrixes_list):
      print("Índice não contido na lista de matrizes, insira outro")

    else:
      controle = False

  m2 = int(escolha)

  return m1,m2

def T1_matrixes(matrix_list):
  
  ### Seleciona 1 matriz na lista ###
  controle = True

  while controle:

    escolha = input("Entre o indice da matriz: ")

    if int(escolha) >= len(matrix_list):
      print("Índice não contido na lista de matrizes, insira outro")

    else:
      controle = False

  m1 = int(escolha)

  return m1
#Rotinas para inserir matrizes #################################################

def add_regular(M):
  
  ### Recebe as entradas de elementos em matrizes retangulares e quadradas ###
  
  linhas,colunas = M.tamanho
  for i in range(linhas):
    for j in range(colunas):
      dado = input("Digite o elemento %s,%s da matriz"%(i,j))
      while tratamento_numerico(dado):
        dado = input("Digite o elemento %s,%s da matriz"%(i,j))
      M.Set_Aij(i, j, dado)
  return None

def add_simetric(M):
  
  ### Recebe a enrtada de elementos em uma matriz simétrica ###
  n,_ = M.tamanho
  for i in range(n):
    for j in range(i+1):
      dado = input("Digite o elemento %s,%s da matriz"%(i,j))
      while tratamento_numerico(dado):
        dado = input("Digite o elemento %s,%s da matriz"%(i,j))
      M.Set_Aij(i, j, dado)
  return None

def add_triangular(M,tr="inf"):
  
  ### Recebe a enrtada de elementos em uma matriz triangular ###

  n,_ = M.tamanho
  if tr=="sup":#superior
    for i in range(n):
      for j in range(i+1):
        dado = input("Digite o elemento %s,%s da matriz"%(j,i))
        while tratamento_numerico(dado):
          dado = input("Digite o elemento %s,%s da matriz"%(j,i))
        M.Set_Aij(j, i, dado)
  else:#inferior
    add_simetric(M)
  return None

def add_diag(M):

  ### Recebe a enrtada de elementos em uma matriz Diagonal ###

  n,_ = M.tamanho
  for i in range(n):
    dado = input("Digite o elemento %s,%s da matriz"%(i,i))
    while tratamento_numerico(dado):
      dado = input("Digite o elemento %s,%s da matriz"%(i,i))
    M.Set_Aij(i, i, dado)
  return None

# Rotinas de operação ##########################################################
def soma_matrizes(matrixes_list):
  
  ### Escolhe 2 matrizes na lista e retorna a soma ###
  
  m1,m2 = T2_matrixes(matrixes_list)

  result = matrixes_list[m1] + matrixes_list[m2]

  return result

def escalar_mult(matrixes_list):
  
  ### Escolhe uma matriz e multiplica por escalar ###
  
  m1 = T1_matrixes(matrixes_list)

  escalar = input("Digite o escalar: ")

  result = matrixes_list[m1] * float(escalar)

  return result

def matrix_mult(matrixes_list):
  
  ### Escolhe 2 matrizes e calcula o produto matricial ###
  
  m1,m2 = T2_matrixes(matrixes_list)

  result = matrixes_list[m1] * matrixes_list[m2]

  return result

def matrix_transp(matrixes_list):
  
  ### Escolhe 1 matriz e calcula a transposta ###
  
  m1 = T1_matrixes(matrixes_list)
  M = matrixes_list[m1]
  result = M.transpose()

  return result


def combinacao_linear(matriz_list):
  
  ### Rotina para calcular a combinação linear de matrizes na lista ###
  
  add_matriz_operacao = True

  matriz_index_list = []
  
  #Escolhe as matrizes
  while add_matriz_operacao:
    escolha = input("Insira o índice da matriz a ser operada : ")
    
    if int(escolha) >= len(matriz_list):
      print("Índice não contido na lista de matrizes, insira outro")
    
    elif int(escolha) in matriz_index_list:
      print("Matriz já escolhida para operação") 
    
    else:
      matriz_index_list.append(int(escolha))
    
    q = input("Deseja operar mais matrizes? (1 para sim / 2 para não)") 
    while tratamento_opcao(q,2):
      print("opção inválida")
      q = input("Deseja operar mais matrizes? (1 para sim / 2 para não)")

    if q == "2":
      add_matriz_operacao = False
  
  result = []

  #Mosta os indices das matrizes selecionadas
  print("Combinação linear da matrizes: ")
  print(matriz_index_list)
  
  #Escolhe os escalares de cada matriz
  for j in range(len(matriz_index_list)):
    q = input("Insira os coeficientes da matriz %s: "%matriz_index_list[j])
    while tratamento_numerico(q):
      print("Entrada inválida")
      q = input("Insira os coeficientes da matriz %s: "%matriz_index_list[j])

    q = float(q)
    result.append(matriz_list[matriz_index_list[j]] * q)
    
  #Calcula o resultado
  if len(result)<=1:
    return result[0]
  else:
    soma = result[0]+result[1]
    for matrix in result[2:]:
      soma = soma + matrix
    return soma
