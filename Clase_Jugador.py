class Jugador():
	def __init__(self, username, password, age, avatar):
		self.username = username
		self.password = password
		self.age = age
		self.avatar = avatar
	
	def new_player():
		print("\nBienvenid@ al modulo de creación de cuenta. \nPor favor indique lo solicitado, y anote su documentación en una hoja para que no la olvide.")
		username = input('\nPor favor indique su Nombre de Usuario: ')
		while True:
			password = input('\nPor favor cree una contraseña para su cuenta: ')
			probando_contraseña = input('Repita la contraseña anteriormente indicada: ')
			if password == probando_contraseña:
				break
			else: print("Las contraseñas no coinciden, intente nuevamente.")
		age = input('\nPor favor indique su edad: ')
		while not age.isnumeric():
			age = input('Favor ingrese su edad correctamente: \n')
		avatar_numero = input('\nEn este juego, puedes elejir un avatar para con el cual jugar. Por favor indique el número de quién quiere ser: \n1. Scharifker\n2. Eugenio Mendoza\n3. Pelusa\n4. Gandhi\n5. Pilar\n6. Kaki Llorente\n7. Victoria Quintero\n8. Alejandro Fariña\n9. Guillermo Sanfuentes\n10. Crear Nuevo Personaje\n\n')
		while (not avatar_numero.isnumeric()) or (not int(avatar_numero) in range(1,11)):
			avatar_numero = input('Favor ingrese una opcion válida (Entre 1 y 10): \n')
		'''Lo hago asi para que sea mas facil ver el programa una vez este contraido el while loop'''
		while True:
			if avatar_numero == '1':
				avatar = "Scharifker"
				break
			elif avatar_numero == '2':
				avatar = "Eugenio Mendoza"
				break
			elif avatar_numero == '3':
				avatar = "Pelusa"
				break
			elif avatar_numero == '4':
				avatar = "Gandhi"
				break
			elif avatar_numero == '5':
				avatar = "Pilar"
				break
			elif avatar_numero == '6':
				avatar = "Kaki Llorente"
				break
			elif avatar_numero == '7':
				avatar = "Victoria Quintero"
				break
			elif avatar_numero == '8':
				avatar = "Alejandro Fariña"
				break
			elif avatar_numero == '9':
				avatar = "Guillermo Sanfuentes"
				break
			elif avatar_numero == '10':
				avatar = input("\nPor favor escriba el nombre de su avatar (Considere las mayúsculas y minúsculas): ")
				break
		
		jugador_nuevo = {}
		jugador_nuevo["username"] = username
		jugador_nuevo["password"] = password
		jugador_nuevo["age"] = age
		jugador_nuevo["avatar"] = avatar

		f = open("Jugadores_DB.txt", "r")
		comprobar_jugadores = f.read()
		f.close()
		jugadores = eval(comprobar_jugadores)
		print(type(jugadores))
		jugadores.append(jugador_nuevo)

		w = open("Jugadores_DB.txt", "w")
		update = str(jugadores)
		w.write(update)
		w.close()



		return jugador_nuevo