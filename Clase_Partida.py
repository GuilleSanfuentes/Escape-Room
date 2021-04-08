import datetime

'''No logre que me dejara guardar las partidas cuando las pierdes, pero se guardan todas las que ganas'''

class Partida():
  def __init__(self, jugador, fecha_y_hora, dificultad):
    self.jugador = jugador
    self.fecha_y_hora = fecha_y_hora
    self.dificultad = dificultad

class Partida_Ganada(Partida):
	def __init__(self, tiempo, vidas):
		self.tiempo = tiempo
		self.vidas = vidas
	
	def gano_la_partida(jugador):
		partida_jugador = {}
		partida_jugador["username"] = jugador["username"]
		partida_jugador["gano"] = True
		partida_jugador["dificultad"] = jugador["dificultad"]
		partida_jugador["vidas"] = jugador["vidas"]
		u = datetime.datetime.now()
		partida_jugador["fecha"] = u.strftime("%c")
		f = open("Historial_partidas.txt", "r")
		comprobar_partidas = f.read()
		f.close()
		comprobar_partidas = eval(comprobar_partidas)
		comprobar_partidas.append(partida_jugador)
		w = open("Historial_partidas.txt", "w")
		update = str(comprobar_partidas)
		w.write(update)
		w.close()

class Partida_Perdida_Por_Tiempo(Partida):
	def partida_perdida_por_tiempo(jugador):
		print('\nSe te acabó el tiempo. Perdiste la partida\n')
		partida_jugador = {}
		partida_jugador["username"] = jugador["username"]
		partida_jugador["razon"] = "Se te acabo el tiempo"
		partida_jugador["gano"] = False
		partida_jugador["dificultad"] = jugador["dificultad"]
		u = datetime.datetime.now()
		partida_jugador["fecha"] = u.strftime("%c")
		f = open("Historial_partidas.txt", "r")
		comprobar_partidas = f.read()
		f.close()
		comprobar_partidas = eval(comprobar_partidas)
		comprobar_partidas.append(partida_jugador)
		w = open("Historial_partidas.txt", "w")
		update = str(comprobar_partidas)
		w.write(update)
		w.close()

class Partida_Perdida_Por_Vidas(Partida):
	def partida_perdida_por_vidas(jugador):
		print('\nSe te acabaron las vidas. Perdiste la partida\n')
		perdedor_jugador = dict()
		perdedor_jugador["dificultad"] = jugador["dificultad"]
		perdedor_jugador["username"] = jugador["username"]
		perdedor_jugador["razon"] = "Se te acabaron las vidas"
		perdedor_jugador["gano"] = False
		u = datetime.datetime.now()
		perdedor_jugador["fecha"] = u.strftime("%c")
		f = open("Historial_partidas.txt", "r")
		comprobar_partidas = f.read()
		f.close()
		comprobar_partidas = eval(comprobar_partidas)
		comprobar_partidas.append(perdedor_jugador)
		w = open("Historial_partidas.txt", "w")
		update = str(comprobar_partidas)
		w.write(update)
		w.close()
    