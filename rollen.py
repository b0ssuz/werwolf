from Karte import Karte
from Gut import Gut

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
class Jaeger(Karten,Gut):
	def toeten(self,other):
		other.lebendig = False

