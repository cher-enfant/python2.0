import random
import math
#n=random.randrange(50)
while True:

    while True:
        try:
            print("entre la somme a mise:")
            prix=int(input())
            assert prix>0
        except ValueError:
            print(":veuillez entre un  entier:") 
        except AssertionError:
            print("le prix doit etre superrieur a zero.") 

        if prix>0:
            break


    while True:
        try:
            print("choix votre boule entre 0 et 49.")
            boule=int(input())

            assert boule>=0
        except ValueError:
            print(":veuillez entre un  entier.") 
        except AssertionError:
            print(" la boule doit etre superrieur a zero") 

        if boule>0:
            break
    n=random.randrange(50) 
     
    if boule==n:
        prix=prix*3
        print( "vous avez gagne et la somme gange est",prix)
    elif n%2==0 and boule%2==0:
        prix=prix+(prix*0.5)
        print( "vous avez gagne et la somme gange est",math.ceil(prix))
    elif n%2==1 and boule%2==1:
        prix=prix+(prix*0.5)
        print( "vous avez gagne et la somme gange est",math.ceil(prix))
    elif boule!=n:
        print("vous avez perdu")
    print(" la boule est",n)
    
    print(" voulez vous jouer a nouveau tapez oui sinon tapez non " )
    rep=input()
    if (rep.lower()=="non"):
        break
    