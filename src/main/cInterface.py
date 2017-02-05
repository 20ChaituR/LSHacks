import objc
from Foundation import NSObject
from main import answerSheet

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
