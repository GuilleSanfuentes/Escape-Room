import requests
import threading
import time
import sys
import os
import _thread
import random
import time

from Clase_Jugador import Jugador
from Clase_Juegos import Juego
from Clase_Sopa_Letras import Sopa_letras
from Clase_Juego_Quiz_Unimet import Quiz_Cultura_Unimetana
from Clase_Preguntas_Sobre_Python import Preguntas_sobre_python
from Clase_Partida import Partida, Partida_Ganada, Partida_Perdida_Por_Tiempo, Partida_Perdida_Por_Vidas

def cls():
	  os.system('cls' if os.name=='nt' else 'clear')

def stopper(sec, jugador):
	time.sleep(sec)
	print('\n\n-------- Se acabó el tiempo!!! -------- \nPresione "enter" para terminar programa.\n')
	Partida_Perdida_Por_Tiempo.partida_perdida_por_tiempo(jugador)
	_thread.interrupt_main()

def descarga_api():
	API = requests.get('https://api-escapamet.vercel.app/')
	api = API.json()
	return api

def leer_DB():
	r = open("Jugadores_DB.txt", "r")
	comprobar = r.read()
	r.close()
	jugadores = eval(comprobar)
	return jugadores

def db_tiempos():
	d = open("Tiempos_y_vidas.txt", "r")
	tiempos = d.read()
	d.close()
	tiempos = eval(tiempos)
	return tiempos

def quita_vidas(jugador, menos_vida):	
	jugador["vidas"] = jugador['vidas'] - float(menos_vida)
	return jugador

def asigna_juego(nombre_juego):
  cuartos = descarga_api()
  while True:
    for cuarto in cuartos:
      objetos = cuarto['objects']
      for objeto in objetos:
        game = objeto["game"]
        if game["name"] == nombre_juego:
          return game

def mostrar_historial_personal(jugador):
	g = open("Historial_partidas.txt", "r")
	buscar_partidas = g.read()
	g.close()
	buscar_partidas = eval(buscar_partidas)
	for partida in buscar_partidas:
		if partida['username'] == jugador["username"]:
			if partida['gano'] == True:
				print(f"---> {partida['fecha']} | Ganó con {partida['vidas']} vidas, en {partida['dificultad']}")
			else: print(f"---> {partida['fecha']} | Perdió por {partida['razon']} en modo {partida['dificultad']}")

def biblioteca(jugador):
	while True:
		accion = input('''
		BIBLIOTECA\n
	1. Mueble de libros | Centro
	2. Mueble de sentarse | Izquierda
	3. Mueble con gabetas | Derecha
	4. Puerta Pasillo Laboratorios
	5. Puerta Plaza Rectorado
	6. Ver mi Inventario\n
	''')
		while (not accion.isnumeric()) or (not int(accion) in range(1,7)):
			accion = input('Favor ingrese una opcion válida: \n')
		if accion == '1':
			award = "Cable HDMI"
			nombre_juego = "ahorcado"
			if jugador[nombre_juego] == False:
				#juego
				jugador[nombre_juego] = True
				jugador['inventario'].append(award)
				print(f"Completaste el juego {nombre_juego.title()}. recibes {award}")
			else: print("No se pueden repetir minijuegos")
		elif accion == '2':
			requirement = "Libro De Matemáticas"
			nombre_juego = "Preguntas matemáticas"
			if requirement in jugador['inventario']:
				if jugador[nombre_juego] == False:
					jugador['vidas'] = jugador['vidas'] + 1
					#juego
					jugador[nombre_juego] = True
					print(f"Completaste el juego {nombre_juego.title()}. recibes 1 vida más. ahora tienes {jugador['vidas']}")
				else: print("No se pueden repetir minijuegos")
			else: print(f"No tienes la herramienta necesaria para realizar esta actividad. Vuelve cuando obtengas {requirement}")
		elif accion == '3':
			requirement = "Llave"
			award = "Mensaje"
			nombre_juego = "Criptograma"
			if requirement in jugador['inventario']:
				if jugador[nombre_juego] == False:	
					#juego
					jugador[nombre_juego] = True
					jugador['inventario'].append(award)
					print(f"Completaste el juego {nombre_juego.title()}. recibes {award}")
				else: print("No se pueden repetir minijuegos")
			else: print(f"No tienes la herramienta necesaria para realizar esta actividad. Vuelve cuando obtengas {requirement}")
		elif accion == '4':
			jugador = pasillo_laboratorio(jugador)
			break
		elif accion == '5':
			jugador = plaza_rectorado(jugador)
			break
		elif accion == '6':
			print("Inventario:\n")
			for item in jugador['inventario']:
				print(item)
	return jugador

