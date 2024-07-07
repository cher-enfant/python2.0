import random
while  True:
    print("welcome to plus or less game\n")
    while True:
        print("1.facile\n", end="")
        print("2.moyen\n", end="")
        print("3.  dificile\n" , end="")
        V=int(input())
        if(V in[1,2,3]):
            break
  
        
    


    match V:
        case 1:
            n=random.randint(1,10)
            K=6
            while(K>0):
                print(" entre votre valeur",end="")
                A=input()
                try:
                   A=int(A)
                   
                except ValueError:
                  print( "veuillez entre un monbre entier valide")
                  continue 
                if(A>n):
                    print(" c'est plus petit que cela")# m trouver mesaj sa pi enteresan
                elif(A<n):
                    print("c'est plus grand que cela")
                else :
                   break
                K-=1
        
            if(K!=0):
                print("bravo vous avez devine le nombre en",6-K,"essais !")
            else:
               print("oups vous avez  depasse le nombre de tentatives autorisees. le nombre etait:",n)
 

        case 2:
          n=random.randint(1,100)
          K=6
          while(K>0):
                print(" entre votre valeur",end="")
                A=input()
                try:
                   A=int(A)
                   
                except ValueError:
                  print( "veuillez entre un monbre entier valide")
                  continue 
                if(A>n):
                    print(" c'est plus petit que cela")# m trouver mesaj sa pi enteresan
                elif(A<n):
                    print("c'est plus grand que cela")
                else :
                   break
                K-=1
        
          if(K!=0):
                print("bravo vous avez devine le nombre en",6-K,"essais !")
          else:
               print("oups vous avez  depasse le nombre de tentatives autorisees. le nombre etait:",n)
 

        
    
        case 3 :
            n=random.randint(1,1000)
            K=6
            while(K>0):
                print(" entre votre valeur",end="")
                A=input()
                try:
                   A=int(A)
                   
                except ValueError:
                  print( "veuillez entre un monbre entier valide")
                  continue 
                if(A>n):
                    print(" c'est plus petit que cela")# m trouver mesaj sa pi enteresan
                elif(A<n):
                    print("c'est plus grand que cela")
                else :
                   break
                K-=1
        
            if(K!=0):
                print("bravo vous avez devine le nombre en",6-K,"essais !")
            else:
               print("oups vous avez  depasse le nombre de tentatives autorisees. le nombre etait:",n)
 
         
 
       
        

        case _:
           
           print(" veuillez entre un nombre entre 1 et 3") 
           
             
             
 
    print(" taper oui pour rejouer et non pour  terminer")  
    P=input()        
    if(P.lower()=="oui"):
         continue
    elif(P.lower()=="non"):
        print("merci d'avoir jouer")
        break
