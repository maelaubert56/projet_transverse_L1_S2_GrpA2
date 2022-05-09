# projet_transverse_L1_S2_GrpA2

### README du projet transverse:
- Maël AUBERT
- Marius Chevailler
- Nathan Bienvenu
- Sylvan Buhard
- Lucas Barthelemy
- Alon Debasc

### Touches :
- Entrer = faire spawn un joueur
- touches directionnelles = avances à gauche ou droite
- espace = sauter OU tirer
- X = sortir l'arme
- M = déclencher la mort subite
- clic = placer le joueur à l'endroit du clic (mode DEBUG)

### *Todo list :*

- système de puissance de tir
- explosions plus souffles
- si on saute de trop haut, on passe a travers le sol
- tjr un pb on peu se bloquer sur un angle si on touche avec la tete en avancant, pb de blocage en l'air et avec le jetpack aussi
- tjr un pb on peu se bloquer sur un angle si on touche avec la tete en avancant
- tjr un pb on peut se bloquer sur un angle si on touche avec la tete en avancant
- finir l'initialisation du jeu
- regrouper tous les états du player un une seule variable, qui contiendrai les états sous forme de chaine de caractère ("falling", "walking", "dead", "jumping","standing") afin de ne pas avoir 20 variables booléennes.
- si pas beaucoup d'armes, regrouper toutes les armes dans une barre (type minecraft) que l'on peut sélectionner avec les touches numériques (genre 10 cases numérotés de 1 à 10)
- faire le syteme de jeu tour par tour, avec 1 seul tir par arme
- teams et équipes à programmer en POO?
- améliorer les équipes avec une classe ou superclasse et avec if self.equipe!= equipe: collision=true
  - AJOUTER LA NOUVELLE ARME NAIN (grenade?)
- menu contextuel pur changer les armes
- prendre des persos de profil avec les 2 cotés?
- animation de déplacement/ de tir de saut etc
- menu de jeu
- bonus qui tombent sur la carte
####
idees ++
- multijoueur;
- terrain destructible


### Historique des updates  ###
* 21/01
  * 0.0.1
    * création du Git et ajout des 1ers fichiers vides


* 26/01
  * 0.0.2
    * ajout du fichier "DEFAULT.py" pour gérer les valeurs par défaut
    * update du README
    * ajout des images (ciel, logo, mer, île)
    * création de la fenêtre et affichage des 1ères images

  
* 27/01
  * 0.0.3
    * ajout d'un personnage dans le jeu (avec son fichier "player.py" et sa class associé)
    * ajout d'un fichier "game.py" qui gere la boucle de jeu et les évènements du jeu
    * chute du joueur lors de son apparition
    * detection des collisions entre le joueur et le terrain


* 28/01
  * 0.0.4
    * gestion des collisions pour empêcher la chute du joueur lorsqu'il touche le sol
    * création d'un fichier "object_background" et de sa class associée afin de gérer le terrain en tant que sprite (facilitant la gestion des collisions)
    * ajout d'une limitation du framerate pour améliorer les performances du jeu en empêcher les differences de vitesses selon la puissance du PC


* 29/01
  * 0.0.5
    * résolution d'un bug de collision (le terrain était déplacé visuellement de 50 px, mais pas son 'rect' ce qui est pris en compte pour la collision). Le terrain visuel est donc placé en x=0, y=0
    * ajout d'une variable 'DEBUG' pour afficher des elements visuels (collisions) et débloquer des fonctions utiles pour le debug du jeu
    * ajout de 2 images de terrains de test
    * modifications mineures (noms de variables/class/fonctions)
    * ajout d'une fonction 'start' activable avec la barre espace pour lancer le jeu (actuellement simplement faire spawn un joueur)


