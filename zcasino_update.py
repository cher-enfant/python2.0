from random import randrange
from math import ceil
a=int()
while a<=0:
        try:
            print("entre le somme avec laquelle vous voulez debuter la partie:")
            a=int(input()) 
        except ValueError:
             print("veuillez entre un chiffre")
print("vous debutez la partie avec",a,"$")
while True:
   n=randrange(0,49)
   prix=int()
   while prix <=0 or prix>a :
        try:
            print("entre la somme que vous voulez miser:")
            prix=int(input())
        except ValueError:
            print(" veullez entre un chiffre.")
   lotto=-1
   while lotto< 0 or lotto> 49:
      try:
            print(" veuillez  choisir une boule entre 0 et 49: ")
            lotto=int(input())
      except ValueError:
            print(" veullez entre un chiffre.")
   print("la roulette tourne... ... et s'arrete sur le numero",n)
   if lotto==n:
        prix*=3 
        a+=prix
        print("vous avez gagnez",prix,"$ et maintenant et vous avez",a,"$ sur votre compte.")
   elif lotto%2==n%2:
        prix+=ceil(prix*0.5)
        a+=prix
        print("vous avez  choisir la bonne couleur vous gagnez",prix,"$ et maintenant et vous avez",a,"$ sur votre compte.")
   else:
        a-=prix
        print("vous avez perdu et maintenant et vous avez",a,"$ sur votre compte.")
   if a<=0:
         print(" vous etes ruine c'est la fin de la partir")
         break
   else:
        print(" vous avez maintant",a,"$")
        k=str
        print("souhaitez- vous quitte le casino(o/n)")
        k=input()
   if k.lower()=="n":
        print("vous quittez le casino avec vos gains.")
        break


         

    
      



       

    

           
    
           
    
    
    
    
    
    
    
    
    
    
        
        
            
