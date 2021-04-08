import os
import random 
import threading

from Clase_Juegos import Juego
from Clase_Partida import Partida

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

class Sopa_letras(Juego):
	def juego_sopa_letras(jugador, game_data):
		cls()
		Sopa_letras.name = game_data['name'].title()
		Sopa_letras.award = game_data['award'].title()
		Sopa_letras.rules = game_data['rules']
		Sopa_letras.questions = game_data['questions']

		'''Esta funcion utiliza lo que se obtiene de la API para generar un juego usando los metodos heredados de la superclase Juegos, y las utiliza para implimir los juegos, aunque se les haga una modificacion en la API. Es decir, no importa si agregan o eliminan preguntas y sus respuestas a cada forma del juego de la API, este codigo siempre funcionara'''
		
		print(f"Bienvenid@ {jugador['avatar']} al juego {Sopa_letras.name}\n\nEn este juego se {Sopa_letras.rules}\n\nSe te haran 3 preguntas, de las cuales debes responder las 3 correctamente para obtener la recompensa\n")
		print(f'Tienes {jugador["vidas"]} vidas')

		vida_menos = 0.5
		numero_cuantas = len(Sopa_letras.questions)-1
		n = random.randint(0,numero_cuantas)
		preguntas = Sopa_letras.questions[n]
		max_preguntas = len(preguntas)
		division = int(max_preguntas/2)
		ultima_pregunta = division
		p = division
		z = []
		for key,valor in preguntas.items():
		  z.append(valor.upper())
		
		pregunta = 0	
		while jugador["vidas"] > 0:
			fachero = pregunta+1
			if pregunta <= (ultima_pregunta - 1):
				print(f"\nTienes {jugador['vidas']} vidas\n\n PREGUNTA {fachero}\n")
				respuesta = input(f"{z[p]}\n===> ").upper()
				while respuesta != z[pregunta]:
					print(f"\nRespuesta incorrecta. Pierdes {vida_menos} vidas\n")
					jugador["vidas"] = (jugador["vidas"] - float(vida_menos))
					print(f"\nTienes {jugador['vidas']} vidas\n")
					if jugador['vidas'] <= 0:
						print("Te quedaste sin vidas. Perdiste el Juego")
						return False
					respuesta = input(f"\n{z[p]}\n===> ").upper()
				pregunta = pregunta + 1
				p = p + 1
			else:
				jugador["sopa_letras"] = True
				jugador['vidas'] = jugador['vidas'] + 1
				print(f'Vidas: {jugador["vidas"]}')
				return jugador
		
