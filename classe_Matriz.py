import numpy as np
from rotinas import*

# Calsse Principal ####################################################
class Matriz:

  def __init__(self, linhas, colunas):
    
    ### Iniciando a matriz ###
    
    self.tamanho = (linhas, colunas)#dimensão
    self.dados   = np.empty(linhas*colunas)#aloca o espaço em um array flat
  
  def Set_Aij(self, i, j, dado):
    
    ### Atribui ao elemento (i,j) o dado passado ###
    self.dados[i*self.tamanho[1]+j] = dado
  
  def get_data(self):

    ### Retorna o elemnto (i,j) da matriz ###

    s = str(self.tipo)
    s+='; '
    s+= str(self.tamanho[0])+'x'+str(self.tamanho[1])
    s+='; '
    for n in self.dados[:-1]:
      s+=str(n)+','
    s+= str(self.dados[-1])
    return s


  def dados_to_numpy(self):

    ### Transforma os dados em matriz do numpy ###

    npMatrix = np.empty(self.tamanho)

    for i in range(self.tamanho[0]):
      for j in range(self.tamanho[1]):
        npMatrix[i][j] = self.Get_Aij(i,j)
    return npMatrix

  def transpose(self):

    ### Calcula a transposta ###

    if self.tipo == 1:
      aux = Matriz_Retangular(self.tamanho[1],self.tamanho[0])
    else:
      n = self.tamanho[0]
    if self.tipo == 2:
      aux = Matriz_Quadrada(n)
    if self.tipo == 3:
      aux = Matriz_Simetrica(n)
    if self.tipo == 4:
      aux = Matriz_Triangular_Superior(n)
    if self.tipo == 5:
      aux = Matriz_Triangular_Inferior(n)
    if self.tipo == 6:
      aux = Matriz_Diagonal(n)

    for i in range(self.tamanho[0]):
      for j in range(self.tamanho[1]):
        aux.Set_Aij(j, i, self.Get_Aij(i, j))
    return aux

  def Read_data(self, data):

    ### Le os dados de um array flat e passa para o objeto ###

    linhas,colunas = self.tamanho
    for i in range(linhas):
      for j in range(colunas):
        self.Set_Aij(i, j, data[i*colunas + j])
  
  def Get_Aij(self, i, j):

    ### Retorna o elemento (i,j) da matriz ###
    
    return self.dados[i*self.tamanho[1]+j]
  
  def __str__(self):
    
    ### Retorna os dados como string em forma de matriz ###
    
    m = self.dados_to_numpy()
    return str(m)
  
  def __repr__(self):
   
   ### retorna as informações do objeto ###
   return "Matriz %i %i"%self.tamanho +"\n "+ str(self)
  
  def __add__(self, B):
    
    ### Soma de matrizes ###
    if self.tamanho != B.tamanho:
      print("Tamanhos incompatíveis")
      return None
    else:
      linhas, colunas = self.tamanho
      Soma = Matriz(linhas, colunas)
      for i in range(linhas):
        for j in range(colunas):
          dado = self.Get_Aij(i, j) + B.Get_Aij(i, j)
          Soma.Set_Aij(i, j, dado) 
      return Soma
  
  def __mul__(self, escalar):

      ### multiplicação matricial e escalar ###
        
        if   isinstance(escalar, int) or  isinstance(escalar,float):
            data = self.dados*escalar
            if self.tipo>1:
                MultEsc = self.__class__(self.tamanho[0])
            else:
                MultEsc = self.__class__(self.tamanho[0],self.tamanho[1])
            MultEsc.Read_data(data)
            return MultEsc
        if isinstance(escalar, Matriz):
            print("matrix mult")
            if escalar.tamanho[0]!=self.tamanho[1]:
                print("Tamanhos inválidos")
            
            else:
                if escalar.tamanho[1]!=self.tamanho[0]:
                    MultEsc = Matriz_Retangular(self.tamanho[0],escalar.tamanho[1])
                else:
                    MultEsc = Matriz_Quadrada(self.tamanho[0])
                        
                m1 = self.dados_to_numpy()
                m2 = escalar.dados_to_numpy()
                
                data = m1@m2
                data = data.flatten()
                
                MultEsc.Read_data(data)
                
                return MultEsc 
        else:
            raise Exception("Not implemented")

                
        
            
  def __rmul__(self,escalar):

      ### multiplicação pela direita de escalar ###
        
        if   isinstance(escalar, int) or  isinstance(escalar,float):
            return self*escalar
        else:
            raise Exception("Not implemented")


