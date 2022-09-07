#2.2.3
def dollar():
    for n in range(0,11):
        euro = 2**n
        dollar = euro*1.12
        print(euro," euro(s) =",dollar," dollar(s)")

#2.2.4
def triple():
    nb=1
    for i in range(12):
        nb*=3
        print(nb)

#3.2.1
def conversion(tf):
    tc=(tf-32)/1.8
    print(tc)

#3.2.2
def nomMois(n):
    if n>12:
        print("Veuillez saisir un mois valide !")
    else:
        l=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
        print(l[n-1])

#3.2.3
def note(N):
    if N >= 80:
        print("Vous avez obtenu un A !")
    elif 80 > N >= 60:
        print("Vous avez obtenu un B !")
    elif 60 > N >= 50:
        print("Vous avez obtenu un C !")
    elif 50 > N >= 40:
        print("Vous avez obtenu un D !")
    elif N < 40:
        print("Vous avez obtenu un E !")

#3.2.4
def triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        print("Votre triangle est valide")
        if a==b==c:
            print('Votre triangle est équilatéral')
        if a==b or a==c or b==c:
            print('Votre triangle est isocèle')
        if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
            print("Votre triangle est rectangle")
    else:
        print("Votre triangle n'est pas valide")

#3.3
def triangle(hauteur):
    for h in range(hauteur,0,-1):
        for c in range(1,h+1):
            print('*',end='')
        print()

#4.1
def rechercheMin(liste):
    min = Liste[0]
    for i in range(1,len(liste)):
        if Liste[i] < min:
            min = Liste[i]
    return min

Liste=[20,8,9,2,35,49]
#print(rechercheMin(Liste))

#4.2
def moyenneVersion1(liste):
    total=0
    for i in range(0,len(liste)):
        total=total+Liste2[i]
        moyenne=total/len(Liste2)
    return moyenne

Liste2=[20,8,9,2,35,49]
#print(moyenneVersion1(Liste2))

#4.2.2
def listedoublon(liste):
    liste2=[]
    for i in range(0,len(liste1)):
        if liste1[i] not in liste2:
            liste2.append(liste1[i])
    liste2.sort()
    return liste2

liste1=[14,20,45,31,14,74,20,94,10]
#print(listedoublon(liste1))
