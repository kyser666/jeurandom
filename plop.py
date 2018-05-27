import os, sys, pygame, time, random, decimal
from joueur import joueur
from missile import missile
from boum import boum
from os import path


screen = pygame.display.set_mode((907,662))


time.sleep(0.5)

dossier_missile=os.path.join(os.path.dirname(__file__), 'missileF')
dossier_perso=os.path.join(os.path.dirname(__file__), 'perso')
dossier_explosion=os.path.join(os.path.dirname(__file__), 'boum')
dossier_music=os.path.join(os.path.dirname(__file__), 'music')
image_joueur=(os.path.join(dossier_perso, '1d.gif'))

son_saut = (os.path.join(dossier_music, 'jump.wav'))



temps_score=0
joueur_spawnx=440
joueur_spawny=460
vitesse_joueur=7      #Pixels par frame
temp_spawn_missile=1.0
force_missile_depart=1.0
gravite_missile=0.6
gravite=0.3
intensite_saut=8
proba_missile=60
taille_texte=30

emplacement_texte_score_temps= (85,26)
couleur_texte_score=(0,0,128)
police_score='Flame on!.ttf'



direction=0
compt_gauche=0
compt_droite=0


j=joueur(joueur_spawnx,joueur_spawny,image_joueur)


image_missile='1.gif'

image_explo_inclusion='1.gif'            
image_explosion=(path.join(dossier_explosion, image_explo_inclusion ))


m0 = missile(force_missile_depart, image_missile)
m1 = missile(force_missile_depart, image_missile)
m2 = missile(force_missile_depart, image_missile)
m3 = missile(force_missile_depart, image_missile)
m4 = missile(force_missile_depart, image_missile)
m5 = missile(force_missile_depart, image_missile)
m6 = missile(force_missile_depart, image_missile)
m7 = missile(force_missile_depart, image_missile)
m8 = missile(force_missile_depart, image_missile)
m9 = missile(force_missile_depart, image_missile)


sprite_missile= pygame.sprite.Group()
sprites_joueur= pygame.sprite.Group()
sprites_joueur.add(j)


clock=pygame.time.Clock()

t0 = time.time() + (temp_spawn_missile*(1/10)) - temp_spawn_missile
t1 = time.time() + (temp_spawn_missile*(2/10))- temp_spawn_missile
t2 = time.time() + (temp_spawn_missile*(3/10)) - temp_spawn_missile
t3 = time.time() + (temp_spawn_missile*(4/10)) - temp_spawn_missile
t4 = time.time() + (temp_spawn_missile*(5/10)) - temp_spawn_missile
t5 = time.time() + (temp_spawn_missile*(6/10)) - temp_spawn_missile
t6 = time.time() + (temp_spawn_missile*(7/10)) - temp_spawn_missile
t7 = time.time() + (temp_spawn_missile*(8/10)) - temp_spawn_missile
t8 = time.time() + (temp_spawn_missile*(9/10)) - temp_spawn_missile
t9 = time.time() + (temp_spawn_missile)





pygame.init()

var_music  = random.randint(3, 3)

if var_music == 3:
    pygame.mixer.Sound(os.path.join(dossier_music, 'play.ogg')).play()
if var_music == 1:
    pygame.mixer.Sound(os.path.join(dossier_music, 'play2.ogg')).play()
if var_music == 2:
    pygame.mixer.Sound(os.path.join(dossier_music, 'play3.ogg')).play()





police_ecri=pygame.font.Font(police_score, taille_texte)

