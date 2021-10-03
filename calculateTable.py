%quickly calculate a Table for the exercise

import math


v = 3*pow(10, 8)
fr = float(input("resonant Frequency \n"))
er = float(input("electric constant\n"))
h = float(input("h, please\n"))
R = float(input("input impedance\n"))
a = float(input("radius\n"))

def actual_length(v, ereff, W, h, fr):
	dL = 0.412 * h * ((ereff + 0.3)*(W/h + 0.264))/((ereff - 0.258)*(W/h + 0.8))
	Leff = v / (2*fr*math.sqrt(ereff))
	L = Leff - 2*dL
	return L

def reactance(er, h, fr, a):
	n = 376.7303
	mr = 1
	la = 299792458 / fr
	ga = 0.57722
	X_p = n * mr* (h/la)*(math.log(1/(a/la)) -ga-math.log(math.pi)-math.log(math.sqrt(mr*er)))
	return X_p

def groundplane_dim(h, L, W):
	return [6*h + L, 6*h + W] #L_g, W_g


W = v/(2*fr) * math.sqrt(2/(er+1))
ereff = (er + 1)/2 + ((er-1)/2)*(1/math.sqrt(1+12*(h/W)))

L = actual_length(v, ereff, W, h, fr)
x = L/4
X_p = reactance(er, h, fr, a)
L_p = complex(R, X_p)

returnTable = {
	"W": W, 
	"ereff": ereff, 
	"L": L,
	"x_0": x,
	"X_p": X_p,
	"L_p": L_p,
	"L_g and W_g": groundplane_dim(h, L, W)
}
print(returnTable)
