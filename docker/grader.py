#This is a template for the grader

from onpit import Grader
from os.path import join, exists

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "docker info":
			return True

	@Grader.addStep(name='step2')
	def step2(self, workingDir, inputCommand):
		if inputCommand == "docker run -it alpine sh":
			return True
