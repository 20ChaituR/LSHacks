import random
import math

def generateQuad():
    [a, b, c] = [random.randint(1, 3), random.randint(1, 20), random.randint(1, 20)]
    temp = []
    temp.append(str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0")
    if (math.pow(b,2) - 4*a*c < 0):
        temp.append("none")
    answer1 = (-b + math.sqrt(math.pow(b, 2)-4*a*c))/2*a
    answer2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    if (answer1 == answer2):
        temp.append(str(answer1))
    else:
        temp.append(str(answer1))
        temp.append(str(answer2))
    return temp

def generateLinear():
    [a, b, c] = [random.randint(1, 25), random.randint(-25, 25), random.randint(-25, 25)]
    temp = []
    temp.append(a + "x + " + b + " = " + c)
    a *= 1.0
    b *= 1.0
    c *= 1.0
    t = (c-b)/a
    temp.append(str(t))
    return temp

def determinant(result, rows, cols):
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

def generateSystem():
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
        temp[2] = str(u)
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
        det = []
        detx = []
        dety = []
        detz = []
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
        x1 = determinant(detx, 3, 3) / determinant(det, 3, 3)
        y1 = determinant(dety, 3, 3) / determinant(det, 3, 3)
        z1 = determinant(detz, 3, 3) / determinant(det, 3, 3)
        temp[3] = str(x1)
        temp[4] = str(y1)
        temp[5] = str(z1)
