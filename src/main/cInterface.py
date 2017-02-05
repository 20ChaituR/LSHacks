import objc
from Foundation import NSObject
from main import answerSheet
#this class finally prints the sheet with questions, space for work and space for answers
class PyAnswerSheet(NSObject):

    def init(self):
        self = super(PyAnswerSheet, self).init()
        self.py = answerSheet()
        return self

    @objc.signature('i@:')
    def printCompetitionProblemSheet(self):
        return self.py.printCompetitionProblemSheet()

    @objc.signature('@@:i')
    def printAlg1ProblemSheet(self):
        return self.py.printAlg1ProblemSheet()
