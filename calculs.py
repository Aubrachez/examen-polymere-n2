import os
os.system('cls')
num=0
MMn=0
MMw=0
R = 8.314 # constante des gaz parfaits (J/(mol*K))
print("Réponse pour le calcul du MMn et MMw ainsi que l'écart de température par la méthode ébullioscopique")
print("Version 1.0")
print(" ")
print(" ")
print(" ")
### variable calcul MMn et MMw
x=12
########## nomnbre d'unité et ensuite la valeur par laquelle x est multiplié
valeurs = [[8,x*1000],[28,x*x*100],[98,x*x*x*10],[18,x*x*x*x*4],[8,x*x*x*x*x]]



#### variable calcul écart temprature et osmométrie
rho =0.8 # masse volumique du solvant (kg/m³)
Tb = 97 # Température d'ébullition du solvant pur (°C)
DHvap = 792 # Enthalpie de vaporisation de l'eau (kJ/kg)
solubilité = 24.4 #en Mpa^-2
poid_polymere = 0.002 # en kg
poid_solvant = 0.100  # en kg
temperature_osmotique = 20 # en °C
Mpropanol = 60.1 # masse molaire du propanol (g/mol)


# calcul du MMn
for i in valeurs:
   
    num=num+(i[0]*i[1])

deno = 0

for j in valeurs:
    deno = deno + j[0]
MMn = round(num/deno,0)
print("="*40)
print("Masse molaire" )
print("="*40)
print("Masse molaire en nombre : MMn = " + str(MMn))


# calcule du MMw

num=0
for i in valeurs:
   
    num=num+(i[0]*i[1]*i[1])

deno = 0

for j in valeurs:
    deno = deno +(j[0]*j[1])

MMw = round(num/deno,0)
print("Masse molaire en masse MMw = " + str(MMw))

# calcul MZ 

num=0
for i in valeurs:
   
    num=num+(i[0]*i[1]*i[1]*i[1])

deno = 0

for j in valeurs:
    deno = deno +(j[0]*j[1]*j[1])

MMz = round(num/deno,0)
print("Masse molaire spécial MMz = " + str(MMz))


print(" "*40)
print(" "*40)
print("="*40)
print("Valeur de PI calculé")
print("="*40)
#calcul PI
pi = round(MMw/MMn,1)
print("PI = " + str(pi))


print(" "*40)
print(" "*40)
####### écart température méthode ébullioscopique ################################################################
print("="*40)
print("Différence de température")
print("="*40)


Mpolymere = MMn
Wpolymere = poid_polymere/(poid_polymere+poid_solvant) # fraction massique du polymère
Wsolvant = poid_solvant/(poid_polymere+poid_solvant) # fraction massique du solvant
Wglobal = Wpolymere/Wsolvant # fraction massique globale


T_phi = Tb+273.15 # température de l'ébullioscopie (K)

delta_H = DHvap*Mpropanol # Enthalpie de vaporisation (J/kg)

delta_T = round((R*T_phi*T_phi/delta_H)*(Mpropanol/MMn)*Wglobal,4) # écart de température (°C)
print("Différence de température = " + str(round(delta_T,4)) + " °C")
print(" "*40)
print(" "*40)
print("="*40)
print("pression osmotique")
print("="*40)
##### calcule osmométrie ################################################################
concentration = 1000*rho*poid_polymere/poid_solvant # concentration en kg/m³
Pression = (8.314*(temperature_osmotique+273.15)*concentration/MMn)*1000
print("Pression osmotique = " + str(round(Pression,0)) + " Pa")



