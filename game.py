from Rollen import *

def main():
	print("Game::main")
	print("Testcode")
	h1 = Hexe()
	s1 = Seherin()
	h1.toeten(s1)
	print(h1.todestrank)
	print(s1.lebendig)



def play():
	pass



if __name__=="__main__":
	main()