def pasillo_laboratorio(jugador):
	while True:
		accion = input('''\n
		PASILLO LABORATORIOS\n
	1. Puerta Biblioteca
	2. Puerta Laboratorios_SL001
	3. Ver mi Inventario\n
	''')
		while (not accion.isnumeric()) or (not int(accion) in range(1,4)):
			accion = input('Favor ingrese una opcion válida: \n')
		if accion == '1':
			jugador = biblioteca(jugador)
			break
		elif accion == '2':
			if jugador['puerta_rota'] == True:
				jugador = laboratorios_SL001(jugador)
				break
			elif "Martillo" in jugador['inventario']:
				print("Usaste el martillo para romper la cerradura\nDesbloqueaste el Laboratorio SL001")
				jugador["puerta_rota"] = True
				jugador["inventario"].remove('Martillo')
			else: print("No puedes pasar por aca, ya que requieres de una herramienta que aun no has obtenido. regresa y búscala")
		elif accion == '3':
			print("Inventario: \n")
			for item in jugador['inventario']:
				print(item)
	return jugador

def laboratorios_SL001(jugador):
	while True:
		accion = input('''
		LABORATORIOS SL001\n
	1. Pizarra | Centro
	2. Computadora 1 | Izquierda
	3. Computadora 2 | Derecha
	4. Puerta Pasillo Laboratorios
	5. Puerta Cuarto Servidores
	6. Ver mi Inventario\n
	''')
		while (not accion.isnumeric()) or (not int(accion) in range(1,7)):
			accion = input('Favor ingrese una opcion válida: \n')
		if accion == '1':
			nombre_juego = "sopa_letras"
			if jugador[nombre_juego] == False:
				game_data = asigna_juego(nombre_juego)
				jugador = Sopa_letras.juego_sopa_letras(jugador, game_data)
				if jugador == False:
					Partida_Perdida_Por_Vidas.partida_perdida_por_vidas(jugador)
					_thread.interrupt_main()
				cls()
				print("Felicidades, completaste la sopa de letras, y ganaste 1 vida más\n")
			else: print("No se pueden repetir minijuegos")
		elif accion == '2':
			requirement = "Cable HDMI"
			award = "Carnet"
			if requirement in jugador['inventario']:
				nombre_juego = "Preguntas sobre python"
				if jugador[nombre_juego] == False:
					game_data = asigna_juego(nombre_juego)
					jugador = Preguntas_sobre_python.juego_preguntas_sobre_python(jugador, game_data)
					if jugador == False:
						Partida_Perdida_Por_Vidas.partida_perdida_por_vidas(jugador)
						_thread.interrupt_main()
					jugador[nombre_juego] = True
					cls()
					print(f"Felicidades, respondiste correctamente la pregunta! Se te entrega {game_data['award'].upper()}\n")
				else: print("No se pueden repetir minijuegos")
			else: print(f"No tienes la herramienta necesaria para realizar esta actividad. Vuelve cuando obtengas {requirement}")
		elif accion == '3':
			award = "Llave"
			requirement = "Contraseña"
			nombre_juego = "Adivinanzas"
			if requirement in jugador['inventario']:
				if jugador[nombre_juego] == False:	
					#juego
					jugador[nombre_juego] = True
					jugador['inventario'].append(award)
					print(f"Completaste el juego {nombre_juego.title()}. recibes {award}")
		elif accion == '4':
			jugador = pasillo_laboratorio(jugador)
			break
		elif accion == '5':
			jugador = cuarto_servidores(jugador)
			break
		elif accion == '6':
			print("Inventario:")
			for item in jugador['inventario']:
				print(item)
	return jugador