# Matriz Retangulares ##########################################################

class Matriz_Retangular(Matriz):

  def __init__(self,linhas,colunas):
    self.tamanho = (linhas, colunas)
    self.tipo    = 1
    self.dados   = np.empty(linhas*colunas)

# Matriz Quadrada ##############################################################
class Matriz_Quadrada(Matriz):
  def __init__(self,n):
    self.tamanho = (n, n)
    self.tipo    = 2
    self.dados   = np.empty(n**2)

  def traco(self):
    ### Traço da matriz ###
    return sum(self.dados[::n])

  def det(self):

    ### Determinante da matriz ###
    
    l = self.dados_to_numpy()
    return np.linalg.det(l)

  def inversa(self):

    ### Calcula a matriz inversa ###
    
    l = self.dados_to_numpy()
    l = np.linalg.inv(l)
    n,_ = self.tamanho
    inv = Matriz_Quadrada(self.tamanho[0])
    for i in range(n):
      for j in range(n):
        inv.Set_Aij(i, j, l[i][j])
    
    return inv
    


# Matrix Simetrica #############################################################
class Matriz_Simetrica(Matriz_Quadrada):
  def __init__(self,n):
    self.tamanho = (n, n)
    self.tipo    = 3
    self.dados   = np.empty(n*(n+1)//2)

  def traco(self):
    
    ### Calcula o traço para matrizes simétricas###
    
    diag = [self.dados[i*(i+1)//2 + i] for i in range(self.tamanho[0])]
    return sum(diag)

  def diagonalizacao(self):

    ### Calcula a diagonalização ###

    l = self.dados_to_numpy()
    eigen_values, p = np.linalg.eig(l)
    D = np.diag(eigen_values)
    P = p.T
    P_inv = np.linalg.inv(P)
    print(P, D, P_inv)

  def Get_Aij(self, i, j):
    
    ### Atribui ao elemento (i,j) o dado passado ###
    
    if i<=j:
      return self.dados[i*(i+1)//2+j]
    else:
      return self.dados[j*(j+1)//2+i]

  def Set_Aij(self, i, j, dado):
    ### Atribui ao elemento (i,j) o dado passado ###
    if i<=j:
      self.dados[i*(i+1)//2+j] = dado
    else:
      self.dados[j*(j+1)//2+i] = dado

  def Read_data(self, data):

    ### Le os dados de um array flat ###

    linhas,colunas = self.tamanho
    for i in range(linhas):
      for j in range(i+1):
        self.Set_Aij(i, j, data[i*(i+1)//2 + j])

  def __add__(self, B):
    
    ### Soma de matrizes ###
    
    if self.tamanho != B.tamanho:
      print("Tamanhos incompatíveis")
      return None
    else:
      linhas, colunas = self.tamanho
      if isinstance(B, Matriz_Simetrica):
        Soma = Matriz_Simetrica(linhas)
        for i in range(linhas):
          for j in range(i+1):
            dado = self.Get_Aij(i, j) + B.Get_Aij(i, j)
            Soma.Set_Aij(i, j, dado)
        return Soma
      else:
        data = np.empty(linhas*colunas)
        for i in range(linhas):
          for j in range(colunas):
            data[i*colunas+j] = self.dados[i*colunas+j] + B.Get_Aij(i,j)
        Soma = Matriz(linhas, colunas)
        Soma.Read_data(data.reshape(self.tamanho))
        return Soma


# Matriz Triangular Superior ###################################################

class Matriz_Triangular_Superior(Matriz_Quadrada):
  def __init__(self,n):
    self.tamanho = (n, n)
    self.tipo    = 5
    self.dados   = np.empty(n*(n+1)//2)

  def traco(self):

    ### Calcula o traço ###

    diag = [self.dados[i*(i+1)//2 + i] for i in range(self.tamanho[0])]
    return sum(diag)

  def Set_Aij(self, i, j, dado):
    
    ### Atribui ao elemento (i,j) o dado passado ###
    
    if i<=j:
      self.dados[j*(j+1)//2+i] = dado
    else:
      print("Matriz tringular superior")

  def Get_Aij(self, i, j):
    
    ### Retorna o elemento (i,j) ###

    if i<=j:
      return self.dados[j*(j+1)//2+i]
    else:
      return 0

  def Read_data(self, data):

    ### Le os dados de um array flat ###

    linhas,colunas = self.tamanho
    for i in range(linhas):
      for j in range(i+1):
        self.Set_Aij(j, i, data[j*(j+1)//2 + i])

  def __add__(self, B):
    
    ### Soma de matrizes ###

    if self.tamanho != B.tamanho:
      print("Tamanhos incompatíveis")
      return None
    else:
      linhas, colunas = self.tamanho
      if isinstance(B, Matriz_Triangular_Superior):
        Soma = Matriz_Triangular_Superior(linhas)
        for i in range(linhas):
          for j in range(i+1):
            dado = self.Get_Aij(j, i) + B.Get_Aij(j, i)
            Soma.Set_Aij(j, i, dado)
        return Soma
      else:
        Soma = Matriz_Quadrada(linhas)
        for i in range(linhas):
          for j in range(colunas):
            dado = self.Get_Aij(i, j) + B.Get_Aij(i, j)
            Soma.Set_Aij(i, j, dado)
        return Soma


# Matriz Triangular Inferior ###################################################

class Matriz_Triangular_Inferior(Matriz_Quadrada):
  def __init__(self,n):
    self.tamanho = (n, n)
    self.tipo    = 4
    self.dados   = np.empty(n*(n+1)//2)

  def traco(self):

    ### Calcula o traço ###

    diag = [self.dados[i*(i+1)//2 + i] for i in range(self.tamanho[0])]
    return sum(diag)

  def Set_Aij(self, i, j, dado):
      
    ### Atribui ao elemento (i,j) o dado passado ###
    
    if i>=j:
      self.dados[i*(i+1)//2+j] = dado
    else:
      print("Matriz tringular inferior")

  def Get_Aij(self, i, j):
    
    ### Retorna o elemento (i,j) ###

    if i>=j:
      return self.dados[i*(i+1)//2+j]
    else:
      return 0

  def Read_data(self, data):
    linhas,colunas = self.tamanho
    for i in range(linhas):
      for j in range(i+1):
        self.Set_Aij(i, j, data[i*(i+1)//2 + j])

  def __add__(self, B):
    
    ### Soma de matrizes ###

    if self.tamanho != B.tamanho:
      print("Tamanhos incompatíveis")
      return None
    else:
      linhas, colunas = self.tamanho
      if isinstance(B, Matriz_Triangular_Inferior):
        Soma = Matriz_Triangular_Inferior(linhas)
        for i in range(linhas):
          for j in range(i+1):
            dado = self.Get_Aij(i, j) + B.Get_Aij(i, j)
            Soma.Set_Aij(i, j, dado)
        return Soma
      else:
        Soma = Matriz_Quadrada(linhas)
        for i in range(linhas):
          for j in range(colunas):
            dado = self.Get_Aij(i, j) + B.Get_Aij(i, j)
            Soma.Set_Aij(i, j, dado)
        return Soma


# Matriz Diagonal ##############################################################

class Matriz_Diagonal(Matriz_Simetrica):
  def __init__(self,n):
    self.tamanho = (n, n)
    self.tipo    = 6
    self.dados   = np.empty(n)

  def traco(self):

    ### Calcula o traço ###

    return sum(self.dados)

  def Set_Aij(self, i, j, dado):
    
    ### Atribui ao elemento(i,j) o dado passado ###

    if i==j:
      self.dados[i] = dado
    else:
      print("Matriz Diagonal")

  def Get_Aij(self, i, j):
    
    ### Retorna o elemento (i,j) ###
    
    if i==j:
      return self.dados[i]
    else:
      return 0

  def Read_data(self, data):

    ### Le os dados de um array flat ###

    linhas,colunas = self.tamanho
    for i in range(linhas):
      self.Set_Aij(i, i, data[i])

  def __add__(self, B):
    
    ### Soma de matrizes ###

    if self.tamanho != B.tamanho:
      print("Tamanhos incompatíveis")
      return None
    else:
      linhas, colunas = self.tamanho
      if isinstance(B, Matriz_Diagonal):
        Soma = Matriz_Diagonal(linhas)
        for i in range(linhas):
          dado = self.Get_Aij(i, i) + B.Get_Aij(i, i)
          Soma.Set_Aij(i, i, dado)
        return Soma
      else:
        Soma = Matriz_Quadrada(linhas)
        for i in range(linhas):
          for j in range(colunas):
            dado = self.Get_Aij(i, j) + B.Get_Aij(i, j)
            Soma.Set_Aij(i, j, dado)
        return Soma

