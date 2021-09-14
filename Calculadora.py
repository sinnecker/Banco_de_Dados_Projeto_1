import classe_Matriz
from programas import* 
from rotinas import*

import numpy as np

def Calculadora():
  
  ### Menu principal da Calculadora ###


  #carrega ou inicia a lista de matrizes
  start = True
  while start:
    r = input("Continuar com a lista de matrizes salva anteiormente? (1 para sim / 2 para não)")
    if tratamento_opcao(r,2):
      print("Opção inválida")

    else:
      start = False
      if r == "1":
        matriz_list = lista_func()#carrega uma lista existente
      else:
        matriz_list = limpar_lista_func()#cria uma nova
        matriz_list = []
  Controle = True


  #Menu de Opções
  while Controle:
    option = input("Menu de Opções: \n Digite 1 para inserir uma nova matriz \n Digite 2 para apagar a uma matriz  \n Digite 3 para apagar todas as matrizes \n Digite 4 para operar as matrizes na lista \n Digite 5 para terminar o programa \n")
    if tratamento_opcao(option,5):
      print("Opção inválida")
    else:
      if option == '1':
        add_matrix(matriz_list)
        print(matriz_list)
      if option == '2':
        matriz_list = del_matrix(matriz_list)
        print(matriz_list)
      if option == '3':
        matriz_list = limpar_lista_func()
      if option == '4':
        Operador(matriz_list)
        print(matriz_list)
      if option == '5':
        save_file(matriz_list)
        Controle = False
    
  return None
  
Calculadora()
