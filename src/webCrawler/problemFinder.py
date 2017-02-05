import urllib

page = urllib.urlopen("http://artofproblemsolving.com/wiki/index.php/2013_AMC_10B_Problems/Problem_9").read()

probInd = page.find('<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><h2><span class="mw-headline" id="Problem">Problem</span></h2>')
pShift = 135
pEnd = -1
for i in range(probInd+pShift, len(page)):
    if (page[i] == '?'):
        pEnd = i + 1
        break

problem = page[probInd + pShift:pEnd]
print(problem)

ansInd = page.find('box')
print(ansInd)

aBeg = 18
for i in range(ansInd, len(page)):
    print(page[i])
    if (page[i] == '}'):
        aBeg = i + 1
        break

aEnd = -1
for i in range(aBeg, len(page)):
    if (page[i:i + 2] == '}$'):
        aEnd = i

answer = page[aBeg: aEnd]
print(answer)