def plaza_rectorado(jugador):
	while True:
		accion = input('''
		PLAZA RECTORADO\n
	1. Saman | Centro
	2. Banco 1 | Izquierda
	3. Banco 2 | Derecha
	4. Puerta Biblioteca
	5. Ver mi Inventario\n
	''')
		while (not accion.isnumeric()) or (not int(accion) in range(1,7)):
			accion = input('Favor ingrese una opcion válida: \n')
		if accion == '1':
			requirement = ["Titulo Universitario", "Mensaje"]
			award = "Disco Duro"
			result = all(elem in jugador['inventario'] for elem in requirement)
			nombre_juego = "Encuentra la lógica y resuelve"
			if result == True:
				if jugador[nombre_juego] == False:
					#juego
					jugador[nombre_juego] = True
					jugador['inventario'].append(award)
					print(f"Completaste el juego {nombre_juego.title()}. recibes {award}")
				else: print("No se pueden repetir minijuegos")
			else: print(f"No tienes la herramienta necesaria para realizar esta actividad. Vuelve cuando obtengas {requirement}")
		elif accion == '2':
			award = "Libro De Matemáticas"
			nombre_juego = "Quizizz Cultura Unimetana"
			if jugador[nombre_juego] == False:
				game_data = asigna_juego(nombre_juego)
				jugador = Quiz_Cultura_Unimetana.quiz_cultura_unimet(jugador, game_data)
				if jugador == False:
					Partida_Perdida_Por_Vidas.partida_perdida_por_vidas(jugador)
					_thread.interrupt_main()
				jugador[nombre_juego] = True
				cls()
				print(f"Felicidades, respondiste correctamente la pregunta! Se te entrega {game_data['award'].upper()}\n")
				jugador["Quizizz Cultura Unimetana"] = True
				jugador['inventario'].append(award)
			else: print("No se pueden repetir minijuegos")
		elif accion == '3':
			award = "Martillo"
			if jugador["memoria con emojis"] == False:	
				#juego
				jugador["memoria con emojis"] = True
				jugador['inventario'].append(award)
			else: print("No se pueden repetir minijuegos")
		elif accion == '4':
			jugador = biblioteca(jugador)
			break
		elif accion == '5':
			print("Inventario:\n")
			for item in jugador['inventario']:
				print(item)
	return jugador

def cuarto_servidores(jugador):
	while True:
		accion = input('''
		CUARTO SERVIDORES\n
	1. Puerta | Centro
	2. Rack | Izquierda
	3. Papelera | Derecha
	4. Puerta Laboratorios SL001
	5. Ver mi Inventario\n
	''')
		while (not accion.isnumeric()) or (not int(accion) in range(1,7)):
			accion = input('Favor ingrese una opcion válida: \n')
		if accion == '1':
			requirement = ["Carnet", "Disco Duro"]
			result = all(elem in jugador['inventario'] for elem in requirement)
			if result == True:
				if jugador["Juego Libre"] == False:
					Partida_Ganada.gano_la_partida(jugador)
					print('\n\nFELICIDADES, GANASTE!')
					time.sleep(3)
					_thread.interrupt_main()
				else: print("No se pueden repetir minijuegos")
			else: print(f"No tienes la herramienta necesaria para realizar esta actividad. Vuelve cuando obtengas {requirement}")
		elif accion == '2':
			award = "Contraseña"
			if jugador["Palabra mezclada"] == False:
				#juego
				jugador["Palabra mezclada"] = True
				jugador['inventario'].append(award)
			else: print("No se pueden repetir minijuegos")
		elif accion == '3':
			award = "Titulo Universitario"
			if jugador["escoge un número entre"] == False:	
				#juego
				jugador["escoge un número entre"] = True
				jugador['inventario'].append(award)
			else: print("No se pueden repetir minijuegos")
		elif accion == '4':
			jugador = laboratorios_SL001(jugador)
			break
		elif accion == '5':
			print("Inventario:")
			for item in jugador['inventario']:
				print(item)
	return jugador

