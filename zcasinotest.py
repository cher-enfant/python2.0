from random import randrange
from math import ceil
while True:
    a=int()
    n=randrange(0,49)
    while a<=0:
        try:
            print("entre le somme avec laquelle vous voulez debuter la partie:")
            a=int(input())
           
        except ValueError:
            print(" veullez entre un chiffre.")
    boule=int()
    while boule<0 or boule >49:
        try:
            print(" veuillez  choisir une boule entre 0 et 49: ")
            boule=int(input())
        except ValueError:
            print(" veullez entre un chiffre.")

    prix=int()
    while prix <=0 or prix>a :
        try:
            print("entre la somme que vous voulez miser:")
            prix=int(input())
        except ValueError:
            print(" veullez entre un chiffre.")
   



       

    

           
    
           
    
    
    
    
    
    
    
    
    
    
        
        
            
