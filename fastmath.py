#!/usr/bin/python

# Fast Math
# *********
# 
# ./flashmath.py <NumQuestions> <difficulty: 1-4>
# 
# Takes number of reps
# Presents flash card 
# Checks your answer

import sys
import random
import time

class flashcard:
	def __init__(self, difficulty):
		if ( difficulty == 1):
			self.minrange = 0
			self.maxrange = 9  
		elif (difficulty == 2):
			self.minrange = -9
			self.maxrange = 9
		elif (difficulty == 3):
			self.minrange = -15
			self.minrange = 15
		elif (difficulty == 4):
			self.minrange = -100
			self.maxrange = 100
		else:
			print "ERR: enter a difficulty 1,2 or 3"
		self.opsym = ['+', '-', '*', '/']
	
	def setformula(self):
		self.arg1 = random.randint(self.minrange, self.maxrange)
		self.arg2 = random.randint(self.minrange, self.maxrange)
		self.op = random.randint(0,3)

	def printformula(self):
		print "\t", self.arg1, self.opsym[self.op], self.arg2 
		print "-----------------\n=\t",

	def printCorrect(self):
		print "\t\t\t  0 0"
		print "\t\t\t \___/"

	def printIncorrect(self):
		print "\t\t\t  0 0"
		print "\t\t\t  ___"
		print "\t\t\t /   \\"

	def calcanswer(self):
		self.answer = eval(str(self.arg1) + self.opsym[self.op] + str(self.arg2))

def welcome():
	print "*****************"
	print "*   Fast Math   *"
	print "*****************"
	print

def goodbye(numcorrect, totaltime):	
	print "*****************"
	print "* ", numcorrect, " / ", sys.argv[1], " *"
	print "* ", round(totaltime,2), " seconds", " *"
	print "*****************"

def main():
	welcome()
	card = flashcard(int(sys.argv[2]))
	numcorrect = 0	
	start = time.time()
	for i in range(0, int(sys.argv[1])):
		card.setformula()
		card.calcanswer()
		card.printformula()	
		if (input() == card.answer):
			numcorrect += 1
			card.printCorrect() 
		else:
			card.printIncorrect()
		print
	totaltime = time.time() - start
	goodbye(numcorrect, totaltime)
			

	
main()
