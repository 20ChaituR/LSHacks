import urllib
import random

def getProb(url):
    page = urllib.urlopen(url).read()

    probInd = page.find(
        '<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><h2><span class="mw-headline" id="Problem">Problem</span></h2>')
    pShift = 135
    pEnd = -1
    for i in range(probInd + pShift, len(page)):
        if (page[i] == '?'):
            pEnd = i + 1
            break

    problem = page[probInd + pShift:pEnd]
    return problem

def getAns(url):
    page = urllib.urlopen(url).read()
    ansInd = page.find(r'\boxed{\textbf{')

    aBeg = 18
    for i in range(ansInd, len(page)):
        if (page[i] == '}'):
            aBeg = i + 1
            break

    aEnd = -1
    checkText = '}'
    for i in range(aBeg, len(page)):
        if (page[i:i + len(checkText)] == checkText):
            aEnd = i

    answer = page[aBeg: aEnd]
    return(answer)

def getRandomProblem():
    amc = "/Users/cravuri/Documents/harker/LSHacks/src/generateProb/AMC.in"
    f = open(amc, 'r')
    lines = f.read().split('\n')
    probnum = random.randint(0, len(lines) / 2 - 1)
    return lines[2*probnum:2*probnum + 2]

for i in range(1, 26):
    prob = getRandomProblem()
    print "Problem " + str(i) + ": " + prob[0]
    print "Answer " + str(i) + ": " + prob[1]
