from Karte import Karte
from Boese import Boese

"""
Rollen: Werwolf, BabyWerwolf

"""


class Werwolf(Karte,Boese):
	def fressen(self,other):
		if type(other) is BabyWerwolf:
			other.id = False
class BabyWerwolf(Karte,Boese):
	id = True # identität auf Gut gesetzt
	aktiv = False
