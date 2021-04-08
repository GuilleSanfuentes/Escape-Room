import os
import random 
import threading

from Clase_Juegos import Juego

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

class Preguntas_sobre_python(Juego):
	def juego_preguntas_sobre_python(jugador, game_data):
		cls()
		Preguntas_sobre_python.name = game_data['name'].title()
		Preguntas_sobre_python.award = game_data['award'].title()
		Preguntas_sobre_python.rules = game_data['rules']
		Preguntas_sobre_python.questions = game_data['questions']

		'''Esta funcion utiliza lo que se obtiene de la API para generar un juego usando los metodos heredados de la superclase Juegos, y las utiliza para implimir los juegos, aunque se les haga una modificacion en la API. Es decir, no importa si agregan o eliminan preguntas y sus respuestas a cada forma del juego de la API, este codigo siempre funcionara'''
		
		print(f"Bienvenid@ {jugador['avatar']} al juego {Preguntas_sobre_python.name}\n\nEn este juego se {Preguntas_sobre_python.rules}\n\nSe te hara 1 pregunta, a la cual debes responder correctamente para obtener la recompensa\n")

		vida_menos = 0.5
		numero_cuantas = len(Preguntas_sobre_python.questions)-1
		n = random.randint(0,numero_cuantas)
		pregunta = Preguntas_sobre_python.questions[n]
		
		while jugador["vidas"] > 0:
			print(f"\nTienes {jugador['vidas']} vidas\n\n")
			respuesta = input(f"{pregunta['question']}\n===> ")
			while respuesta != pregunta["answer"]:
				print(f"\nRespuesta incorrecta. Pierdes {vida_menos} vidas\n")
				jugador["vidas"] = (jugador["vidas"] - float(vida_menos))
				if jugador['vidas'] <= 0:
					print("Te quedaste sin vidas. Perdiste el Juego")
					return False
				print(f"\nTienes {jugador['vidas']} vidas\n")
				respuesta = input(f"{pregunta['question']}\n===> ").upper() 
			jugador["Preguntas_sobre_python"] = True
			jugador['inventario'].append(Preguntas_sobre_python.award)
			return jugador
		