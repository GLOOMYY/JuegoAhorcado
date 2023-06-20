from random import choice, shuffle
import json

def lecturaArchivo(nombre_archivo):
    """
    Lee el archivo JSON y lo guarda en un diccionario

    :args:
      nombre_archivo(str): Nombre del archivo JSON
    :return: 
      diccionario(dict): Diccionario con las palabras y categorías
    """

    with open(nombre_archivo, "r") as f:
      diccionario = json.load(f)
    return diccionario
 
def categorias(x):
  """
  Recibe una categoria y retorna un elemento aleatorio de la categoria
    
  :args:
    x(dict): Categorias y elementos
  
  :returns:
    y(str): elemento escogido
  """
  print("Revolviendo el listado de categorias...")
  categorias = list(x.keys())
  shuffle(categorias)
  
  print("Seleccionando al azar una categoria tematica")
  categoria = choice(categorias)
  print(f"La categoria seleccionada es: {categoria}")
  
  print(f"Revolviendo el listado de palabras dentro de la categoria {categoria}")
  values = x[categoria]
  shuffle(values)
  palabra = choice(values)
  
  return palabra, categoria

def bienvenida():
  """
  Da la bienvenida al juego
  
  :returns:
    nombre(str): Nombre del jugador
  """
  print("Bienvenid@ a nuestro juego\nUn juego donde muy seguramente perderas\nPara iniciar queremos concerte")
  nombre=input("¿Cual es tu nombre?\n")
  return nombre

def eleccion(nombre):
  """
  Pregunta al jugador cual modo prefiere
  
  :args:
    nombre(str): Nombre del jugador
  :returns:
    tipo(int): Tipo de juego
  """
  print(f"{nombre} este juego tiene dos modos:\nEl primero es el ahorcado y el segundo es la decapitacion instantanea")
  print("Por favor dinos que prefieres\n1. Ahorcado\n2. Guillotina")
  
  while True:
    tipo = int(input())
    
    if (tipo==1):
      print(f"Muy bien {nombre}, has elegido el ahorcado ")
      break
    elif (tipo==2):
      print(f"Muy bien {nombre}, has elegido la guillotina ")
      break
    else:
      print(f"{nombre} te estas pasando, ¿quieres jugar o no? ")
      
  return tipo

def ahorcado(palabra, categoria):
  """
  Mucho mas compleja :v
  
  :locals:
    abecedario(list): Lista con el abecedario que luego se desordena y es usada cuando el jugador elige una letra al azar
    posibilidades(dict): Diccionario con los dibujos del ahorcado
    intentos(int): Usado para romper el while
    errores(list): Almacena las letras erroneas
    correctas(list): Almacena las letras correctas
  
  :args:
    palabra(str): Palabra a adivinar
    categoria(str): Categoria de la palabra
    
  :returns:
    No retorna, solo imprime si gana o pierde
    
  """
  
  abecedario = ['a','b','c','d','e','f','g','h','i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  shuffle(abecedario)
  posibilidades = lecturaArchivo("ahorcado.json")
  print("Tienes 7 intentos")
  intentos=0
  errores = []
  correctas = []
  
  while intentos <7:
    print(f"Categoria: {categoria}")
    print(f"Palabra: {''.join([letra if letra in correctas else '_' for letra in palabra])}") # Imrpime guiones y las letras correctas que se hayan dicho
    print("Letras fallidas: "+", ".join(errores)) # Imprime las letras incorrectas
    letra = str(input("Indique una letra o pulse (+) para elegir una letra al azar "))
    
    if letra=='+': # Si elige una letra al azar se selecciona una letra aleaotoria del abecedario y se elimina para que no vuelva a salir
      letra = choice(abecedario)
      abecedario.remove(letra)
      print(f"La letra escogida al azar es: {letra}")
    
    if (letra in correctas) or (letra in errores): # Revisa si la letra ingresada ya fue usada
      print("Esa letra ya la dijiste")
      continue # Si ya fue usada omite el resto del ciclo
      
    if letra in palabra: # Revisa si es correcta o no la letra ingresada
      print("¡Muchachos! detengan el montaje del cadalso por ahora")
      correctas.append(letra)
    else:
      print("Lo lamento, pero comenzó el montaje del cadalso")
      errores.append(letra)
      intentos+=1
      
    if intentos>0: # Si ya se equivocó al menos 1 vez se empieza a dibujar el ahorcado
      print(posibilidades[str(intentos)])
  
  if intentos==7:
    print(f"La palabra era {palabra}")
  elif intentos<7:
    print(f"Felicidades, la palabra era {palabra}")

def guillotina(palabra, categoria):
  """
    Casi lo mismo de la funcion anterior
  
  :locals:
    abecedario(list): Lista con el abecedario que luego se desordena y es usada cuando el jugador elige una letra al azar
    posibilidades(dict): Diccionario con los dibujos del ahorcado
    intentos(int): Usado para romper el while
    errores(list): Almacena las letras erroneas
    correctas(list): Almacena las letras correctas
  
  :args:
    palabra(str): Palabra a adivinar
    categoria(str): Categoria de la palabra
    
  :returns:
    No retorna, solo imprime si gana o pierde
    
  """
  abecedario = ['a','b','c','d','e','f','g','h','i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  shuffle(abecedario)
  posibilidades = lecturaArchivo("guillotina.json")
  print("Tienes 7 intentos")
  intentos=0
  errores = []
  correctas = []
  
  while intentos <7:
    print(f"Categoria: {categoria}")
    print(f"Palabra: {''.join([letra if letra in correctas else '_' for letra in palabra])}")
    print("Letras fallidas: "+", ".join(errores))
    letra = str(input("Indique una letra o pulse (+) para elegir una letra al azar "))
    if letra=='+':
      letra = choice(abecedario)
      abecedario.remove(letra)
      print(f"La letra escogida al azar es: {letra}")
    
        
    if (letra in correctas) or (letra in errores):
      print("Esa letra ya la dijiste")
      continue
      
    if letra in palabra:
      print("¡Muchachos! detengan el montaje de la guillotina por ahora")
      correctas.append(letra)
    else:
      print("Lo lamento, pero comenzó el montaje de la guillotina")
      errores.append(letra)
      intentos+=1
    if intentos>0:
      print(posibilidades[str(intentos)])
  
  if intentos==7:
    print(f"La palabra era {palabra}")
  elif intentos<7:
    print(f"Felicidades, la palabra era {palabra}")

def main():
  """
  Funcion principal que invoca las demas funciones en el orden requerido
  """
  
  nombre = bienvenida()
  tipo  = eleccion(nombre)
  palabra, categoria = categorias(lecturaArchivo("palabras.json"))
  print("Ahora te enseñaremos la interfaz de juego")
  if (tipo==1):
    print("Esta es la interfaz del ahorcado")
    ahorcado(palabra, categoria)
  elif (tipo==2):
    print("Esta es la interfaz de la guillotina")
    guillotina(palabra, categoria)

while True:
  main()
  print("¿Deseas volver a jugar?\n1 para no\nCualquier numero para si")
  x = int(input())
  if (x==1): 
    break
