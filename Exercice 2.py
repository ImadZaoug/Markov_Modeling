import numpy as np
#matrice de transition
A = [[0 for i in range(9)]for i in range(9)]
A[0][0]=1
A[8][8]=1
for i in range(1,len(A)-1):
    A[i][i+1]=0.4
    A[i][i-1]=0.6
print("l'expretion de la matrice de transition : ")
print(A)

#calcule de la loi de la fortune de Morty jour avec la probabilité invariante μ0
def Morty_fortune(μ0,A,n):
  return np.dot(μ0, np.linalg.matrix_power(A, n))

#Question 3 :
mu_init = [0]*9 #initialisation
mu_init[3] = 1 #Morty dispose de 3 euros
print("question 3 :")
print("initialement Morcy dispose de 3 euros donc μ0 = [0,0,0,1,0,0,0,0,0] ")
print("n=3 : ",Morty_fortune(mu_init,A,3))
print("n=10 : ",Morty_fortune(mu_init,A,10))
print("n=100 : ",Morty_fortune(mu_init,A,100))


#question 4 :
#Implémentation de la fonction Moty(X):

def Morty(X):
    U= np.random.rand(1)[0]
    if (X==0):
            return 0
    if (X==1):
        if U < 6/10:
            return 0
        else :
            return 2
    if (X==2):
        if U < 6/10:
            return 1
        else :
            return 3
    if (X==3):
        if U < 6/10:
            return 2
        else :
            return 4
    if (X==4):
        if U < 6/10:
            return 3
        else :
            return 5
    if (X==5):
        if U < 6/10:
            return 4
        else :
            return 6
    if (X==6):
        if U < 6/10:
            return 5
        else :
            return 7
    if (X==7):
        if U < 6/10:
            return 6
        else :
            return 8
    if (X==8):
        return 8

#Question 4 :
def simulation(euros,n_steps):
    # Initialisation de l'état initial
    X = euros

    # Nombre de pas de la simulation
    n_steps = n_steps

    # Tableau pour enregistrer les états successifs
    states = np.zeros(n_steps)
    states[0] = X

    # Boucle pour simuler la chaîne de Markov
    for i in range(1, n_steps):
        X = Morty(X)
        states[i] = X

    # Calcul de la proportion de chaque état
    proportion_0 = np.mean(states == 0)
    proportion_1 = np.mean(states == 1)
    proportion_2 = np.mean(states == 2)
    proportion_3 = np.mean(states == 3)
    proportion_4 = np.mean(states == 4)
    proportion_5 = np.mean(states == 5)
    proportion_6 = np.mean(states == 6)
    proportion_7 = np.mean(states == 7)
    proportion_8 = np.mean(states == 8)
    return [proportion_0,proportion_1,proportion_2,proportion_3,proportion_4,proportion_5,proportion_6,proportion_7,proportion_8]



def pr(euros,n_répétition,n_steps):
    # Nombre de simulation
    n_rep = n_répétition
    
    # Tableau pour enregistrer les résultats de chaque simulation
    states = [0]*n_rep

    # Boucle pour générer 100 simulation :
    for i in range(0, n_rep):
        states[i] = simulation(euros,n_steps)
    states = np.transpose(states)
    # Calcul de la proportion de chaque état
    proportion_0 = np.mean(states[0])
    proportion_1 = np.mean(states[1])
    proportion_2 = np.mean(states[2])
    proportion_3 = np.mean(states[3])
    proportion_4 = np.mean(states[4])
    proportion_5 = np.mean(states[5])
    proportion_6 = np.mean(states[6])
    proportion_7 = np.mean(states[7])
    proportion_8 = np.mean(states[8])
    return [proportion_0,proportion_1,proportion_2,proportion_3,proportion_4,proportion_5,proportion_6,proportion_7,proportion_8]
#Question 4 :
print("question 4 :")
print("n=100 : ",pr(3,500,100))
print("n=1000 : ",pr(3,500,1000))

#Question 5 :
def Esperance(n_simulation,euros,n_steps):
    # On calcule le nombre de fois que la simulation converge vers l'état 0 
    s=0
    # Boucle pour générer 100 simulation :
    for i in range(0, n_simulation):
        #nombre de visite à l'état 0 > nombre de visite à l'état 8 ==> la simulation converge vers l'état 0(état absorbant)
        if simulation(euros,n_steps)[0] > simulation(euros,n_steps)[8] :
            s+=1
    return s
print("question 5 :")
print("n=100 : ",Esperance(100,3,1000))