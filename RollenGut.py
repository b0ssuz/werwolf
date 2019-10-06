from Karte import Karte
from Gut import Gut

"""
Rollen: Hexe,Seherin,Dorfbewohner,Jason,Jaeger,Reiseleiterin
"""


class Hexe(Karte,Gut):
	heiltrank = True
	todestrank = True
	def heilen(self,other):
		other.lebendig = True
		self.heiltrank = False
	def toeten(self,other):
		other.lebendig = False
		self.todestrank = False	
class Seherin(Karte,Gut):
	pass
class Dorfbewohner(Karte,Gut):
	pass
class Jason(Karte,Gut):
	pass
class Jaeger(Karte,Gut):
	def toeten(self,other):
		other.lebendig = False
class Reiseleiterin(Karte,Gut):
	def in_den_urlaub_schicken(self,other):
		other.verreist = True

