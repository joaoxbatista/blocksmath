import pygame, sys

jogador = {}
jogador['energia'] = 100
jogador['pontos'] = 0
jogador['rect'] = pygame.Rect((5, 10), (20, 20))
jogador['blocos'] = 0
jogador['tempo'] = 0
jogador['next'] = False
limite_blocos = 0

mapa0 = [
	'x1111111111111111',
	'13222311111233121',
	'12113232430012211',
	'13320222110022331',
	'12333313320234311',
	'11111111111111111',
	]
mapa1 = [
	'x1111111111111111',
	'0323311111233121',
	'02114232430012211',
	'33320222110022331',
	'12333323320234311',
	'11111222111111111',
	]
mapa2 = [
	'x1110023202323002',
	'12223133333323323',
	'12113232430012211',
	'13321231222233311',
	'12333313320234333',
	'12223331312220010',
	]

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
 
def movePlayer(evento, nivel):

	xant, yant = jogador['rect'].left, jogador['rect'].top

	if evento.type == pygame.KEYDOWN:

		if evento.key == pygame.K_w:
			jogador['rect'].move_ip(0, -35)
			collideObjects(nivel)
			print "W"

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

def menu():
	pygame.init()
	jogador['next'] = False
	tela = pygame.display.set_mode((460, 420))
	pygame.display.set_caption("Blocks Math - Menu")
	relogio = pygame.time.Clock()
	fps = 25
	sair = False

	background = pygame.image.load('imgs/menu.jpg')

	while sair != True:

		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				pygame.quit()

			if evento.type == pygame.KEYDOWN:
		
				if evento.key == pygame.K_1:
					pygame.quit()
					nivel(mapa0, 40)
				if evento.key == pygame.K_2:
					nivel(mapa1, 30)
				if evento.key == pygame.K_3:
					nivel(mapa2, 25)
				if evento.key == pygame.K_4:
					pygame.quit()

		tela.blit(background, (0, 0))

		pygame.display.update()
		relogio.tick(fps)

def nivel(mapa1, limite):
	
	nivel1 = getObjects(mapa1)
	pygame.init()
	limite_blocos = limite

	largura, altura = (590, 350)
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption("Jogo 1")
	relogio = pygame.time.Clock()
	fps = 20
	sair = False

	backgroud = pygame.image.load('imgs/background.jpg')
	pygame.font.init()
	fonte = pygame.font.get_default_font()
	titulo = pygame.font.SysFont(fonte, 24)
	texto = pygame.font.SysFont(fonte, 16)
	h1_pontos = titulo.render("Blocos coletados: ", 1, (0, 255, 0))



	while sair != True:

		for evento in pygame.event.get():

			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				menu()

			movePlayer(evento, nivel1)
		
		 	if jogador['blocos'] > limite_blocos:
		 		jogador['blocos'] = 0
		 		jogador['rect'] = pygame.Rect((5, 10), (20, 20))
		 		endlevel('lose') 
		 		
	
		relogio.tick(fps)

		tela.fill((0,0,0))
		tela.blit(backgroud, (0,0))
		
		h1_energia = titulo.render("Energia: "+str(jogador['energia']), 1, (0, 255, 0))
		h1_blocos = titulo.render("Blocos restantes: "+str(limite_blocos - jogador['blocos']), 1, (0, 255, 0))
		h1_pontos = titulo.render("Pontos: "+str(jogador['pontos']), 1, (255, 255, 255))

		p_objetivo = texto.render("Colete os blocos verdes", 1, (255, 255, 255))
		p_obs = texto.render("E necessario ter 220 de energia", 1, (255, 255, 255))
		p_bazul = titulo.render("Bloco azul = +10", 1, (0, 0, 255))
		p_broxo = titulo.render("Bloco roxo = +5", 1, (255, 0, 255))
		p_bamarelo = titulo.render("Bloco amarelo = -5", 1, (255, 255, 0))
		p_bvermelho = titulo.render("Bloco vermelho = -10", 1, (255, 0, 0))

		tela.blit(h1_energia, (10, 240))
		tela.blit(h1_blocos, (200, 260))
		tela.blit(h1_pontos, (200, 240))

		tela.blit(p_objetivo, (10, 260))
		tela.blit(p_obs, (10, 275))
		tela.blit(p_bazul, (410, 240))
		tela.blit(p_broxo, (410, 260))
		tela.blit(p_bvermelho, (410, 280))
		tela.blit(p_bamarelo, (410, 300))

		printObjects(tela, nivel1)
		pygame.draw.rect(tela, (255, 255, 255), jogador['rect'])
		pygame.display.update()


def endlevel(result):

	pygame.init()

	largura, altura = 500, 500
	tela = pygame.display.set_mode((largura, altura))
	pygame.display.set_caption("Blocks Math - End Game")
	sair = False
	
	green, red, white = (50, 220, 50), (220, 50, 50), (255, 255, 255)
	color = 0
	text = ""

	fonte = pygame.font.get_default_font()
	h1 = pygame.font.SysFont(fonte, 30)
	
	while sair != True:

		for evento in pygame.event.get():

			if evento.type == pygame.QUIT:

				pygame.quit()
				menu()

		if result == "win":
			color = green
			text = "You Win"
		else:
			color = red
			text = "You Lose"

		tela.fill(color)
		texto = h1.render(text, 1, white)
		tela.blit(texto, (200, 240))
		pygame.display.update()	

menu()