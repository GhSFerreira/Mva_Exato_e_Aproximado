import numpy as np
import matplotlib.pyplot as plt

K = 3
N = 4
Z = 0
E = 0.01

def maxI(Nia, Ni):
    maior = 0
    for i in range(0, K):
        temp = abs(Nia[i]-Ni[i])
        if temp > maior:
            maior = temp

    return maior


def mvaExato(Si, Vi):

    Ni = np.zeros(K)
    list = []

    for n in range(1, N+1):
        R = 0
        Xi = np.zeros(K)
        Ri = np.zeros(K)

        for i in range(0, K):
            Ri[i] = Si[i] * (1 + Ni[i])

        for j in range(0, K):
            R += (Ri[j]*Vi[j])

        Xo = n / (R + Z)

        for i in range(0, K):
            Ni[i] = Xo*Vi[i]*Ri[i]
            Xi[i] = Xo*Vi[i]

        list.append([R, Xo, n, Ri, Xi, Ni.copy()])

    return list


def mvaAproximado(Si, Vi):
    list = []

    Ni = np.zeros(K)

    for i in range(0, K):
        Ni[i] = N / K

    maiorDA = maxI(Ni, np.zeros(K))
    while maiorDA > E:
        R = 0
        Xi = np.zeros(K)
        Ri = np.zeros(K)

        for i in range(0, K):
            Ri[i] = Si[i] * (1 + (((N-1)/N)*Ni[i]))

        for j in range(0, K):
            R += Ri[j]*Vi[j]

        Xo = N / (R + Z)

        Nia = Ni.copy()

        for i in range(0, K):
            Ni[i] = Xo*Vi[i]*Ri[i]
            Xi[i] = Xo*Vi[i]

        maiorDA = maxI(Nia, Ni)

        list.append([R, Xo, N, Ri, Xi, Ni.copy()])

    return list
     # CPU          D1      D2
Si = [0.005714286, 0.030, 0.025]
Vi = [14, 5, 8]

mvaE = mvaExato(Si, Vi)
#mvaA = mvaAproximado(Si, Vi)

print("\nMVA Exato:\n")
print("R\tXo\tN", end="\t")
for i in range(1,K+1):
    print("R%i" % i, end="\t")

for i in range(1,K+1):
    print("X%i" % i, end="\t")

for i in range(1,K+1):
    print("N%i" % i, end="\t")

print("\n")

for linha in mvaE:
    for coluna in linha:
        if type(coluna) is np.ndarray:
            for item in coluna:
                print("%.3f" % item, end="\t")
        else:
            print("%.3f" % coluna, end="\t")
    print("")
#
#print("\n\n\t\t\t\t\t\t\t\t\tMVA APROXIMADO:\n")

#print("R\tXo\tN", end="\t")
#for i in range(1,K+1):
#    print("R%i" % i, end="\t")

#for i in range(1,K+1):
#    print("X%i" % i, end="\t")

#for i in range(1,K+1):
#   print("N%i" % i, end="\t")

#print("\n")

#for linha in mvaA:
#    for coluna in linha:
#        if type(coluna) is np.ndarray:
#            for item in coluna:
#                print("%.2f" % item, end="\t")
#        else:
#            print("%.2f" % coluna, end="\t")
#    print("")
