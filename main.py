#-*- coding: latin1 -*-
import pygame, sys, time

#PROPRIEDADE GLOBAIS DO JOGADOR
jogador = {}
jogador['energia'] = 100
jogador['pontos'] = 0
jogador['rect'] = pygame.Rect((5, 10), (20, 20))
jogador['blocos'] = 0
jogador['tempo'] = 0
jogador['next'] = False
jogador['level'] = 0
limite_blocos = 0

#MAPAS DO JOGO

mapas = [

	[
		'xx121333x12322201',
		'1x2223x111x2x3101',
		'1211323243001x211',
		'13320222x10022331',
		'1233x313320234311',
		'11x1x11x32x111111',
	],

	[
		'x111x322123111111',
		'03233x1114232121',
		'0211432x430012211',
		'333202221x0x22331',
		'12333123320x34311',
		'11141223231xx1111',
	],

	[
		'x11xxx23202323002',
		'1222xx33333323323',
		'1211x232430012211',
		'133212x1222233311',
		'123333xx320234333',
		'12223331312220010',
	],

	[
		'x11xxx23202323002',
		'1222xx33333323323',
		'1211x232430012211',
		'133212x1222233311',
		'123333xx320234333',
		'12223331312220010',
	],
]

#FUNÇAO QUE CONVERTE ARRAY EM BLOCOS E ADICIONA A LISTA
def getObjects(mapa):

	bvd = []
	bvm = []
	baz = []
	bam = []
	objetivo = []

	for x in range(len(mapa)):

		y = 0
		for objeto in mapa[x]:
			
			bloco = pygame.Rect(((y*35)+5, (x*35)+10), (20, 20))

			if objeto == '0':
				bvd.append(bloco)
			if objeto == '1':
				bvm.append(bloco)
			if objeto == '2':
				bam.append(bloco)
			if objeto == '3':
				baz.append(bloco)
			if objeto == '4':
				objetivo.append(bloco)

			y +=1
	return [bvd, bvm, baz, bam, objetivo]

#FUNÇAO QUE DESENHA OS BLOCOS NA TELA
def printObjects(tela, objetos):

	x = 0

	for objeto in objetos:

		#vermelho
		if x == 0:
			for bloco in objeto:
				pygame.draw.rect(tela, (255, 0, 0), bloco) 
		#amarelo
		if x == 1:
			for bloco in objeto:
				pygame.draw.rect(tela, (255, 255, 0), bloco) 
		#azul
		if x == 2:
			for bloco in objeto:
				pygame.draw.rect(tela, (0, 0, 255), bloco) 
		#roxo
		if x == 3:
			for bloco in objeto:
				pygame.draw.rect(tela, (255, 0, 255), bloco) 

		if x == 4:
			for bloco in objeto:
				pygame.draw.rect(tela, (0, 255, 0), bloco) 

		x += 1 

#FUNÇAO QUE VERIFICA COLISAO
def collideObjects(objetos):

	pygame.mixer.init()
	energiaup = pygame.mixer.Sound('sounds/energiup.ogg')
	energiadown = pygame.mixer.Sound('sounds/energidown.ogg')
	pointup = pygame.mixer.Sound('sounds/pointup.ogg')
	x = 0

	for objeto in objetos:

		if x == 0:
			for bloco in objeto:
				if jogador['rect'].colliderect(bloco):
					energiadown.play()
					jogador['energia'] -= 10
					jogador['blocos'] += 1
					objeto.remove(bloco)

		elif x == 1:
			for bloco in objeto:
				if jogador['rect'].colliderect(bloco):
					energiadown.play()
					jogador['energia'] -= 5
					jogador['blocos'] += 1
					objeto.remove(bloco)
		elif x == 2:
			for bloco in objeto:
				if jogador['rect'].colliderect(bloco):
					energiaup.play()
					jogador['energia'] += 10
					jogador['blocos'] += 1
					objeto.remove(bloco)
		elif x == 3:
			for bloco in objeto:
				if jogador['rect'].colliderect(bloco): 
					energiaup.play()
					jogador['energia'] += 5
					jogador['blocos'] += 1
					objeto.remove(bloco)
		elif x == 4:
		 	for bloco in objeto:
		 		if jogador['rect'].colliderect(bloco) and jogador['energia'] == 220:
		 			pointup.play()
		 			objeto.remove(bloco)
		 			jogador['energia'] -= 50
		 			jogador['pontos'] += 1

 		 		
 		 	if len(objeto) == 0:
 				jogador['rect'] = pygame.Rect((5, 10), (20, 20))
 				jogador['blocos']
 		 		endlevel('win')

		x += 1

