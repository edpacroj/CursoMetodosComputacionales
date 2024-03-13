# -*- coding: utf-8 -*-
"""Lab02_python_basico02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OAnq8dhj3BO8yAum4lk4OamREMaqU-54

<a href="https://colab.research.google.com/github/hernansalinas/autogrades/blob/main/Laboratorios_Taller/Lab02_python_basico02.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>


# Laboratorio 02
### Métodos computacionales para físicos  y astrónomos
### Universidad de Antioquia
### Prof: Hernan D. Salinas Jiménez
"""

# Ejecutar esta celda antes de cada laboratorio
!git clone https://github.com/hernansalinas/autogradesMetodosComputacionales.git

# Commented out IPython magic to ensure Python compatibility.
# Ejecutar esta celda antes de cada laboratorio
path="autogradesMetodosComputacionales/Laboratorios_Taller/libs"
pathL="autogradesMetodosComputacionales/Laboratorios_Taller/libs/Lab_02"
# %run -i {path}/libUnitTest.py

"""## Problemas

### Factorial
1. Elaborar un algoritmo e implementar en python, el factorial de un número entero `n` ingresado por el usuario.

1. Si el número es un entero deberá retornal el factorial del número.
2. Si el número es negativo deberá aparecer un mensaje tipo string con el mensaje  "el número no puede ser negativo"

3. Si el número es pertenece a los reales(float) el mensaje será, el número no puede ser real.


     ### Ejemplo de Ejecución
    ```python

    >>> factorial(3)
        6

    >>> factorial(1987123)
        =???
```

"""

def fac(n):
 if n<0 or type(n)==float:
  return 'el número no puede ser real o negativo'
 if n==1 or n==0:
  return 1
 if type(n)==int:
  count= n*fac(n-1)
 return (count)

fac(3)
#factorial = 1
          #  for i in range(1, n + 1):
           #     factorial *= i
            #return factorial

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test01.py
def fac(n):
 if n<0 or type(n)==float:
  return 'el número no puede ser real o negativo'
 if n==1 or n==0:
  return 1
 if type(n)==int:
  count= n*fac(n-1)
 return (count)

fac(5)

"""### Teoria de números

Los enunciados 2 y 3 se refieren a la siguiente información:

Diseñar un programa en el que entrado  un numero `a`  retorne una variable booleana True or false si cumple que es:

2. [Números defectivo](https://es.wikipedia.org/wiki/Número_defectivo) : la suma de los divisores propios es menor que el número.

  La rutina se deberá llamar números_defectivos



3. [Números abundantes](https://es.wikipedia.org/wiki/Número_abundante): la suma de los divisores es mayor que el número.

  La rutina se deberá llamar números_abundantes



4. [Números semiperfectos](https://es.wikipedia.org/wiki/N%C3%BAmero_semiperfecto) la suma de todos o algunos de los divisores propios es igual al número.

  La rutina se debera llamar numeros_semiperfectos

5. [Números perfectos](https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto) la suma de todos sus divisores propios, excepto el mismo numero, es igual al número.

   La rutina se deberá llamar numeros_perfectos


6. [Números primos](https://es.wikipedia.org/wiki/N%C3%BAmero_primo) el número es divisible unicamente por sí mismo y por 1.
   La rutina se deberá llamar numeros_primos


Problema no obligatorio:

P1. Retornar los 30 primeros números de cada clase
"""

#Números defectivo : la suma de los divisores propios es menor que el número.La rutina se deberá llamar números_defectivos
#int(input())
def numeros_defectivos(a):
  L=[]
  for i in range(1,a):
    n=a%i
    if n==0:
      L.append(i)
  return L

numeros_defectivos(6)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test02.py
#Números defectivo : la suma de los divisores propios es menor que el número.La rutina se deberá llamar números_defectivos
#int(input())
def numeros_defectivos(a):
  L=[]
  for i in range(1,a):
    n=a%i
    if n==0:
      L.append(i)
  if sum(L)<a:
    return True
  if sum(L)>a:
    return False
