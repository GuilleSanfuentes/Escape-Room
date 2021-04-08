import os
import random 
import threading

from Clase_Juegos import Juego

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

class Quiz_Cultura_Unimetana(Juego):
	def quiz_cultura_unimet(jugador, game_data):
		cls()
		Quiz_Cultura_Unimetana.name = game_data['name'].title()
		Quiz_Cultura_Unimetana.award = game_data['award'].title()
		Quiz_Cultura_Unimetana.rules = game_data['rules']
		Quiz_Cultura_Unimetana.questions = game_data['questions']

		'''Esta funcion utiliza lo que se obtiene de la API para generar un juego usando los metodos heredados de la superclase Juegos, y las utiliza para implimir los juegos, aunque se les haga una modificacion en la API. Es decir, no importa si agregan o eliminan preguntas y sus respuestas a cada forma del juego de la API, este codigo siempre funcionara'''
		
		print(f"Bienvenid@ {jugador['avatar']} al juego {Quiz_Cultura_Unimetana.name}\n\nEn este juego se {Quiz_Cultura_Unimetana.rules}\n\nSe te hara 1 preguntade seleccion simple, la que debes responder correctamente para obtener la recompensa. Pierdes media vida cada vez que te equivocas\n")
		print(f'Tienes {jugador["vidas"]} vidas')

		vida_menos = 0.5
		numero_cuantas = len(Quiz_Cultura_Unimetana.questions)-1
		n = random.randint(0,numero_cuantas)
		preguntas = Quiz_Cultura_Unimetana.questions[n]
		correct_answer = preguntas["correct_answer"]
		respuestas = []
		respuestas.append(preguntas["correct_answer"])
		respuestas.append(preguntas["answer_2"])
		respuestas.append(preguntas["answer_3"])
		respuestas.append(preguntas["answer_4"])
		random.shuffle(respuestas)
		print(f"\nPregunta:\n{preguntas['question']}\n")
		respuesta = input(f"1. {respuestas[0]}\n2. {respuestas[1]}\n3. {respuestas[2]}\n4. {respuestas[3]}\n ---->")
		while (not respuesta.isnumeric()) or (not int(respuesta) in range(1,5)):
			print(f"\nRespuesta incorrecta. Pierdes {vida_menos} vidas\n")
			jugador["vidas"] = (jugador["vidas"] - float(vida_menos))
			print(f"\nTienes {jugador['vidas']} vidas\n")
			if jugador['vidas'] <= 0:
				print("Te quedaste sin vidas. Perdiste el Juego")
				return False
			respuesta = input("Intente nuevamente: \n ---->")
		respuesta = (int(respuesta) - 1)
		answer = respuestas[respuesta]
		while answer != correct_answer:
			print(f"\nRespuesta incorrecta. Pierdes {vida_menos} vidas\n")
			jugador["vidas"] = (jugador["vidas"] - float(vida_menos))
			print(f"\nTienes {jugador['vidas']} vidas\n\n")
			if jugador['vidas'] <= 0:
				print("Te quedaste sin vidas. Perdiste el Juego")
				return False
			respuesta = input("Intente nuevamente: \n ---->")
			respuesta = (int(respuesta) - 1)
			answer = respuestas[respuesta]
		return jugador
		
