# -------------- FUNCION SUMAR -------------- 
def sumar(a , b):
  return a + b

# -------------- FUNCION RESTAR -------------- 
def restar(a , b):
  return a - b


# -------------- FUNCION MULTIPLICAR -------------- 
def multiplicar(a , b):
  return a * b

# -------------- FUNCION DIVIDIR -------------- 
def dividir(a , b):
  if b == 0:
    return None
  return a / b

opcion = 0

while opcion != 5:

  print("--------------- MENU --------------")
  print("1..... SUMAR")
  print("2..... RESTAR")
  print("3..... MULTIPLICAR")
  print("4..... DIVIDIR")
  print("5..... SALIR")
  opcion = int(input("Ingrese una opción... "))


  # VALIDACION PARA SALIR 
  if opcion == 5:
    break
  
  a = int(input("Ingrese un No. "))
  b = int(input("Ingrese un No. "))

  if opcion == 1:
    print("Resultado de la suma ", sumar(a , b))
  elif opcion == 2:
    print("Resultado de la resta " , restar(a , b))
  elif opcion == 3:    
    print("Resultado de la multipicación es " , multiplicar(a , b))
  elif opcion == 4:
    resultado = dividir(a , b)
    if resultado is None:
      print("imposible divisón entre 0")
    else:
      print("Resultado de la división " , resultado)
  else:
    print("Opción no valida")