def nuevo_juego(jugador):
	dificultad = input('''\nSeleccione el nivel de dificultad:
	1. Fácil
	2. Medio
	3. Difícil
	\n''')
	while (not dificultad.isnumeric()) or (not int(dificultad) in range(1,4)):
		dificultad = input('\nFavor ingrese una opcion válida: \n \n')
	lista_tiempos = db_tiempos()
	if dificultad == '1':
		dificultad = "Fácil"
		sec = float(lista_tiempos[0])
		vidas = float(lista_tiempos[3])
	if dificultad == '2':
		dificultad = "Media"
		sec = float(lista_tiempos[1])
		vidas = float(lista_tiempos[4])
	if dificultad == '3':
		dificultad = "Difícil"
		sec = float(lista_tiempos[2])
		vidas = float(lista_tiempos[5])
	print(f'Dificultad: {dificultad}\nVidas: {vidas}')
	jugador["vidas"] = float(vidas)
	jugador['dificultad'] = dificultad
	jugador["inventario"] = []
	jugador['puerta_rota'] = False
	jugador["ahorcado"] = False
	jugador["Preguntas matemáticas"] = False
	jugador["Criptograma"] = False
	jugador["sopa_letras"] = False
	jugador["Encuentra la lógica y resuelve"] = False
	jugador["memoria con emojis"] = False
	jugador["Preguntas sobre python"] = False
	jugador["Adivinanzas"] = False
	jugador["Quizizz Cultura Unimetana"] = False
	jugador["Juego Libre"] = False
	jugador["Palabra mezclada"] = False
	jugador["escoge un número entre"] = False
	time.sleep(1)
	print(f"Avatar: {jugador['avatar']}")
	print("Que comience el juego...")
	time.sleep(2)
	cls()
	print(f"\nHoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a recuperar el disco, para eso tienes {sec/60} minutos, antes de que el servidor se caiga y no se pueda hacer más nada. ¿Aceptas el reto?\n\n")
	number = random.randint(1111,9999)
	print(f"\nIngrese el codigo '{number}' para aceptar el reto:\n")
	inicio_juego = input('\n')
	while inicio_juego != str(number):
		inicio_juego = input("Intente Nuevamente\n")
	
	threading.Thread(target = stopper, args = (sec, jugador)).start()
	cls()
	print(f"Bienvenido {jugador['avatar']}, gracias por tu disposición a ayudarnos a resolver este inconveniente. Te encuentras actualmente ubicado en la biblioteca. Presiona enter para ver a tu alrededor. \n\n¡Recuerda que el tiempo corre más rápido que un trimestre en este reto!.")
	biblioteca(jugador)

def main():
	print('\nBienvenid@ a Escapemet.\nPor favor marque 1 si desea iniciar sesion, o 2 si desea registrarse como nuevo usuario')

	opcion = input('')
	while (not opcion.isnumeric()) or (not int(opcion) in range(1,3)):
		opcion = input('Favor ingrese una opcion válida: \n \n')
	if opcion == '1':
		db_jugadores = leer_DB()
		usuario = input("\nBienvenid@ de vuelta, jugador. Por favor indique su nombre de usuario.\n")
		innecesario = False
		while innecesario == False:
			for user in db_jugadores:
				if user['username'] == usuario:
					innecesario = True
					break
			while innecesario == False:
				usuario = input("\nEl usuario ingresado no se encuentra en el sistema. Intente nuevamente: \n")
				if user['username'] == usuario:
					innecesario = True
					break
			break
		contraseña = input('Por favor ingrese su contraseña: ')
		while contraseña != user['password']:
			contraseña = input('La contraseña no coincide con el usuario. Intente nuevamente: \n')
		jugador = user

	elif opcion == '2':
		jugador = Jugador.new_player()
		print(f"\nEl usuario {jugador['username']} de {jugador['age']} años de edad, eligió al avatar {jugador['avatar']}.\n\n---- Su usuario ha sido creado exitosamente. ----")
	'''Puro BS para que se vea mas interesante'''
	print("\nIniciando programa...")
	time.sleep(2)
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	cls()

	while True:
		primera_opcion = input("\nPor favor indique si desea:\n1. Iniciar una nueva Partida\n2. Ver las instrucciones del juego\n3. Ver los rankings en el juego\n--> ")
		while (not primera_opcion.isnumeric()) or (not int(primera_opcion) in range(1,4)):
			primera_opcion = input('Favor ingrese una opcion válida: \n \n')
		if primera_opcion == "1":
			nuevo_juego(jugador)
			break
		elif primera_opcion == "2":
			print('''
				Instrucciones:

	1) Todo juego tendrá un límite de tiempo y un límite de vidas, que va en correlación a la dificultad que el jugador elija.
	2) Perderás vidas cuando te equivoques. Dependiendo del reto, perderás una cierta cantidad, u otra.
	3) El avatar que elegiste será tu personaje en el juego para siempre. Si deseas uno nuevo, necesitarás crearte una nueva cuenta.
	4) No olvides la contraseña que creaste! No se te podrá ser reestaurada, asi que si la pierdes, tendrás que crearte una nueva cuenta para jugar.
	5) Juega todos los juegos, y diviertete limpiamente! 
	6) En caso de juegos con ejercicios y funciones matemáticas, tienes permitido el uso de calculadoras, pero no busques respuestas en internet a preguntas sencillas! 
	7) No se pueden repetir minijuegos
	8) No puedes salir de un minijuego hasta haberlo completado
	9) Diviertete! Y buena suerte

			''')
		elif primera_opcion == "3":
			print('\n')
			mostrar_historial_personal(jugador)

main() 