

class Prof:
	def __init__(self,i):
		self.id=i
		self.stages = []
		self.satisfaction = 100000000
		self.maxStage = 6
		self.minStage=4

	def __init__(self,i,stage):
		self.id=i
		self.stages = []
		self.satisfaction = 100000000
		self.maxStage = stage
		self.minStage=4

	def addStagesInit(self,s,m):
		listeS = self.stages[:]
		listeS.append(s)
		if len(self.stages)<self.maxStage:
			self.stages.append(s)
			self.satisfaction = m.calculSatisfacton(self,self.stages)
			return True
		else :
			return False
	def addPossible(self):
		if len(self.stages)<self.maxStage:
			return True
		else :
			return False

	def addStages(self,s,m):
		
		if len(self.stages)<self.maxStage:
			self.stages.append(s)
			self.satisfaction = m.calculSatisfacton(self,self.stages)
			return True
		else :
			return False

	def removeStages(self,s,m):
		 
		#if len(self.stages)>self.minStage:
		self.stages.remove(s)
		self.satisfaction = m.calculSatisfacton(self,self.stages)
		return True
		#else :
		#	return False
	
	def toString(self):
		return "["+str(self.id)+" :S"+str(self.stages) +", sat:"+ str(self.satisfaction)+"]"
