from datetime import datetime, timedelta
import time

# Bienvenida
print "Bienvenido!"
print "Reglas:"
print "X,y,z,w"

n=None
while not isinstance(n, int):
	print "Cuantos equipos?"
	n = int(raw_input())
teams = {}
for x in range(1,n+1):
	print "Nombre del equipo %d:" % x
	name = raw_input() 
	teams[name] = 0

f = open('palabras.txt','r')
palabras = f.read().splitlines()

def one_minute(time_ini):
	period = timedelta(minutes=1)
	if (time_ini+period) == datetime.now():
		return True
	else:
		return False 

for key, value in teams.iteritems():
	print "Turno del Equipo %s" % key
	time.sleep(3)
	time_ini = datetime.now()
	i = 0
	while (not one_minute(time_ini)) and palabras:
		print palabras[i]
		result = raw_input()
		if result!='p' and result!='pass':
			teams[key]+=100
		palabras.pop(i)
		if palabras==None:
			print "Se acabo"
			break
print teams
print "Gano el equipo %s" % max(teams, key=lambda k: teams[k])
