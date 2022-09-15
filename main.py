import random
import time
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'
RESET = '\033[39m'
iniciar_trivia = True 
intento = 0
puntos=[]
while iniciar_trivia == True:
 puntos=[]
 puntaje = random.randint(0,100)
 intento += 1
 print(RED+"\nIntento número:",intento,RESET)
 print(GREEN+"Bienvenido a mi trivia sobre cultura general\nPondré a prueba tus conocimientos\n"+RESET)
 time.sleep(2) 
 nombre = input(BLUE+"¿Cuál es tu nombre?: "+RESET)
 print(GREEN+"\nBienvenido",nombre,", responde las siguientes preguntas correctamente y ganarás puntos, falla y se te restarán,los puntos ganados o restados son aleatorios entre 0 y 100, escribe la letra de la alternativa y presiona 'Enter' para enviar tu respuesta:"+RESET)
 print(GREEN+"Iniciarás con"+RED,puntaje,RESET,GREEN+"puntos\n")
 input(BLUE+"Presiona Enter para continuar"+RESET)
 for conteo in range (5,0,-1):
  print(RED,conteo,RESET)
  time.sleep(1)
 print(MAGENTA+"\n1.¿Cuál es el único mamífero que puede volar?"+RESET)
 print(RED+"a)"+YELLOW+" El Pato"+RESET)
 print(RED+"b)"+YELLOW+" El murciélago"+RESET)
 print(RED+"c)"+YELLOW+" La mariposa"+RESET)
 print(RED+"d)"+YELLOW+" El caballo\n"+RESET)
 rpt = input(BLUE+"Ingresa tu respuesta:"+RESET)
 while rpt not in ("a","b","c","d","t","A","B","C","D","T"):
  rpt = input(RED+"No es una alternativa válida, escoge una de las alternativas mostradas\n"+BLUE+"Ingresa tu respuesta: "+RESET )
 if rpt=="a" or rpt=="A":
   puntaje-=random.randint(0,100)
   print(GREEN+"¡¿Como que un pato?!¡El pato es un ovíparo",nombre,"!"+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="c" or rpt=="C":
   puntaje-=random.randint(0,100)
   print(GREEN+"La mariposa es un Insecto, no es la respuesta correcta",nombre,RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="d" or rpt=="D":
   puntaje-=random.randint(0,100)
   print(GREEN,nombre,"el caballo es un mamífero, pero no vuela, ¿o sí?"+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="t" or rpt=="T":
   puntaje+= 1000000
   print(RED+"Bien hecho",nombre,"has encontrado la letra secreta, has logrado muchos puntos"+RESET)
   print(BLUE+"Alcanzaste los"+RED,puntaje,BLUE+"puntos\n"+RESET)
 else:
   puntos.append(random.randint(0,100))
   print(GREEN+"Has ganado"+RED,puntos[0],GREEN+"puntos")
   sumar=sum(puntos,puntaje)
   print(GREEN+"Respuesta correcta acertaste",nombre+RESET)
   print(GREEN+"Tienes"+RED,sumar,GREEN+"puntos\n"+RESET)
 time.sleep(2)
 print(MAGENTA+"2.¿Quien es el autor del Quijote?"+RESET)
 print(RED+"a)"+YELLOW+" Mario Vargas Llosa"+RESET)
 print(RED+"b)"+YELLOW+" Cesar Vallejo"+RESET)
 print(RED+"c)"+YELLOW+" Miguel de Cervantes Saavedra"+RESET)
 print(RED+"d)"+YELLOW+" Ricardo Palma\n")
 rpt = input(BLUE+"Ingresa tu respuesta:"+RESET)
 while rpt not in ("a","b","c","d","A","B","C","D"):
  rpt = input(RED+"No es una alternativa válida, escoge una de las alternativas mostradas\n"+BLUE+"Ingresa tu respuesta: "+RESET )
 if rpt=="a" or rpt=="A":
   puntaje-=random.randint(0,100)
   print(GREEN+"Mario Vargas Llosa no escribió el Quijote."+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="b" or rpt=="B":
   puntaje-=random.randint(0,100)
   print(GREEN+"Cesar Vallejo no es el autor."+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="d" or rpt=="D":
   puntaje-=random.randint(0,100)
   print(GREEN+"Ricardo Palma no es su autor."+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 else:
   puntos.append(random.randint(0,100))
   print(GREEN+"Has ganado"+RED,puntos[1],GREEN+"puntos")
   sumar=sum(puntos,puntaje)
   print(GREEN+"Don Quijote de la Mancha fue la obra maestra de Miguel de Cervantes Saavedra,",nombre,"Lo estás haciendo bien."+RESET)
   print(GREEN+"Tienes"+RED,sumar,GREEN+"puntos\n"+RESET)
 time.sleep(2)
 print(MAGENTA+"3.¿A cuantos años equivale un Lustro?"+RESET)
 print(RED+"a)"+YELLOW+" 10 años"+RESET)
 print(RED+"b)"+YELLOW+" 15 años"+RESET)
 print(RED+"c)"+YELLOW+" 100 años"+RESET)
 print(RED+"d)"+YELLOW+ " 5 años\n"+RESET)
 rpt = input(BLUE+"Ingresa tu respuesta:"+RESET)
 while rpt not in ("a","b","c","d","A","B","C","D"):
  rpt = input(RED+"No es una alternativa válida, escoge una de las alternativas mostradas\n"+BLUE+"Ingresa tu respuesta: "+RESET )
 if rpt=="a" or rpt=="A":
   puntaje-=random.randint(0,100)
   print(GREEN+"Incorrecto, una década son 10 años."+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="b" or rpt=="B":
   puntaje-=random.randint(0,100)
   print(GREEN+"Te equivocaste, un quindenio equivale a 15 años."+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 elif rpt=="c" or rpt=="C":
   puntaje-=random.randint(0,100)
   print(GREEN+"Estuviste cerca, pero no, un siglo o centuria equivale a 100 años"+RESET)
   print(GREEN+"Tienes"+RED,puntaje,GREEN+"puntos\n"+RESET)
 else:
   puntos.append(random.randint(0,100))
   sumar=sum(puntos,puntaje)
   print(GREEN+"Has ganado"+RED,puntos[2],GREEN+"puntos")
   sumar=sum(puntos,puntaje)
   print(GREEN+"Excelente",nombre,"lo has hecho bien, un lustro equivale a 5 años"+RESET)
   print(GREEN+"Tienes"+RED,sumar,GREEN+"puntos\n"+RESET)
 time.sleep(3)
 print(GREEN+"Tenemos la última pregunta de nuestra trivia , en la cual podrías ganar o perderlo todo:"+RESET)
 time.sleep(2)
 numero=int(input(BLUE+"Ingresa un numero:"+RESET))
 print(GREEN+"\nSi respondes correctamente tus"+RED,sumar,GREEN+"puntos se multiplicarán por"+WHITE,numero,RESET)
 print(GREEN+"Si tu respuesta se acerca a la correcta a tus"+RED,sumar,GREEN+"puntos se le sumarán "+WHITE,numero,RESET)
 print(GREEN+"Si tu respuesta está muy alejada de la respuesta correcta a tus"+RED,sumar,GREEN+"puntos se le restarán"+WHITE,numero,RESET)
 print(GREEN+"Si tu respuesta es la que no tiene relación con la pregunta tus"+RED,sumar,GREEN+"puntos se dividirán entre"+WHITE,numero,RESET)
 time.sleep(10)
 print(MAGENTA+"\n4.¿Cuanto es 152 elevado a 0?"+RESET)
 print(RED+"a)"+YELLOW+" 152"+RESET)
 print(RED+"b)"+YELLOW+" 1"+RESET)
 print(RED+"c)"+YELLOW+" 0"+RESET)
 print(RED+"d)"+YELLOW+" Cristiano Ronaldo\n"+RESET)
 rpt = input(BLUE+"Ingresa tu respuesta:"+RESET)
 while rpt not in ("a","b","c","d","A","B","C","D"):
  rpt = input(RED+"No es una alternativa válida, escoge una de las alternativas mostradas\n"+BLUE+"Ingresa tu respuesta: "+RESET )
 if rpt=="a" or rpt=="A":
   print(GREEN+"Incorrecto, 152 no es la respuesta."+RESET)
   print(GREEN+"A tus"+RED,puntaje,GREEN+"puntos se le restarán"+WHITE,numero,RESET)
   print(GREEN+"Trivia finalizada, Gracias por jugar",nombre,"Alcanzaste los"+RED,puntaje-numero,GREEN+"puntos"+RESET)

 elif rpt=="c" or rpt=="C":
   print(GREEN+"Casi, pero no."+RESET)
   print(GREEN+"A tus"+RED,puntaje,GREEN+"puntos se le sumarán "+WHITE,numero)
   print(GREEN+"Trivia finalizada, Gracias por jugar",nombre,"Alcanzaste los"+RED,puntaje+numero,GREEN+"puntos"+RESET)
 elif rpt=="d" or rpt=="D":
   print(GREEN+"SIIIIUUUUUU, fallaste xd"+RESET)
   print(GREEN+"Tus"+RED,puntaje,GREEN+"puntos serán divididos entre"+WHITE,numero,RESET)
   print(GREEN+"Trivia finalizada, Gracias por jugar",nombre,"Alcanzaste los"+RED,puntaje/numero,GREEN+"puntos"+RESET)
 else:
   puntos.append(random.randint(0,100))
   print(GREEN+"Has ganado"+RED,puntos[3],GREEN+"puntos")
   sumar=sum(puntos,puntaje)
   print(GREEN+"Excelente",nombre,"todo número elevado a la 0 es 1"+RESET)
   print(GREEN+"Puntuacion de"+RESET,RED,sumar,RESET)
   print(GREEN+"Puntuación Total:"+RED,sumar*numero,GREEN+"puntos")

 print(GREEN+"\n¿Deseas jugar nuevamente la trivia?"+RESET)
 repetir_trivia = input(BLUE+"Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()
 if repetir_trivia != "si": 
   print(BLUE+"\n!Gracias por jugar mi trivia",nombre,", hasta pronto!"+RESET)
   iniciar_trivia = False
   