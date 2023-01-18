import numpy as np
#matrice de transition
A=[[5/6,1/12,1/12],
   [1/4,1/2,1/4],
   [1/4,0,3/4]]

#La chaîne de Markov est irréductible,
#car il est possible de passer de n'importe quel état à n'importe quel autre état en un nombre fini de transitions.
#Elle est aussi apériodique, car il n'y a pas de période fixe au cours de laquelle l'état de la chaîne se répète(PGCD = 1).

def probabilité_invariante(x):
    s=0
    min=1000
    b=1000
    a=0
    #résolution du système X.v= cte.v(valp=valeur propre; vecp=vecteur propre)
    valp, vecp = np.linalg.eig(np.transpose(x))
    vecp=np.transpose(vecp)
    #vu que A contient des valeur dans Q donc il y a des inprécision de calcule(5/6=0,8333..)
    #ce qui peut engendrer des petites erreurs au niveau des valeurs propres donc on prend la valeur propre la plus proche de 1
    for i in range(len(valp)):
        if abs(valp[i]-1)<0.01:
            b=i
    #normalisation
    for j in range(len(vecp[b])):
                s+=vecp[b][j]
                a=(vecp[b])/s
    return a
print("question 2 :")
print("la probabilité invariante s'écrit sous forme : ",probabilité_invariante(A))

#calcule de loi au n-ième jour avec la probabilité invariante μ0
def état_jour_n(μ0,A,n):
  return np.dot(μ0, np.linalg.matrix_power(A, n))

#Question 3 - 4 :
mu_init = [1,0,0] #initialement en bonne santé
mu_init1 = [0,1,0] #initialement enrhumé
mu_init2 = [0,0,1] #initialement malade
print("question 3 :")
print("pour μ0 = [1,0,0] ")
print("n=5 : ",état_jour_n(mu_init,A,5))
print("n=10 : ",état_jour_n(mu_init,A,10))
print("n=50 : ",état_jour_n(mu_init,A,50))
print("n=100 : ",état_jour_n(mu_init,A,100))
print("question 4 :")
print("pour μ0 = [0,1,0] ")
print("n=5 : ",état_jour_n(mu_init1,A,5))
print("n=10 : ",état_jour_n(mu_init1,A,10))
print("n=50 : ",état_jour_n(mu_init1,A,50))
print("n=100 : ",état_jour_n(mu_init1,A,100))
print("pour μ0 = [0,0,1] ")
print("n=5 : ",état_jour_n(mu_init2,A,5))
print("n=10 : ",état_jour_n(mu_init2,A,10))
print("n=50 : ",état_jour_n(mu_init2,A,50))
print("n=100 : ",état_jour_n(mu_init2,A,100))


#Fonction qui calcule A^n
def Matrice_puissance_n(A,n):
  return np.linalg.matrix_power(A, n)

#Question 5 :
print("question 5 :")
print("Calcule de A^n")
print("n=5 : ",Matrice_puissance_n(A,5))
print("n=10 : ",Matrice_puissance_n(A,10))
print("n=50 : ",Matrice_puissance_n(A,50))
print("n=100 : ",Matrice_puissance_n(A,100))

#question 6 :
#Implémentation de la fonction adam(X):

def adam(X):
    U= np.random.rand(1)[0]
    if (X==1):
        if U < 5/6:
            return 1
        elif 5/6< U < 11/12:
            return 2
        else :
            return 3
    if (X==2):
        if U < 1/4:
            return 1
        elif 1/4 <U < 3/4:
            return 2
        else :
            return 3
    if (X==3):
        if U < 1/4:
            return 1
        else :
            return 3

#Question 7 :

# Initialisation de l'état initial
X = 1

# Nombre de pas de la simulation
n_steps = 100000

# Tableau pour enregistrer les états successifs
states = np.zeros(n_steps)
states[0] = X

# Boucle pour simuler la chaîne de Markov
for i in range(1, n_steps):
    X = adam(X)
    states[i] = X

# Calcul de la proportion de chaque état
proportion_1 = np.mean(states == 1)
proportion_2 = np.mean(states == 2)
proportion_3 = np.mean(states == 3)
print("question 7 :")

print("Proportion de l'état 1 :", proportion_1)
print("Proportion de l'état 2 :", proportion_2)
print("Proportion de l'état 3 :", proportion_3)