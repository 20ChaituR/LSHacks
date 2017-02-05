# import pytesseract
# from PIL import Image
# from PIL import ImageFilter

import random
import math

class answerSheet(object):

    def __init__(self):
        self.file = "/Users/cravuri/Documents/harker/LSHacks/src/webCrawler/AMC.in"

    def generateQuad(self):
        [a, b, c] = [random.randint(1, 3), random.randint(1, 20), random.randint(1, 20)]
        temp = []
        temp.append(str(a) + "x^2 + " + str(b) + "x + " + str(c))
        if (math.pow(b,2) - 4*a*c < 0):
            temp.append("none")
        else:
            answer1 = (-b + math.sqrt(math.pow(b, 2)-4*a*c))/2*a
            answer2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
            if (answer1 == answer2):
                temp.append(str(answer1))
            else:
                temp.append(str(answer1))
                temp.append(str(answer2))
        return temp

    def generateLinear(self):
        [a, b, c] = [random.randint(1, 25), random.randint(1, 25), random.randint(1, 25)]
        temp = []
        temp.append(str(a) + "x + " + str(b) + " = " + str(c))
        a *= 1.0
        b *= 1.0
        c *= 1.0
        t = (c-b)/a
        temp.append(str(t))
        return temp

    def determinant(self, result, rows, cols):
        if rows == 2:
            return result[0][0] * result[1][1] - result[0][1] * result[1][0]
        determinant1 = 0
        determinant2 = 0
        for i in range(rows):
            temp = 1
            temp2 = 1
            for j in range(cols):
                temp *= result[(i + j) % cols][j]
                temp2 *= result[(i + j) % cols][rows - 1 - j]
            determinant1 += temp
            determinant2 += temp2
        return determinant1 - determinant2

    def generateSystem(self):
        number = random.randint(2, 3)
        if number == 2:
            coefficients = []
            for i in range(6):
                coefficients.append(random.randint(1, 25))
            [a, b, c, d, e, f] = coefficients
            temp = [0, 0, 0, 0]
            temp[0] = str(a) + "x + " + str(b) + "y = " + str(c)
            temp[1] = str(d) + "x + " + str(e) + "y = " + str(f)
            for i in range(6):
                coefficients[i] *= 1.0
            [a, b, c, d, e, f] = coefficients
            t = (c * e - b * f) / a * e - b * d
            temp[2] = str(t)
            u = (c - a * t) / b
            temp[3] = str(u)
            return temp
        if number == 3:
            coefficients = []
            for i in range(12):
                coefficients.append(random.randint(1, 25))
            [a, b, c, d, e, f, g, h, i, j, k, l] = coefficients
            temp = [0, 0, 0, 0, 0, 0]
            temp[0] = str(a) + "x + " + str(b) + "y + " + str(c) + "z = " + str(d)
            temp[1] = str(e) + "x + " + str(f) + "y + " + str(g) + "z = " + str(h)
            temp[2] = str(i) + "x + " + str(j) + "y + " + str(k) + "z = " + str(l)
            for i in range(12):
                coefficients[i] *= 1.0
            [a, b, c, d, e, f, g, h, i, j, k, l] = coefficients
            det = [[], [], []]
            detx = [[], [], []]
            dety = [[], [], []]
            detz = [[], [], []]
            det[0] = [a, b, c]
            det[1] = [e, f, g]
            det[2] = [i, j, k]
            detx[0] = [d, b, c]
            detx[1] = [h, f, g]
            detx[2] = [l, j, k]
            dety[0] = [a, d, c]
            dety[1] = [e, h, g]
            dety[2] = [i, l, k]
            detz[0] = [a, b, d]
            detz[1] = [e, f, h]
            detz[2] = [i, j, l]
            x1 = self.determinant(detx, 3, 3) / self.determinant(det, 3, 3)
            y1 = self.determinant(dety, 3, 3) / self.determinant(det, 3, 3)
            z1 = self.determinant(detz, 3, 3) / self.determinant(det, 3, 3)
            temp[3] = str(x1)
            temp[4] = str(y1)
            temp[5] = str(z1)
            return temp

    def getRandomProblem(self):
        amc = self.file
        f = open(amc, 'r')
        lines = f.read().split('\n')
        probnum = random.randint(0, len(lines) / 2 - 1)
        return lines[2*probnum:2*probnum + 2]

    def generateRandomProblem(self):
        probType = random.randint(0, 2)
        prob = []
        if (probType == 0):
            prob = self.generateQuad()
        if (probType == 1):
            prob = self.generateLinear()
        if (probType == 2):
            prob = self.generateSystem()
        prob.append(probType)
        return prob

    def getText(self, img):
        image = Image.open(img)
        image.filter(ImageFilter.SHARPEN)
        text = pytesseract.image_to_string(image)
        return text

    answerKey = []

    def normalize(self, prob):
        normProb = ""
        a = prob.split(" ")
        curLen = 0
        for i in range(len(a)):
            normProb = normProb + a[i] + " "
            curLen = curLen + len(a[i])
            if (curLen >= 72):
                normProb = normProb + "\n"
                curLen = 0
        return normProb

    def printCompetitionProblemSheet(self):
        out = open("/Users/cravuri/Documents/harker/LSHacks/src/AMC.out", "w")
        for i in range(1, 26):
            prob = self.getRandomProblem()
            out.write("Problem " + str(i) + ". " + self.normalize(prob[0]))
            for _ in range(10):
                out.write("\n")
            out.write("Answer: " + "\n" + "\n")
            self.answerKey.append(str(prob[1]))

    def printAlg1ProblemSheet(self):
        out = open("/Users/cravuri/Documents/harker/LSHacks/src/AMC.out", "w")
        for i in range(1, 16):
            prob = self.generateRandomProblem()
            type = prob[len(prob) - 1]
            if type == 0:
                out.write("Problem " + str(i) + ". Solve the following quadratic equation for x: \n" + self.normalize(prob[0]))
                for _ in range(10):
                    out.write("\n")
                out.write("Answer: " + "\n" + "\n")
                if (len(prob) == 3):
                    self.answerKey.append(prob[1])
                else:
                    self.answerKey.append(prob[1] + ", " + prob[2])
            if type == 1:
                out.write("Problem " + str(i) + ". Solve the following equation for x: \n" + self.normalize(prob[0]))
                for _ in range(10):
                    out.write("\n")
                out.write("Answer: " + "\n" + "\n")
                self.answerKey.append(prob[1])
            if type == 2:
                if (len(prob) == 5):
                    out.write("Problem " + str(i) + ". Solve the following system of equations for x and y: \n" + self.normalize(prob[0]) + "\n" + self.normalize(prob[1]))
                    for _ in range(10):
                        out.write("\n")
                    out.write("Answer: " + "\n" + "\n")
                    self.answerKey.append(str(prob[2]) + ", " + str(prob[3]))
                if (len(prob) == 7):
                    out.write("Problem " + str(i) + ". Solve the following system of equations for x, y, and z: \n" + self.normalize(
                        prob[0]) + "\n" + self.normalize(prob[1]) + "\n" + self.normalize(prob[2]))
                    for _ in range(10):
                        out.write("\n")
                    out.write("Answer: " + "\n" + "\n")
                    self.answerKey.append(str(prob[3]) + ", " + str(prob[4]) + ", " + str(prob[5]))

x = answerSheet()
x.printAlg1ProblemSheet()