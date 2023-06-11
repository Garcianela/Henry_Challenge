# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

'''
    Esta función recibe como argumento un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:
    
def numeroBinario(numero):#Función creada que recibe un número entero"

   if type(numero)!=int: #No se permite un número 
        return "No se permite un número distinto a entero, ingrese un número entero por favor"
   
   if numero<0: #No se permite un número menor a cero
        return "Ingrese un número mayor a cero, por favor"

   modulos=[]
   while ( numero != 0): #Número mayor hacer se realiza la repesentación binaria 
        modulo=numero%2
        cociente=numero//2
        modulos.append(modulo) #Se obtiene la lista de módulos
        numero=cociente
        lista=int(modulos)
        lista.sort(reverse=True) #Se ordena la lista de mayor a menor

   print(modulos)
      
def dividirMultiplicar(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar una lista con los siguientes parámetros:
   1.Los números que sean positivos y pares se deben dividir por 2, y el resultado expresado como entero (sin decimales, no redondeando, debe tomar sólo la parte entera de la división por 2).
   2.Los números negativos multiplicados por 2.
   3.Los que no cumplan los criterios anteriores deben quedar igual al valor original.
   4.Ordernar los números de mayor a menor.
   Ej: dividirMultiplicar([2,4,1,-3]): debe retornar: [2, 1, 1, -6]
   '''   
   #Tu código acá

def dividirMultiplicar(lista):
  
  lista_positivos=[] # Lista vacía para almacenar números positivos y pares
  lista_negativos=[] # Lista vacía para almacenar número negativos
  lista_elementos=[] # Lista vacía para almacenar los números que no cumplen las dos condiciones anteriores

  for i in lista: # Bucle para números positivos y pares
    if i>0 and i%2==0:
      cociente=i//2
      lista_positivos.append(cociente)

  for i in lista:# Bucle para números negativos
    if i<0:
      multiplica=i*2
      lista_negativos.append(multiplica)

  for i in lista: # Bucle para los números que no cumplen las dos condiciones anteriores
      if i>0 and i%2 != 0:
        elemento=i
        lista_elementos.append(elemento)

  general=lista_positivos+lista_negativos+lista_elementos #concatenado de listas

  lista_secundaria=general
  lista_secundaria.sort(reverse=True) #Se ordena la lista de mayor a menor

  print(lista_secundaria)

def crearDiccionario(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar un diccionario con tres claves, "multiplos3", 'cuadrados", "menores_promedio".
   Para la clave "multiplos3", el valor debe ser una lista con los múltiplos de 3 de la lista original.
   Para la clave "cuadrados", el valor debe ser una lista con los valores de la lista original elevados al cuadrado.
   Para la clave "menores_promedio", el valor debe ser una lista con los valores menores al promedio de la lista original.
   EJ: crearDiccionario([3,6,7,12]): debe retornar: {'multiplos3': [3, 6, 12], 'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}
   '''
   #Tu código acá

def crearDiccionario(lista):

   multiplos3=[] # Creamos una lista vacía, donde vamos a ir completando los multiplos de 3
   cuadros=[] # Creamos una lista vacía, donde vamos a ir completando los potencias de la lista
   promedio=[] # Creamos una lista vacía, donde vamos a ir completando los números menores a promedio

   for i in lista: 
      if i%3 == 0:
         multiplos3.append(i)
    
   for i in lista:
      potencia = i**2
      cuadros.append(potencia)

   elementos=len(lista)
   suma_elem=sum(lista)
   prom=suma_elem/elementos
   for i in lista:
      if i<prom:
         promedio.append(i)

      miDic={"multiplos3":multiplos3,"Cuadros":cuadros,"menores_promedio":promedio}

   return miDic

def trianguloRectangulo(a,b,c):
   '''
   La función debe recibir como argumentos el valor en cm de los lados de un triángulo (a y b son los catetos), y dado estos valores, retornar True si en efecto corresponden a un triángulo rectángulo, o False en caso contrario. Sólo se debe poder pasar valores enteros como argumentos de la función, caso contrario debe retornar nulo.
   EJ: trianguloRectangulo(3.5,3.5,2.4), debe retornar nulo
   EJ: trianguloRectangulo(3,3,3), debe retornar False
   EJ: trianguloRectangulo(3,4,5), debe retornar True
   '''
   #Tu código acá
def trianguloRectangulo(a,b,c): # Se introduce los parámetros de a,b,c

    potencia_a=a**2 # Cateto a al cuadrado
    potencia_b=b**2 # Cateto b al cuadrado
    potencia_c=c**2 # Cateto c al cuadrado

    suma=potencia_a+potencia_b # sumamos los catetos de acuerdo a Pitagoras

    if potencia_c == suma: # Condicional si se cumple Pitagoras
        print(True) # En caso de ser triángulo rectangulo imprime True
    
    else:
        return print("False") # En caso de no ser triángulo rectangulo imprime False   

def ciudadesPoblacion(diccionario):
   '''
   Dado el siguiente diccionario ciudades, la función debe retornar una lista de listas, donde cada elemento de la lista sea una lista con el par ['ciudad', población], pero sólo de las ciudades que comiencen con la letra 'B', y como último elemento de la lista el par ['promedio', promedio de población] con el promedio de población de las ciudades seleccionadas.
   Ej: Si se pidiera ciudades que comiencen con la letra 'S', debe devolver: [['São Paulo', 21048514], ['Santiago de Chile', 7112808],['promedio', 14080661.0]]

   ciudades = {
      'São Paulo': 21048514,
      'Buenos Aires': 14975587,
      'Río de Janeiro': 11902701,
      'Bogotá': 10777931,
      'Lima': 10479899,
      'Santiago de Chile': 7112808,
      'Belo Horizonte': 6006091,
      'Caracas': 5622798,
      'Brasília': 4291577
      }
      Pista: investigar método de string startswith()
   '''
   #Tu código acá

   #def ciudadesPoblacion(diccionario):

    #elementos=(diccionario.items())
   #return 'Funcion incompleta'#

def ordenarPalabras(palabras):
   '''
   La función recibe como argumento una secuencia de palabras unidas por guiones, y debe retornar las mismas palabras, unidas por guiones, pero en orden alfabético. Si el argumento que se le pasa no es un string o no contiene guiones, debe retornar nulo.
   EJ: ordenarPalabras('saco-libro-casa') debe retornar 'casa-libro-saco'
   EJ: ordenarPalabras('Hola') debe retornar nulo
   Pista: investigar métodos de string
   '''
   #Tu código acá

def ordenarPalabras(palabras):
   palabra_separada=palabras.split("-") # Se empleo el método split para separar la palabra
   palabra_separada.sort() # Fue empleado para ordenar la palabra
   union=palabra_separada
   i="-".join(union)  # Empleado para unir palabras
   return print(i)

def stringEspejo(texto):
    '''
    La función recibe como argumento una cadena de texto y retorna la cadena invertida, pero sólo si tiene más de tres caracteres, sino debe retornar nulo.
    EJ: stringEspejo('Hola Mundo') debe retornar 'odnuM aloH'
    EJ: stringEspejo('Hoy') debe retornar nulo
    '''
    #Tu código acá

def stringEspejo(texto):
   resultado="" # Creamos la variable que vamos a ir completar al ejecutar el while
   indice=len(texto) # Obtenemos el tamaño de la cada de texto

   while indice > 0: # Realizamos la iteración de los caracteres del texto
      resultado += texto[indice-1] # Vamos completando el texto
      indice-=1 # Realizamos un decremento a la variable del bucle
   return print(resultado) # Imprimos el resultado