# print('CECI EST UN JEU QUI TESTE VOTRE MEMOIRE', end="")
# print('vous allez voir une série de mots et vous devrez dire si vous l\'avez déjà vu ou non', end="")
from playGame import playGame

import os
os.system('cls')
playGame()
#algo
#Ouvrir fichier en lecture
#essayer de trouver le mot dans le fichier
#si on le trouve, on vérifie le choix, si on a dit qu'on l'avait déjà vu, on donne les points et on break la boucle, si il a dit qu'il était nouveau, on affiche loose, met fin à la partie et affiche le score, (on propose de rejouer)
#si on ne le trouve pas et qu'on sort de la boucle avec wordFounded = True, on perds
#
#
  
    
  # else:
  #   for UsedWord in UsedWords:
  #     if(Mot == UsedWord):
  #       print("Bien joué!")
  #       score +=1
  #       game = "playing"
      
  
  

# print(mots)
# for mot in mots:
#   W.write(mot)
# F.close()
# W.close()