numeros_defectivos(2)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test03.py
#Numeros abundantes,suma los divisores
def numeros_abundantes(a):
  A=[]
  for i in range(1,a):
    n=a%i
    if n==0:
      A.append(i)
  if sum(A)>a:
    return True
  if sum(A)<a:
    return False

numeros_abundantes(4)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test04.py
#semiperfectos:la suma de todos o algunos de los divisores propios es igual al número.
from itertools import combinations
def divisores_propios(a):
  d=[]
  for i in range(1, a):
    if a%i==0:
      d.append(i)
  return d
def numeros_semiperfectos(a):
  n=divisores_propios(a)
  S=[]
  for i in range(2, len(n)+1):
    comb=list(combinations(n,i))
    S.append(comb)
  for j in range(len(S)): #
    for k in range(len(S[j])):
      if sum(S[j])==a:
        return True
  else:
    return False

divisores_propios(20)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test05.py
#perfectos
def numeros_perfectos(a):
  P=[]
  for i in range(1,a):
    n=a%i
    if n==0:
      P.append(i)
  if sum(P)==a:
    return True
  if sum(P)>a or sum(P)<a:
    return False

numeros_perfectos(6)

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test06.py
#primos
def numeros_primos(a):
  C=[]
  for i in range(1,a):
    n=a%i
    if n==0:
      return True
    if n>=0:
      return False

numeros_primos(8)

"""
7. Diseñar un programa en el que entrado dos números `a`  y `b` retorne una variable booleana **True** o **false**.

  [Números amigos](https://es.wikipedia.org/wiki/N%C3%BAmeros_amigos) `a` y `b` tales que a es la suma de los divisores propios de `b` y viceversa.
    La rutina se debera llamar numeros_amigos




P2. Retornar los 10 primeros pares de numeros perfectos, semiperfectos, amigos

"""

a=int(input())
b=int(input())

# Commented out IPython magic to ensure Python compatibility.
# %run -i {pathL}/test07.py
def numeros_amigos(a,b):
  m=divisores_propios(a)
  n=divisores_propios(b)
  if sum(m)==b and sum(n)==a:
     return True
  else:
    return False
numeros_amigos(2,6)

"""3. Determine si un número `n` entero ingresado por el usuario es un [palíndromo](https://en.wikipedia.org/wiki/Palindromic_number), (Retorne `True` en caso afirmativo y `False` en caso contrario)

```python


    >>> palindromo(3333333)
        True

    >>> palindromo(2323)
        True
        
    >>> palindromo(1111349111111)
        False
```



"""

def palindromo(a):
   invertir = str(a)
   n = int(invertir[::-1])
   if n == a:
    return True
   else:
    return False

palindromo(2424242)

"""8 Construir un programa en el que  entrado un arreglo de números se  ordenen de forma ascendente, Ver algoritmo
[Quicksort](https://es.wikipedia.org/wiki/Quicksort).


```python


<<< v = [22, 32, 42, 12, 22, 31, 41, 11, 12, 232, 24, 12, 22]
<<< def quicksort(v):

<<<     return v
<<< w = print(quicksort(v))
<<< [11, 12, 12, 12, 22, 22, 22, 24, 31, 32, 41, 42, 232]

```

Sólo para comprobar tu código,  puedes hacer uso del comando sort de python.
```python
<<< b = [22, 32, 42, 12, 22, 31, 41, 11, 12, 232, 24, 12, 22]

<<< print(b.sort())

<<< [11, 12, 12, 12, 22, 22, 22, 24, 31, 32, 41, 42, 232]
```
"""

import numpy as np

v=list(np.random.randint(0,50, 10))
def quicksort(v):
    n = len(v)
    for i in range(n):
        indice = i
        for j in range(i+1, n):
            if v[j] < v[indice]:
                indice = j
        v[i], v[indice] = v[indice], v[i]
    return v

quicksort(v)

print(np.sort(v))