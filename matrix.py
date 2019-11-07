import csv

class Matrix:
	def __init__(self,p):
		self.path = p
		reader = csv.reader(open(p), delimiter=";")
		self.stages = list(reader)

	def calculSatisfacton(self,p,pListe):
		sat = 0	
	
		if len(pListe) == 0 :
			 
			return 100000000
		for i in pListe:
			sat=sat + int(self.stages[i][p.id])

		malus = p.minStage - len(pListe)
		if malus > 0:
			sat=sat+malus*100000000
		return sat/len(pListe)