game = True
while game:
    temps = (time.time() + 1) - time.time()





    temps1=time.time()
    diff_temp=temps1-t0
    if diff_temp >= (temp_spawn_missile):
        m0 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m0)
        t0 = temps1
        
    temps2=time.time()
    diff_temp=temps2-t1
    if diff_temp >= (temp_spawn_missile):
        m1 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m1)
        t1 = temps2
    
    
    temps3=time.time()
    diff_temp=temps3-t2
    if diff_temp >= (temp_spawn_missile):
        m2 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m2)
        t2 = temps3
    
    
    temps4=time.time()
    diff_temp=temps4-t3
    if diff_temp >= (temp_spawn_missile):
        m3 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m3)
        t3 = temps4
    
    
    temps5=time.time()
    diff_temp=temps5-t4
    if diff_temp >= (temp_spawn_missile):
        m4 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m4)
        t4 = temps5
    
    
    temps6=time.time()
    diff_temp=temps6-t5
    if diff_temp >= (temp_spawn_missile):
        m5 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m5)
        t5 = temps6
    
    
    temps7=time.time()
    diff_temp=temps7-t6
    if diff_temp >= (temp_spawn_missile):
        m6 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m6)
        t6 = temps7
    
    
    temps8=time.time()
    diff_temp=temps8-t7
    if diff_temp >= (temp_spawn_missile):
        m7 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m7)
        t7 = temps8
    
    
    temps9=time.time()
    diff_temp=temps9-t8
    if diff_temp >= (temp_spawn_missile):
        m8 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m8)
        t8 = temps9
    
    
    temps10=time.time()
    diff_temp=temps10-t9
    if diff_temp >= (temp_spawn_missile):
        m9 = missile(force_missile_depart, image_missile)
        sprite_missile.add(m9)
        t9 = temps10
    
    
    
    key = pygame.key.get_pressed()
    touche_appuye = 0
    
    if key[pygame.K_a]:
        j.rect.move_ip(-vitesse_joueur, 0)
        compt_gauche += 1
        compt_droite = 0
        direction = -1
        touche_appuye = 1
        if 0<compt_gauche<=1:
            j.image = pygame.image.load((path.join(dossier_perso, '1g.gif')))
        if 1<=compt_gauche<=2:
            j.image = pygame.image.load((path.join(dossier_perso, '2g.gif')))
        if 2<=compt_gauche<=3:
            j.image = pygame.image.load((path.join(dossier_perso, '3g.gif')))
        if 3<=compt_gauche<=4:
            j.image = pygame.image.load((path.join(dossier_perso, '4g.gif')))
        if 4<=compt_gauche<=5:
            j.image = pygame.image.load((path.join(dossier_perso, '5g.gif')))
        if 5<=compt_gauche<=6:
            j.image = pygame.image.load((path.join(dossier_perso, '6g.gif')))
        if 6<=compt_gauche<=7:
            j.image = pygame.image.load((path.join(dossier_perso, '7g.gif')))
        if 7<=compt_gauche<=8:
            j.image = pygame.image.load((path.join(dossier_perso, '8g.gif')))
        if 8<=compt_gauche<=9:
            j.image = pygame.image.load((path.join(dossier_perso, '9g.gif')))
        if 9<=compt_gauche<=10:
            j.image = pygame.image.load((path.join(dossier_perso, '10g.gif')))
        if 10<=compt_gauche<=11:
            j.image = pygame.image.load((path.join(dossier_perso, '11g.gif')))
        if 11<=compt_gauche<=12:
            j.image = pygame.image.load((path.join(dossier_perso, '12g.gif')))
        if compt_gauche>12:
            compt_gauche = 0
    if touche_appuye == 0 and direction == -1:
        j.image = pygame.image.load((path.join(dossier_perso, '1g.gif')))
        
        
    
    if key[pygame.K_d]:
        j.rect.move_ip(vitesse_joueur, 0)
        compt_gauche = 0
        compt_droite += 1
        direction = 1
        touche_appuye = 1
        if 0<compt_droite<=1:
            j.image = pygame.image.load((path.join(dossier_perso, '1d.gif')))
        if 1<=compt_droite<=2:
            j.image = pygame.image.load((path.join(dossier_perso, '2d.gif')))
        if 2<=compt_droite<=3:
            j.image = pygame.image.load((path.join(dossier_perso, '3d.gif')))
        if 3<=compt_droite<=4:
            j.image = pygame.image.load((path.join(dossier_perso, '4d.gif')))
        if 4<=compt_droite<=5:
            j.image = pygame.image.load((path.join(dossier_perso, '5d.gif')))
        if 5<=compt_droite<=6:
            j.image = pygame.image.load((path.join(dossier_perso, '6d.gif')))
        if 6<=compt_droite<=7:
            j.image = pygame.image.load((path.join(dossier_perso, '7d.gif')))
        if 7<=compt_droite<=8:
            j.image = pygame.image.load((path.join(dossier_perso, '8d.gif')))
        if 8<=compt_droite<=9:
            j.image = pygame.image.load((path.join(dossier_perso, '9d.gif')))
        if 9<=compt_droite<=10:
            j.image = pygame.image.load((path.join(dossier_perso, '10d.gif')))
        if 10<=compt_droite<=11:
            j.image = pygame.image.load((path.join(dossier_perso, '11d.gif')))
        if 11<=compt_droite<=12:
            j.image = pygame.image.load((path.join(dossier_perso, '12d.gif')))
        if compt_droite>12:
            compt_droite = 0
    if touche_appuye == 0 and direction == 1:
        j.image = pygame.image.load((path.join(dossier_perso, '1d.gif')))
        
    if key[pygame.K_SPACE]:
        j.jump(intensite_saut, son_saut)
        
        
    sprites_joueur.update
    sprite_missile.update
    
    
    j.update(gravite)
    m1.update_missile(gravite_missile)
    m2.update_missile(gravite_missile)
    m3.update_missile(gravite_missile)
    m4.update_missile(gravite_missile)
    m5.update_missile(gravite_missile)
    m6.update_missile(gravite_missile)
    m7.update_missile(gravite_missile)
    m8.update_missile(gravite_missile)
    m9.update_missile(gravite_missile)
    
    
            
            
    
    if pygame.sprite.groupcollide(sprite_missile, sprites_joueur, False, True):
        boum()
        pygame.mixer.Sound(os.path.join(dossier_music, 'boom.wav')).play()
        game = False
        
        
        
    
    image_fond=pygame.image.load('bkgrd.GIF').convert()
    fond_rect=image_fond.get_rect()
    screen.blit(image_fond, fond_rect)
    
    
    sprites_joueur.draw(screen)
    sprite_missile.draw(screen)
    
    v=decimal.Decimal(temps)
    temps_arrondi=round(v, 2)
    
    score = police_score.render('YOUR TIME : ' + str(temps_arrondi), True, couleur_texte_score)
    screen.blit(score, emplacement_texte_score_temps )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)