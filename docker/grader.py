#This is a template for the grader

from onpit import Grader
from os.path import join, exists

class LabGrader(Grader):
	@Grader.addStep(name='step1')
	def step1(self, workingDir, inputCommand):
		if inputCommand == "git clone https://github.com/kwendim/IntroductionToOs.git":
			return True
