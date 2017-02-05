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

def getRandomProb():
    year = str(random.randint(2, 16))
    prob = str(random.randint(1, 25))
    level = random.randint(0, 1)
    type = random.randint(0, 1)
    if (len(year) == 1):
        year = "0" + year
    if (level == 0):
        level = '10'
    else:
        level = '12'
    if (type == 0):
        type = 'A'
    else:
        type = 'B'
    url = "http://artofproblemsolving.com/wiki/index.php/20" + year + "_AMC_" + level + type + "_Problems/Problem_" + prob
    #url = "http://artofproblemsolving.com/wiki/index.php/2014_AMC_12B_Problems/Problem_9"
    amc = [getProb(url), getAns(url)]
    print url
    print amc[0]
    print amc[1]

getRandomProb()