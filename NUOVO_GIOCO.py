import pygame
#inizio
pygame.init()
schermo = pygame.display.set_mode((1400,700))
#musica
pygame.mixer.music.load("musica_gioco.mp3")
pygame.mixer.music.play(-1)
#colori
rosso = (255,0,0)
blu = (0,0,255)
giallo = (255,255,0)
verde = (0,255,0)
bianco = (255,255,255)
nero = (0,0,0)
#entita
astronave = pygame.Rect(600,450,100,150)
nemico = pygame.Rect(530,80,80,150)
pulsante = pygame.Rect(600,500,240,60)
pul_inizio = pygame.Rect(500,300,300,150)
#immagini
nemico_ = pygame.image.load("nemico.png")
nemico_ = pygame.transform.scale(nemico_,(200,200))
astronave_ = pygame.image.load("astronave.png")#astronave
astronave_ = pygame.transform.scale(astronave_,(200,250))
missile = pygame.image.load("missile.png")#missile_
missile = pygame.transform.scale(missile,(50,100))
sfondo = pygame.image.load("sfondo_pianeti.png")
sfondo = pygame.transform.scale(sfondo,(1400,700))
laser = pygame.image.load("laser.png")
laser = pygame.transform.rotate(laser,-43)
laser = pygame.transform.scale(laser,(200,300))
#fisica
running = True
tasto = False
colore = verde
velocita = 8
velocita_n = 3
tempo = 4
toccato = False
destra = True
sinistra = False
mostra_evento = False
morto = False
gioco = False
toccato = False
Punteggio = 0
#ciclo principale
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                if not tasto:
                    suono_sparo = pygame.mixer.Sound("sparo.mp3")
                    suono_sparo.play()
                tasto = True
#tasti
    tasti = pygame.key.get_pressed() 
    if gioco and not morto:
        if tasti[pygame.K_d]:
            astronave.x += 1
            if astronave.x >= 1180:
                astronave.x -= 1
        if tasti[pygame.K_a]:
            astronave.x -= 1
            if astronave.x <= 50:
                astronave.x += 1
#condizioni
        if not tasto:
            missile_ = pygame.Rect(astronave.x,astronave.y + 50,100,150) 
        if tasto:
            missile_.y -= velocita
            velocita -= 0.02
            if velocita <= 0:
                tasto = False
                velocita = 8
                missile_.y = astronave.y + 50
            if not toccato:
                if missile_.colliderect(nemico):
                    Punteggio += 5
                    if astronave.x >= 530:
                        nemico = pygame.Rect(50,80,80,150)
                    else:
                        nemico = pygame.Rect(1180,80,80,150)
                    tasto = False
        if nemico.x >= 1200:
            sinistra = True
            destra = False
        if nemico.x <= 100:
            destra = True
            sinistra = False
        if destra:
            nemico.x += 1
        if sinistra:
            nemico.x -= 1
        if mostra_evento:
            if astronave.x <= nemico.x + 60 and astronave.x >= nemico.x - 60:
                suono_morte = pygame.mixer.Sound("suono_morte.mp3")
                suono_morte.play()
                morto = True
                Punteggio = 0
    if gioco and morto:
        if pulsante.collidepoint(pygame.mouse.get_pos()):
            if tasti[pygame.K_SPACE]:
                if astronave.x >= 300 and astronave.x <= 700:
                    nemico.x = 50
                else:
                    nemico.x = 530
                morto = False
                tasto = False
                toccato = False
#disegno
    if gioco and not morto:
        schermo.blit(sfondo,(0,0))
        schermo.blit(missile,(astronave.x + 70,missile_.y + 60))
        schermo.blit(astronave_,(astronave.x,astronave.y))
        if not toccato:
            tempo -= 0.01
            mostra_evento = True
            if tempo <= 0:
                tempo = 4
            if tempo >= 1.5:
                 mostra_evento = False
            if mostra_evento:
                schermo.blit(laser,(nemico.x + 2,nemico.y + 130))
            punteggio = pygame.font.Font(None,60)
            punteggio = punteggio.render("punteggio: " + str(Punteggio),True,bianco)
            schermo.blit(punteggio,(1050,50))
            schermo.blit(nemico_,(nemico.x,nemico.y))
    if gioco and morto:
        schermo.fill(nero)
        scritta_morte = pygame.font.Font(None,150)
        scritta_morte = scritta_morte.render("GAME OVER",True,blu)
        scritta_rigioca = pygame.font.Font(None,70)
        scritta_rigioca = scritta_rigioca.render("play again",True,colore)
        schermo.blit(scritta_rigioca,(600,500))
        schermo.blit(scritta_morte,(400,300))
        if pulsante.collidepoint(pygame.mouse.get_pos()):
            colore = bianco
        if not pulsante.collidepoint(pygame.mouse.get_pos()):
            colore = verde
    if not gioco:
        schermo.fill(nero)
        scritta_i = pygame.font.Font(None,130)
        titolo = pygame.font.Font(None,150)
        scritta_i = scritta_i.render("GIOCA",True,colore)
        titolo = titolo.render("SPACE WAR",True,blu)
        schermo.blit(scritta_i,(550,400))
        schermo.blit(titolo,(390,150))
        if pul_inizio.collidepoint(pygame.mouse.get_pos()):
            colore = bianco
        if not pul_inizio.collidepoint(pygame.mouse.get_pos()):
            colore = blu
        if pul_inizio.collidepoint(pygame.mouse.get_pos()) and tasti[pygame.K_SPACE]: 
            gioco = True
#fine
    pygame.display.update()
if gioco:
    if missile_.colliderect(nemico):
        nemico_ = pygame.image.load("nemico.png")
        nemico_ = pygame.transform.scale(nemico_,(200,200)) 
pygame.quit()
