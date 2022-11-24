#De random importer la fonction choice
#De os importer la fonction systeme
#Importer la fonction platfrom

#Initialiser Joueur egal -1
#Initialiser Ordi egal +1
#Initaliser les valeur PLATEAU [[0,0,0] [0,0,0] [0,0,0]]

# Définir la fonction evaluate pour parametre state
  # Si win pour parametre state, Ordi
    # incrementer score egal +1
  #Sinon si win (state,joueur)
    #incrementer score egal-1 
  #Sinon
    #incrementer score egal 0

#definir la fonction win (state,joueur)
  #La condition win-etat egal au nombre de victoire possible
  #Si Joueur,joueur, joueur est dans la condition win_etat
    #retourner la valeur True
  #sinon
    #retourner la valeur False

#Definir la fonction game_over de parametre état
  #retourner la valeur win(etat, JOUEUR) ou la valeur wins(etat, ORDI)

#Definir la fonction cellules_vides pour parametre état 
  #initialiser cellule egal []
  # 
    #Pour coordonéee x, ligne dans enumerate(etat):
      # Pour coordonéee y, cellule dans enumerate(ligne)
        # Si cellule verifie 0
          # ajouter la valeur cellule a x,y  
    

    #Retourner cellules

# definir la fonction valid_movement(x,y)
  # si coordonéee x,y est dans la cellule_vide(plateau)
    # retourer True
  # sinon
    # retourner False

# definir la fonction set_move(x,y, joueur)
  # si valid_movement(x,y)
    # PLATEAU(x,y) egal joueur
        # retourner la valeur True
  # sinon
    # retourner la valeur False

# definir la fonction minimax(etat,incr,joueur)
  # si joueur verifie ordi
    # best egal au valeur -1,-1, -float('inf')
  # sinon
    # best egal au valeur -1,-1,+float('inf')
  # si incr verifie 0 ou que game_over(etat)
    #coordonéee x,y egal cellule[0], cellule[1]
    #coordonéee etat[x][y] egal joueur
    #score egal minimax(etat, incr - 1, -joueur)
    #coordonéee etat[x][y] egal 0
    #score[0], score[1] egal x, y
  #si joueur verifie ordi
    #si score[2] est superieur a best[2]
      #best egal score
  #sinon
    #si score[2] est inferieur a best[2]
      #best egal score
  #retourner best

  #definir la fonction clean
      # os_name egal platform.system().lower()
      # si 'windows' est dans os_name:
      #   system('cls')
      # sinon
      #   system('clear')

# definir la fonction affiche(etat, o_choice, j_choice):
#    liste de caractere egal {
#         -1: j_choice,
#         +1: o_choice,
#         0: ' '
#     }
#     str_line egal '---------------'

#     afficher('\n' + str_line)
#     pour ligne est dans etat:
#         pour cell est dans ligne:
#             symbol egal chars[cell]
#             afficher(f'| {symbol} |', endegal'')
#         afficher('\n' + str_line)


# definir la fonction tour_ordi(o_choice, j_choice):

#     incr egal len(cellule_vide(PLATEAU))
#     si incr verifie 0 ou que game_over(PLATEAU):
#         returner

# efectuer la fonction clean()
#     afficher(f'Tour de ordinateur [{o_choice}]')
#     affiche(PLATEAU, o_choice, j_choice)

#     si incr  verifie  9
#       coordonée de x egal choice([0, 1, 2])
#       coordonée de y egal choice([0, 1, 2])
#     sinon
#         move egal minimax(PLATEAU, incr, ORDI)
#       coordonée de x, y egal move[0], move[1]

#     efectuer la fonction set_move(x, y, ORDI)

# definir la fonction tour_joueur(o_choice, j_choice):
#     incr egal len(cellule_vide(PLATEAU))
#     si incr  verifie  0 ou que game_over(PLATEAU):
#         returner

#     incrementer move egal -1
#     liste des moves egal {
#         1: [0, 0], 2: [0, 1], 3: [0, 2],
#         4: [1, 0], 5: [1, 1], 6: [1, 2],
#         7: [2, 0], 8: [2, 1], 9: [2, 2],
#     }

#     efectuer la fonction clean()
#     afficher(f'Tour joueur [{j_choice}]')
#     affiche(PLATEAU, o_choice, j_choice)

#     tant que move inferieur 1 ou que move superieur 9:
#         essaye:
#             move egal a init de l'input ('Utilisé le clavier numérique (1..9): '))
#             l'action coord egal moves[move]
#             l'action can_move egal set_move(coord[0], coord[1], JOUEUR)

#             si pas can_move:
#                 afficher('Mauvais mouvement')
#                 move egal -1
#         except (EOFError, KeyboardInterrupt):
#             afficher('Au revoir')
#             sorti()
#         except (KeyError, ValueError):
#             afficher('Mauvais choix')

#     si j_choice  verifie  'X':
#         appliquer o_choice egal 'O'
#     sinon
#         appliquer o_choice egal 'X'

#     efectuer clean()
#     tant que  first n'est pas egale a 'Y' et first n'est pas egale a 'N':
#         essaye:
#             first egal a l'input('Premier à jouer?[y/n]: ').upper()
#         except (EOFError, KeyboardInterrupt):
#             afficher('Au revoir')
#             exit()
#         except (KeyError, ValueError):
#             afficher('Mauvais choix')

#     tant que toute les valeur(cellule_vide(PLATEAU)) superieur a 0 et pas game_over(PLATEAU):
#         si first verifie  'N':
#             efectuer tour_ordi(o_choice, j_choice)
#             first egal ''

#         efectuer tour_joueur(o_choice, j_choice)
#         efectuer tour_ordi(o_choice, j_choice)

#     si wins(PLATEAU, JOUEUR):
#         efectuer clean()
#         afficher(f'Tour joueur [{j_choice}]')
#         affiche(PLATEAU, o_choice, j_choice)
#         afficher('GAGNER!')
#     elif wins(PLATEAU, ORDI):
#         efectuer clean()
#         afficher(f'Tour ordinateur [{o_choice}]')
#         affiche(PLATEAU, o_choice, j_choice)
#         afficher('PERDU!')
#     sinon
#         efectuer clean()
#         efectuer affiche(PLATEAU, o_choice, j_choice)
#         afficher('EGALITE!')

#     efectuer exit()

# efectuer main()