#FUNÇAO DE MOVIMENTAÇAO DO JOGADOR
def movePlayer(evento, nivel):

	xant, yant = jogador['rect'].left, jogador['rect'].top

	if evento.type == pygame.KEYDOWN:

		if evento.key == pygame.K_w:
			jogador['rect'].move_ip(0, -35)
			collideObjects(nivel)

		if evento.key == pygame.K_s:
			jogador['rect'].move_ip(0, 35)
			collideObjects(nivel)

		if evento.key == pygame.K_d:
			jogador['rect'].move_ip(35, 0)
			collideObjects(nivel)

		if evento.key == pygame.K_a:
			jogador['rect'].move_ip(-35, 0)
			collideObjects(nivel)

	if jogador['rect'].left < 0 or jogador['rect'].left > 590:
		jogador['rect'].left = xant
	if jogador['rect'].top < 0 or jogador['rect'].top > 200:
		jogador['rect'].top = yant

#FUNÇAO QUE DESENHA A TELA DO MENU
def menu():
	pygame.init()
	jogador['next'] = False
	tela = pygame.display.set_mode((460, 420))
	pygame.display.set_caption("Blocks Math - Menu")
	relogio = pygame.time.Clock()
	fps = 25
	sair = False
	
	background = pygame.image.load('imgs/menu.jpg')
	
	opc = 0

	while sair != True:
		
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()

			if evento.type == pygame.KEYDOWN:
		
				if evento.key == pygame.K_1:
					opc = 1
					sair = True
				if evento.key == pygame.K_2:
					opc = 2
					sair = True
				if evento.key == pygame.K_3:
					opc = 3
					sair = True
				if evento.key == pygame.K_4:
					sair = True

		tela.blit(background, (0, 0))
		pygame.display.update()
		relogio.tick(fps)

	pygame.quit()
	nivel(mapas, opc)


#FUNCAO DESENHA A TELA DO NIVEL
def nivel(mapas, dificuldade):
	
	if dificuldade == 1:
		limite_blocos = 40
		tempo_limite = 60
		title = "Blocks Math - Dificuldade: Fácil"

	elif dificuldade == 2:
		limite_blocos = 35
		tempo_limite = 50
		title = "Blocks Math - Dificuldade: Médio"

	elif dificuldade == 3:
		limite_blocos = 35
		tempo_limite = 40
		title = "Blocks Math - Dificuldade: Difícil"
	
	print jogador['level']
	mapa = getObjects(mapas[jogador['level']])
	pygame.init()
	
	largura, altura = (590, 350)
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption(title)
	
	fps = 20
	sair = False

	relogio = pygame.time.Clock()
	t0 = int(time.time())

	backgroud = pygame.image.load('imgs/background2.png')
	textura = pygame.image.load('imgs/glass.png')

	pygame.font.init()
	fonte = pygame.font.get_default_font()
	titulo = pygame.font.SysFont(fonte, 16)
	texto = pygame.font.SysFont(fonte, 16)
	h1_pontos = titulo.render("Blocos coletados: ", 1, (0, 255, 0))

	while sair != True:

		for evento in pygame.event.get():

			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				menu()

			movePlayer(evento, mapa)

		
		
		t1 = int(time.time())
		dt = t1 - t0
		tr = tempo_limite - dt
		
	 	if (jogador['blocos'] > limite_blocos or tr <= 0):
	 		jogador['blocos'] = 0
	 		jogador['rect'] = pygame.Rect((5, 10), (20, 20))
	 		endlevel('lose') 
		 		
	
		relogio.tick(fps)

		tela.fill((0,0,0))
		
		
		h1_energia = titulo.render(str(jogador['energia']), 1, (30, 30, 30))
		h1_blocos = titulo.render(str(limite_blocos - jogador['blocos']), 1, (30, 30, 30))
		h1_pontos = titulo.render(str(jogador['pontos']), 1, (30, 30, 30))
		h1_tempo = titulo.render(str(tr), 1, (30, 30, 30))

		printObjects(tela, mapa)
		pygame.draw.rect(tela, (255, 255, 255), jogador['rect'])

		tela.blit(backgroud, (0,0))
		tela.blit(h1_energia, (314, 270))
		tela.blit(h1_tempo, (314, 316))
		tela.blit(h1_blocos, (232, 316))
		tela.blit(h1_pontos, (232, 270))
		tela.blit(textura, (5,10))

		pygame.display.update()

#FUNCAO QUE DESENHA A TELA DE RESULTADO
def endlevel(result):

	pygame.init()

	largura, altura = 500, 500
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption("Blocks Math - End Level")
	sair = False
	
	green, red, white = (50, 220, 50), (220, 50, 50), (255, 255, 255)
	color = 0
	text = ""

	fonte = pygame.font.get_default_font()
	h1 = pygame.font.SysFont(fonte, 30)
	
	if result == "win":
		jogador['level'] +=1
	elif result == "lose":
		jogador['level'] +=0	

	while sair != True:

		for evento in pygame.event.get():

			if evento.type == pygame.QUIT:

				sair = True
				menu()

		if result == "win":
			color = green
			text = "You Win"
			
		elif result == "lose":
			color = red
			text = "You Lose"

 		jogador['blocos'] = 0

		tela.fill(color)
		texto = h1.render(text, 1, white)
		tela.blit(texto, (200, 240))
		pygame.display.update()	

	pygame.quit()
menu()