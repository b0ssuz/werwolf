from Karte import Karte
from Boese import Boese



class Werwolf(Karte,Boese):
	def fressen(self,other):
		if type(other) is BabyWerwolf:
			other.id = False
	pass
class BabyWerwolf(Karte,Boese):
	id = True # identität auf Gut gesetzt
	aktiv = False
