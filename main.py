import csv
import numpy
import random
from random import shuffle
from prof import Prof
from matrix import Matrix

nbSwap=0
nbPick=0
def minProf(l):
	pr=None
	m=1000
	for p in l:
		if len(p.stages)<=m and len(p.stages)< p.maxStage:
			pr=p
			m=len(p.stages)
	return pr


def randomSwitch(p,p2):
	i = random.randint(0,len(p.stages)-1)	
	j = random.randint(0,len(p2.stages)-1)	
	t=p.stages[i]
	p.stages[i]=p2.stages[j]
	p2.stages[j]=t


def findBest(p,p2,i,matrix):
	l1=p.stages[:]
	l2=p2.stages[:]

	sat = (p.satisfaction + p2.satisfaction )/2

	for j in p2.stages:
	 
		l1.remove(i)
		l2.remove(j)
		l1.append(j)
		l2.append(i)
		
		sat2 = (matrix.calculSatisfacton(p,l1) + matrix.calculSatisfacton(p2,l2))/2
		if sat > sat2 :
			p.stages = l1[:]
			p2.stages=l2[:]
			p.satisfaction = matrix.calculSatisfacton(p,p.stages)
			p2.satisfaction = matrix.calculSatisfacton(p2,p2.stages)
			sat = (p.satisfaction + p2.satisfaction )/2
			global nbSwap
			nbSwap=nbSwap+1
			return True
		else : 
			l1=p.stages[:]
			l2=p2.stages[:]
	return False	
	


def findSwitch(p,p2,matrix):
	i=0	
	while i<len(p.stages):
		j=p.stages[i]
		if findBest(p,p2,j,matrix):
			i=0
		else:
			i=i+1


def findPick(p,p2,matrix):
	for i in p2.stages:
		l1=p.stages[:]
		l2=p2.stages[:]
		if p.addPossible():
			l1.append(i)
			l2.remove(i)
			sat2 = (matrix.calculSatisfacton(p,l1) + matrix.calculSatisfacton(p2,l2))/2
			p.satisfaction = matrix.calculSatisfacton(p,p.stages)
			p2.satisfaction = matrix.calculSatisfacton(p2,p2.stages)
			sat = (p.satisfaction + p2.satisfaction )/2
			if sat > sat2 :
				
				if p2.removeStages(i,matrix) :
					global nbPick
					nbPick=nbPick+1
					p.addStages(i,matrix)
		
			

def calculSatisfaction(l):
	sat = 0
	for p in l:
		sat=sat+p.satisfaction
	return sat


nbProf = 60
nbStage = 203

nbStageMini=4
nbStageMaxi=6

matrix = Matrix("testCSV.csv")

listProf=[]
for i in range(0,nbProf):
	listProf.append(Prof(i,random.randint(nbStageMini, nbStageMaxi)))


nbStageA=0

while nbStageA < nbStage:
	p = minProf(listProf)
 
	if not p == None:
  		if p.addStagesInit(nbStageA,matrix) :
  			nbStageA=nbStageA+1


for p in listProf:
	p.satisfaction = matrix.calculSatisfacton(p,p.stages)
	print(p.toString())

nbGeneration = 10
historique=[]
for j in range(0,nbGeneration):

	print("randomisation")
	for i in range(0,100):
		randomSwitch(listProf[random.randint(0,len(listProf)-1)],listProf[random.randint(0,len(listProf)-1)])

	historique.append(calculSatisfaction(listProf)/len(listProf))
	for i in range(0,nbGeneration):
		print ("Generation "+str(i)+" sur "+str(nbGeneration*nbGeneration) + " Satisfaction general :"+str(calculSatisfaction(listProf)/len(listProf))+" nbSwap:"+str(nbSwap)+" nbPick:"+str(nbPick))
		
		for p in listProf:
			for p2 in listProf:
				if not p.id==p2.id :
					
					findSwitch(p,p2,matrix)
					findPick(p,p2,matrix)







print(historique)

 
