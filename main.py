#Modulos
import ascii_art
import os

#Funciones
def LimpiarConsola():
  os.system('cls' if os.name == 'nt' else 'clear')

def Despedida():
  print(ascii_art.GraciasPorJugar)
  print("\n Gracias por utilizar mi primer programa hecho en python ;D\n")
  exit()

def perdiste():
  print(ascii_art.GameOver)

def validate(Result):
  if(Result=="Y"):
    LimpiarConsola()
    IniciarJuego()
  if(Result=="N"):
    Despedida()

def IniciarJuego():
  print(ascii_art.island)

  print("Bienvenido a...\n")
  print("*~*~* ISLA DEL TESORO *~*~*\n")
  print("Tu mision es encontrar el tesoro!\n")

  PrimeraRuta = input("Estás en una encrucijada, ¿te gustaría ir a la 'izquierda' o 'derecha'?\n").lower()

  if  PrimeraRuta == "izquierda":
    print(ascii_art.escalofriante)
    print("\n Continúas por el camino sinuoso y bordeado de árboles. Escalofriante.\n")

    SegundaRuta = input("\nHa llegado a un río de aguas agitadas, ¿le gustaría 'nadar' o 'buscar' otra opción?\n")

    if(SegundaRuta=="buscar"):
      print(ascii_art.PasarPuente)
      print("\n¡Que suerte! Ves un árbol caído a unos cien metros río arriba, se une a las dos orillas del río como un puente. Cruzas el río con éxito\n")

      TerceraRuta = input("\nEntras en una cueva con tres puertas, ¿te gustaría abrir la puerta 'azul', 'roja' o 'amarilla'?\n");

      if(TerceraRuta == "azul"):
        perdiste()
        print("\nEncuentras a un gigante taciturno en el suelo llorando. Te quedas atascado escuchando sus problemas y tu incomodidad social te impide encontrar una salida en la conversación. Te mueres de hambre. Juego terminado.\n")

        GameOver = input("Te gustaría volver a jugar? 'Y', 'N'?\n")
        validate(GameOver)
      
      if(TerceraRuta == "roja"):
        perdiste()
        print("\nAbres la puerta e inmediatamente te envuelven las llamas. Esa fue la puerta de incendios, Juego terminado.\n")

        GameOver = input("Te gustaría volver a jugar? 'Y', 'N'?\n")
        validate(GameOver)

      if(TerceraRuta == "amarilla"):
        print(ascii_art.treasure_chest)
        print("\n¡El amarillo es el color del oro! Duuuh, al pareser el cofre nesesita una clave :c, pero podemos saber cual es viendo todos los mapas dados :D\n")

      for open in range(3):
        password = input("COMBINACION: ")
        if password == "LGBKAZMJP":
          print(ascii_art.treasure_chest_open)
          print("\nHAS CONSEGUIDO EL TESORO!! ERES UN PIRATA LEGENDARIOO\n")
          print("gracias por jugar creado por:  Daniel Builes Nick: CmdData")
          exit()
        else:
          print("Combinacion incorrecta te quedan ",2-open,"Intentos ")

    else:
      perdiste()
      print("\nBueno eso fue tonto, te dejas llevar por la corriente y te quedas inconsciente en una roca. Te ahogas y tu cuerpo es arrastrado al mar. Meses después, su cadáver flotante hinchado se convierte en un regalo para las gaviotas. Juego terminado.\n")

      GameOver = input("Te gustaría volver a jugar? 'Y', 'N'?")
      validate(GameOver)
  else:
    perdiste()
    print("\nOh Noooo--- caes en un pozo sin fondo. No te preocupse, tendrás mucho tiempo para pensar por qué no miras por donde caminas. Game Over.\n")

    GameOver = input("Te gustaría volver a jugar? 'Y', 'N'?\n")
    validate(GameOver)

#Ejecutar el metodo principal
IniciarJuego()