* 30/01
  * 0.0.6
    * ajout de la fonction de déplacement du joueur avec les touches directionnelles
    * ajout de 2 équipes dans lesquelles les joueurs sont répartis équitablement
    * ajout de la possibilité de changer de joueur (avec la touche C)
    * ajout de la 'mort subite' faisant monter la mer à grande vitesse (avec la touche M)
    * affichage de la vie des joueurs (sert également d'indicateur de selection du joueur)
  * 0.0.7
    * amélioration du déplacement des joueurs (qui glitch dans les murs)
    * amélioration de la clareté du code et des commentaires
  * 0.0.8
    * amélioration du déplacement des joueurs
    * modification des touches ('return' remplace 'space' pour faire apparaitre un personnage)
    * ajout d'un shuriken qui se déplace en ligne droite, sans gravité, lors de l'appui sur la touche 'space'
    * création d'un fichier 'weapon' afin d'accueillir la classe des armes et leurs caractéristiques.
    * le shuriken se détruit en sortant de la map
  * 0.0.9
    * le déplacement est maintenant fluide et sans bug.
    * résolution d'un bug de position du shuriken
  * 0.0.10
    * mise en transparent de l'arrière-plan du shuriken
    * le spawn du joueur se fait à des coordonnées randoms
    * le shuriken est détruit lors d'une collision avec le terrain
    * ajout de deux musiques dans les fichiers et de leur lancement dans le jeu


* 31/01
  * 0.0.11
    * la chute est maintenant accélérée selon la gravité terrestre (9.81 m/s² éventuellement adaptable pour rendre le jeu jouable)
    * début du développement de la fonction de jump (non fonctionnelle) utilisable avec la touche 'fleche haut'
  * 0.0.12
    * amélioration du jump afin qu'il s'arrête apres avoir touché le sol.
    * correction d'un bug qui bloquait le personnage en l'air s'il touchait un objet au-dessus de la moitié du rect du joueur 
  * 0.0.13
    * maintenant, pour switcher entre la fonction projectile et jump, on utilise la touche 'X'. les deux fonctions sont activables ensuite avec 'space'
    * ajout de la collision du shuriken et du joueur (le shuriken est détruit dans le cas échéant)
    * améliorations mineures (changement de noms, optimisation, commentaires)
  * 0.0.14
    * correction du bug de collision entre les différents sprites
    * ajout d'une image du joueur différente pour distinguer les 2 équipes


* 01/02
  * 0.0.15
    * correction d'un bug empêchant le switch des fonctions jump et projectile


* 02/02
  * 0.0.16
    * création du menu principal permettant uniquement de lancer le jeu pour le moment
    * ajout d'images pour représenter les boutons
    * création d'un fichier 'menu.py' accueillant une boucle similaire à 'game' pour gérer le menu
    * ajout d'évènements pour permettre de cliquer sur les boutons affichés et de se déplacer entre différents menus
  * 0.0.17
    * déplacement de la génération du jeu dans 'game' afin de pouvoir charger le menu avant de lancer le jeu
    * ajout d'un menu 'pause' en appuyant sur la touche 'escape'


* 05/02
  * 0.0.18
    * possibilité de skip le menu en mode DEBUG pour gagner du temps
    * résolution d'un bug de glitch advenant uniquement en mode DEBUG


* 09/02
  * 0.0.19
    * Ajout d'une fonction pour placer le joueur au clic en mode DEBUG
    * Ajout d'une fonction pour activer/désactiver le son de la musique depuis le menu du jeu
    * L'image du joueur est maintenant transparente
  * 0.0.20
    * développement du menu (nouvelles pages, icônes, fonctions)
    * ajout de boutons retour pour naviguer facilement de menu en menu
  * 0.0.21
    * résolution d'un bug lors du saut (le personnage se bloquait dans les murs plus hauts que lui)
    * ajout d'une fonction de jetpack au jeu (pas de visuel pour le moment) activable avec la touche 'J'
    * amélioration du menu
  * 0.0.22
    * ajout de nombreuses icônes pour le menu
    * bug de saut fixé
    * apparition d'un bug lors de sauts trop hauts : apres avoir acquis une certaine vitesse, le joueur traverse le terrain.
    * apparition d'un bug de collision entre les joueurs


* 11/02
  * 0.0.23
    * jetpack fonctionnel
    * saut réparé
    * collision entre les joueurs réparée


* 12/02
  * 0.0.24
    * Tous les bugs de collision sont réparés : les bugs venaient d'un décalage de 50 px de l'image faite au début pour des raisons esthétiques. le décalage avait été supprimé suite à des bugs, mais certaines fonctions le prenaient encore en compte.
    * ajout de deux images de terrain supplémentaire
    * ajout d'une musique dans les fichiers
    * modifications mineures (modification de noms, ajout de commentaires, optimisation)


* 13/02
  * 0.0.25
    * les joueurs perdent maintenant de la vie lorsqu'ils sont touchés par un shuriken
    * la vie s'affiche sur tous les joueurs en permanence
    * un indicateur indique quel joueur on contrôle
    * déplacement de quelques assets
    * autres modifs mineures (clareté du code)
    * ajout d'un historique de l'avancement du code dans le README

* 15/02
  * 0.0.26
    * ajout de la fonction pour la mort (transformation en tombe)
    * ajout de quelques images pour la mort et pour gérer plus tard les différentes animations (jetpack, chute, etc.)
    * la couleur du montant de la vie correspond à la couleur de l'équipe

* 16/02
  * 0.0.27
    * ajout d'un viseur qui change de sens selon la direction du joueur (s'affiche uniquement lorsque l'on sort l'arme)

* 19/02
  * 0.0.28
    * changement du nom du terrain qui s'appelait "background" par endroit (renommé en ground pour éviter la confusion entre ces deux éléments)
    * ajout d'une variable à Player (state) afin de regrouper les différentes variables d'état (is_falling, jumping, etc) en une seule qui contiendra la chaine de caractères correspondant à l'état actuel du player.

* 21/02
  * 0.0.29
    * avancement du changement des variables d'état vers une variable commune (affichée dans le terminal).
    * Bugs à régler :
      * ne passe pas à "aiming" lors du passage aux armes
      * La variable passe constamment a "falling", lors du déplacement et du vol en jetpack

* 28/02 
  * 0.0.30
    * tentative de réticule
  * 0.0.31
    * agencement et positionnement des boutons du jeu
  * 0.0.32
    * changement des variables d'état

* 15/03
  * 0.0.33
    * ajout d'une musique
    
* 18/03
  * 0.0.34
    * gestion de la mort d'un joueur (à la mort d'un joueur, on le déplace dans un groupe "dead_player" et on affiche une pierre tombale à la place
  * 0.0.35
    * gestion du game over, affichage des tombes dans l'eau

* 05/04
  * 0.0.36
    * trajectoire des projectiles ajoutée + explosions + viseur + rotation projectile en fonction de la vitesse.

* 09/05
  * 0.0.37
    * ajout d'images
  * 0.0.38
    * reset apres la fin du jeu, resolution des bugs lors de la navigation dans les menus
  * 0.0.39
    * Ajout des images dans le jeu + Game Over avec affichage de l'equipe gagnante
  * 0.0.40
    * ajout de boutons afin d'améliorer l'expérience.
    * optimisation du code
    * la mer est désormais bien reset