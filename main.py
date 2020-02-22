'''
Jeu Réalisé Par Yamis MANFALOTI / KreeZe
'''

"""
Librairies
"""
import time
import pygame
from random import*


"""
Initialisation pygame + paramètre
"""
hauteur = 14
largeur = 12
TITLE_SIZE = 48
pygame.init()
fenetre = pygame.display.set_mode(((largeur+5)*TITLE_SIZE, (hauteur+1)*TITLE_SIZE)) #816 par 720
pygame.display.set_caption("Dungeon Fighter")
font = pygame.font.SysFont('Impact', 25)
font2 = pygame.font.SysFont('Impact', 20)

"""
Fonction Main
"""

def main():

    """
    Initialisation Variable Main
    """
    frequence = pygame.time.Clock()
    loop = True
    tiles = []
    numeroTile = ''
    NB_TILES = 40
    hauteur = 14
    largeur = 12
    TITLE_SIZE = 48
    joueurX = 1
    joueurY = 2
    posX = ''
    posY = ''
    bas = 2
    droite = 1
    player = 12
    coffre = 0
    attaque = 0
    countTemps1 = 0
    countTemps2 = 0
    countTemps3 = 0
    countTemps4 = 0
    vieJoueur = 100
    VieMob = 100
    yMob1 = 3
    yMob2 = 6
    yBoss = 9
    VieDepart = 100
    direction = ''
    timing = 0
    SpeedAction = 20
    prochainne = ''
    choix = ''
    lvl = 0
    difficulte = [
        [100,20,32,33],   #lvl 0       2 monstre
        [150,20,38],   #lvl 1       1 boss
        [100,18,35,36],   #lvl 2       2 monstre
        [150,18,39],   #lvl 3       1 boss
        [100,16,33,34],   #lvl 4       2 monstre
        [150,16,38],   #lvl 5       1 boss
        [100,14,36,37],   #lvl 6       2 monstre
        [150,14,39],   #lvl 7       1 boss
        [100,12,32,33],   #lvl 8       2 monstre
        [150,12,38],   #lvl 9       1 boss
        [100,10,35,36],   #lvl 10      2 monstre
        [150,10,39],  #lvl Final    1 boss Final
        [  0, 0] ] #lvl inexistante empeche out of index
    NbMob = 2
    Boss = 3
    combat = 0
    imageMob = 0

    """
    Map + Id Des Tiles
    """
    niveauVierge = [
    [8 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,9 ],
    [1 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,7 ,7 ,7 ,7 ,7 ,0 ,7 ,7 ,7 ,7 ,2 ],
    [1 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,4 ,2 ],
    [10,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,11] ]


    """
    Differente Fonctions
    """

    def chargetiles(tiles): #fonction permettant de charger les images tiles dans une liste tiles[]
        for n in range(0,NB_TILES):
            tiles.append(pygame.image.load('data/'+str(n)+'.png'))

    def afficheNiveau(niveau): #affiche le niveau a partir de la liste a deux dimensions niveau[][]
        for y in range(hauteur):
            for x in range(largeur):
                fenetre.blit(tiles[niveau[y][x]],(x*TITLE_SIZE+100,y*TITLE_SIZE))

    def AfficheJoueur(numero):
        fenetre.blit(tiles[numero],(joueurX * TITLE_SIZE+100,joueurY * TITLE_SIZE-5))

    def cooldown(CooldownEnSec):
        start = time.time()
        end = 0
        while end <= CooldownEnSec :
            end = time.time() - start
        return 'passed'

    def GameOver():
        ImageGameOver = pygame.image.load('data/GameOver.png')
        fenetre.fill((0,0,0))
        fenetre.blit(ImageGameOver,(0,0))

    def Victoire():
        ImageVictoire = pygame.image.load('data/Victoire.png')
        fenetre.fill((0,0,0))
        fenetre.blit(ImageVictoire,(0,0))

    def text(texte,police,msg,x,y):
            texte = police.render(msg, True, (0, 128, 0))
            fenetre.blit(texte ,(x,y))
            if police == font:
                texte = police.render(msg, True, (0, 0, 0))
                fenetre.blit(texte ,(x,y))

    def AfficheMob(mob,x,y):
        fenetre.blit(tiles[mob],(x * TITLE_SIZE+100,y * TITLE_SIZE-5))

    """
    Boucle Jeu
    """
    while loop==True:
        niveauVierge[11][6] = 0
        FinAffichage = 0
        """
        Detection touche
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = False
                elif event.key == pygame.K_UP:
                    direction = 'haut'
                elif event.key == pygame.K_DOWN:
                    direction = 'bas'
                elif event.key == pygame.K_RIGHT:
                    direction = 'droite'
                elif event.key == pygame.K_LEFT:
                    direction = 'gauche'
                elif event.key == pygame.K_RETURN:
                    FinAffichage = 1

        """
        Fonction Dirrection/Déplacement/Animation

        """

        if direction == 'droite':
            start2 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start2
            countTemps1 += 0.5

            if droite+1 >= 11:
                print("déplacement impossible")
                countTemps1 = 0
                direction = ''
                joueurX = 10
                droite = 10
            elif countTemps1 >= 0.5 and countTemps1 <= 1:
                player = 12
                joueurX += 0.25
                posY = joueurY
            elif countTemps1 >= 1 and countTemps1 <= 1.5:
                player = 13
                joueurX += 0.25
                posY = joueurY
            elif countTemps1 >= 1.5 and countTemps1 <= 1.9:
                player = 14
                joueurX += 0.25
                posY = joueurY
            elif countTemps1 >= 2 and countTemps1 <= 2.1:
                player = 15
                joueurX += 0.25
                posY = joueurY
                countTemps1 = 0
                direction =''
                droite += 1
                joueurX = int(joueurX)

            if posY != joueurY:
                countTemps1 = 0
                direction =''
                joueurX = int(joueurX)


        if direction == 'gauche':
            start4 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start4
            countTemps2 += 0.5

            if droite-1 <= 0:
                print("déplacement impossible")
                countTemps2 = 0
                direction = ''
                joueurX = 1
                droite = 1
            elif countTemps2 >= 0.5 and countTemps2 <= 1:
                player = 16
                joueurX -= 0.25
                posY = joueurY
            elif countTemps2 >= 1 and countTemps2 <= 1.5:
                player = 17
                joueurX -= 0.25
                posY = joueurY
            elif countTemps2 >= 1.5 and countTemps2 <= 1.9:
                player = 18
                joueurX -= 0.25
                posY = joueurY
            elif countTemps2 >= 2 and countTemps2 <= 2.1:
                player = 19
                joueurX -= 0.25
                posY = joueurY
                countTemps2 = 0
                direction =''
                joueurX = int(joueurX)
                droite -= 1

            if posY != joueurY:
                countTemps2 = 0
                direction =''
                joueurX = int(joueurX)

        if direction == 'haut':
            start3 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start3
            countTemps3 += 0.5

            if bas-1 <= 1:
                print("déplacement impossible")
                countTemps3 = 0
                direction = ''
                bas = 2
                joueurY = 2
            elif countTemps3 >= 0.5 and countTemps3 <= 1:
                player = 20
                joueurY -= 0.25
                posX = joueurX
            elif countTemps3 >= 1 and countTemps3 <= 1.5:
                player = 21
                joueurY -= 0.25
                posX = joueurX
            elif countTemps3 >= 1.5 and countTemps3 <= 1.9:
                player = 22
                joueurY -= 0.25
                posX = joueurX
            elif countTemps3 >= 2 and countTemps3 <= 2.1:
                player = 23
                joueurY -= 0.25
                posX = joueurX
                countTemps3 = 0
                direction =''
                joueurY = int(joueurY)
                bas -= 1

            if posX != joueurX:
                countTemps3 = 0
                direction = ''
                joueurY = int(joueurY)

        if direction == 'bas':
            start3 = time.time()
            end = 0
            while end <= 0.033 :
                end = time.time() - start3
            countTemps4 += 0.5

            if bas+1 == 13:
                print("déplacement impossible")
                countTemps4 = 0
                direction = ''
                bas = 12
                joueurY = 12
            elif countTemps4 >= 0.5 and countTemps4 <= 1:
                player = 24
                joueurY += 0.25
                posX = joueurX
            elif countTemps4 >= 1 and countTemps4 <= 1.5:
                player = 25
                joueurY += 0.25
                posX = joueurX
            elif countTemps4 >= 1.5 and countTemps4 <= 1.9:
                player = 26
                joueurY += 0.25
                posX = joueurX
            elif countTemps4 >= 2 and countTemps4 <= 2.1:
                player = 27
                joueurY += 0.25
                posX = joueurX
                countTemps4 = 0
                direction =''
                joueurY = int(joueurY)
                bas += 1

            if posX != joueurX:
                countTemps4 = 0
                direction = ''
                joueurY = int(joueurY)


        """
        Fonction Zone De Combat
        """

        if combat == 1:
            direction = 'nul'
            chgmt = 0
            fleche = pygame.image.load('data/fleche.png')
            fleche1 = pygame.image.load('data/fleche1.png')
            fleche2 = pygame.image.load('data/fleche2.png')
            fleche3 = pygame.image.load('data/fleche3.png')
            fleche4 = pygame.image.load('data/fleche4.png')
            VoyantChgmt = pygame.image.load('data/VoyantChgmt.png')
            VoyantChgmt = VoyantChgmt.convert_alpha()
            VoyantChgmtVert = pygame.image.load('data/VoyantChgmtVert.png')
            VoyantChgmtVert = VoyantChgmtVert.convert_alpha()
            ImageFleche = fleche
            VieDepart = VieMob

            while VieMob > 0 and vieJoueur != 0:
                Voyant = 0
                """
                Initialisation Varialble Zone De Combat
                """
                direction = 'nul'
                chgmt = 0
                fenetre.fill((0,0,0))
                niveauVierge[11][6] = 7
                afficheNiveau(niveauVierge)

                """
                Clock + Detection Touche 30 FPS
                """
                if cooldown(0.033) == 'passed':
                    timing += 1

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                        VieMob = 0
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            loop = False
                            VieMob = 0
                        elif event.key == pygame.K_UP:
                            direction = 'haut'
                            chgmt = 1
                        elif event.key == pygame.K_DOWN:
                            direction = 'bas'
                            chgmt = 1
                        elif event.key == pygame.K_RIGHT:
                            direction = 'droite'
                            chgmt = 1
                        elif event.key == pygame.K_LEFT:
                            direction = 'gauche'
                            chgmt = 1
                """
                Choix Action A Faire Pour Attaquer (Random)
                """
                if timing == SpeedAction:
                    choix = randint(0,3)
                    if choix == 0:
                        prochainne = 'haut'
                    elif choix == 1:
                        prochainne = 'bas'
                    elif choix == 2:
                        prochainne = 'droite'
                    elif choix == 3:
                        prochainne = 'gauche'
                    Voyant = 1
                    timing = 0

                """
                Detection Bonne Action
                """
                if direction == prochainne:
                    VieMob -= 20
                    direction = ''
                elif direction != prochainne and chgmt == 1:
                    vieJoueur -= 20

                if prochainne == 'gauche':
                    ImageFleche = fleche1
                elif prochainne == 'haut':
                    ImageFleche = fleche2
                elif prochainne == 'bas':
                    ImageFleche = fleche3
                elif prochainne == 'droite':
                    ImageFleche = fleche4

                """
                Affichage Text Vie Mob/Joueur
                """

                text('textVieMob',font,"Vie Du Monstre: "+str(VieMob)+"/"+str(VieDepart),3*TITLE_SIZE+120,11*TITLE_SIZE-36)
                text('textVieJoueur',font,"Vie Du Hero: "+str(vieJoueur)+"/ 100",3*TITLE_SIZE+120,11*TITLE_SIZE-60)
                text('strLvl',font,"Lvl : "+str(lvl),5*TITLE_SIZE+120,11*TITLE_SIZE-85)

                """
                Mise En Marche Du Voyant Vert Quand Changement De Prochaine
                """
                if Voyant == 0:
                    fenetre.blit(VoyantChgmt,(9*TITLE_SIZE+100+12,11*TITLE_SIZE))
                elif Voyant == 1:
                    fenetre.blit(VoyantChgmtVert,(9*TITLE_SIZE+100+12,11*TITLE_SIZE))

                """
                Affichage Des Fleches + De Leur Activation + Mob/Boss
                """
                fenetre.blit(ImageFleche,(3*TITLE_SIZE+100,11*TITLE_SIZE))
                fenetre.blit(mob,(7*TITLE_SIZE,3*TITLE_SIZE))

                pygame.display.update()

            """
            Augmentation du lvl si on a tué le boss
            """
            if vieJoueur != 0:
                Boss -= 1
                NbMob -= 1

            """
            Evite de relancer direct le combat
            """
            joueurY += 1
            combat = 0

        """
        Definition du degrés de dificulté en fonction du lvl et si c'est un boss ou pas
        """
        VieMob = difficulte[lvl][0]
        SpeedAction = difficulte[lvl][1]
        if NbMob == 0:
            lvl += 1
            NbMob = 2
        if Boss == 1:
                VieMob = 200
        if Boss == 0:
            lvl += 1
            Boss = 3
            NbMob = 2


        """
        Appel Des Différentes Fonctions
        """

        fenetre.fill((0,0,0))
        chargetiles(tiles)
        afficheNiveau(niveauVierge)
        AfficheJoueur(player)
        if Boss != 1 :
            AfficheMob(difficulte[lvl][2],1,3)
        else:
            AfficheMob(difficulte[lvl-1][2],1,3)

        if Boss != 1 :
            AfficheMob(difficulte[lvl][3],1,6)
        else:
            AfficheMob(difficulte[lvl-1][3],1,6)

        if Boss != 1 :
            AfficheMob(difficulte[lvl+1][2],1,9)
        elif Boss == 1:
            AfficheMob(difficulte[lvl][2],1,9)



        coffre = 0
        print(droite)
        print(bas)

        """
        Affichage Différent Textes
        """
        text('strVieJoueur',font2,"Vie Du Hero: ",11.5*TITLE_SIZE+120,1*TITLE_SIZE)
        text('strVieJoueur2',font2,str(vieJoueur)+"/ 100",11.5*TITLE_SIZE+120,1*TITLE_SIZE+25)
        text('strLvl',font2,"Lvl : "+str(lvl),11.5*TITLE_SIZE+120,2.5*TITLE_SIZE)

        """
        Detection Combat
        """
        if joueurY == yMob1:
            combat = 1
            yMob1 = 0
            imageMob = difficulte[lvl][2]
        if joueurY == yMob2:
            combat = 1
            yMob2 = 0
            imageMob = difficulte[lvl][3]
        if joueurY == yBoss:
            combat = 1
            yBoss = 0
            imageMob = difficulte[lvl][2]

        """
        Definition mob à afficher
        """


        mob = tiles[imageMob].convert_alpha()

        """
        Detection mort Boss Final + fin du jeu
        """

        numeroTile = niveauVierge[int(joueurY)][int(joueurX)]
        if numeroTile == 0 and lvl == 10:
            Victoire()
            if FinAffichage == 1:
                loop = False


        """
        Fonction detection coffre
        """

        numeroTile = niveauVierge[int(joueurY)][int(joueurX)]
        if numeroTile == 0 and lvl != 10:
            print("vous êtes sur le coffre")
            yMob1 = 3
            yMob2 = 6
            yBoss = 9
            droite = 1
            bas = 2
            coffre = 1
            joueurX,joueurY = 1,2

        """
        Detecte Game Over
        """

        if vieJoueur <= 0:
            GameOver()
            if FinAffichage == 1:
                loop = False

        if joueurX < 1:
            joueurX = 1
        elif joueurX > 10:
            joueurX = 10

        if joueurY < 2:
            joueurY = 2
        elif joueurY > 12:
            joueurY = 12

        """
        Actualisation fenetre graphique
        """
        pygame.display.update()


"""
Menu Du Jeux
"""
def menu():
    menu0 = pygame.image.load('data/menu0.png')
    menu1 = pygame.image.load('data/menu1.png')
    touches = pygame.image.load('data/touches.png')
    continuer = True
    continuer2 = True
    choix = 0
    entrer = 0
    while continuer != False:
        fenetre.blit(touches,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                elif event.key == pygame.K_RETURN:
                    continuer = False
        pygame.display.update()
    while continuer2 != False:
        entrer = 0
        if choix == 0:
            fenetre.blit(menu0,(0,0))
        elif choix == 1:
            fenetre.blit(menu1,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer2 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer2 = False
                elif event.key == pygame.K_UP:
                    choix = (choix-1)%2
                elif event.key == pygame.K_DOWN:
                    choix = (choix+1)%2
                elif event.key == pygame.K_RETURN:
                    entrer = 1

        if entrer == 1 and choix == 0:
            main()
        elif entrer == 1 and choix == 1:
            continuer2 = False
        pygame.display.update()

    pygame.quit()






"""
Execution
"""
menu()