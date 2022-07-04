import os

from random import randint
def playGame():
  score = 0
  print('Bienvenue dans un jeu de mémoire, une série de mots vont vous être proposés')
  print('il vous suffit d\'indiquer s\'il est déjà apparu durant la session de jeu ou s\'il est nouveau.')
  print('1 point vous sera accordé à chaques bonne réponse.')
  print('LETS GO BON COURAGE')
  R = open('Données/UsedWords.txt','w', encoding='utf-8')
  R.writelines('')
  R.close()
  newRound(score)

def newRound(score):
  print('Avez-vous déjà vu ce mot? :\n')
  choice = ""
  validChoice = False
  F = open("Données/ListeMots.txt", "r", encoding='utf-8')
  words = F.readlines()
  word = words[(randint(0, len(words)-1))]
  print("-------> " + word )
  while validChoice != True:
    choice = input("1) DEJA VU!\n2) NOUVEAU !\n")
    # print(choice)
    choice = int(choice)
    if(choice == 1 or choice == 2):
      validChoice = True
      break
    print("1) DEJA VU! \n2) NOUVEAU ! (Concentrez-vous svp)")
    print('\n')
    print('Avez-vous déjà vu ce mot? :\n')
    print("--------> " + word)
  R = open('Données/UsedWords.txt','r', encoding='utf-8')
  UsedWords = R.readlines()
  R.close()
  # open in Append mode to put cursor at the end of the file

  for UsedWord in UsedWords:
    if(word == UsedWord):
      if(choice == 2):
        print("LOOSER")
        print("VOTRE SCORE : " + str(score) + " points")
        print('NEW GAME')
        playGame()
      if(choice == 1):
        os.system('cls')
        print('+1!')
        score+=1
        newRound(score)
  if(choice == 1):
    print("LOOSER")
    print("VOTRE SCORE : " + str(score) + " points")
    print('NEW GAME')
    playGame()
  os.system('cls')
  print('+1!')
  score+=1
  W = open('Données/UsedWords.txt', "a", encoding='utf-8')
  W.writelines(word)
  W.writelines('\n')
  W.close()
  newRound(score)

  #CHOI#X NOUVEAU
  if(choice == 1):
    for UsedWord in UsedWords:
      if(word == UsedWord):
        print("LOOSER")
        print("Vous avez " + str(score) + " points")
        print('NEW GAME')
        playGame()
    score +=1
    W.write(word)
    W.write('\n')