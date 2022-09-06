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



