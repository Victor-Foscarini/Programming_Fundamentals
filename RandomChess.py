#Victor Foscarini Almeida

#em todo o código foi utilizada uma estutura de árvore de decisão que checa sempre em uma função verifica() quais são as possibilidades de ação da peça, seja para capturar outra peça ou se mover e salva todos os seus possíveis movimentos, além de salvar no geral o que acontece no jogo e os seus dessenrolares
#outras estruturas e árvores de decisão menores também foram utilizadas no código para realizar captura e movimento de peças, além de loops para imprimir o tabuleiro e as suas mudanças utilizando o pygame
#a biblioteca pygame foi utilizada para ter uma visão do tabuleiro e é impresso em verde-escuro os possíveis movimentos de andar com captura e em verde-claro os possíveis movimentos de andar sem captura
#no início do código estão escritas as classes, uma com relação  à peça e outra com relação ao tabuleiro e no final é realizado o loop principal do jogo
#note que foi utilizado um tabuleiro(matriz 8x8) que contém uma classe peça em cada posição da matriz com informação relacionada à peça/ausência de peça no local do tabuleiro

#OBS: caso o código esteja travando, recomendo a mudança do fps/taxa de resposta do pygame no final do código(possivelmente linha 445) de 30 para outro número menor
"""
#no caso, a preferência está no lado esquerdo da árvore abaixo
#lógica semelhante ao metódo in-order traversal

								   peça
								/        \
							pode mover	não pode mover
							/        \
						  comer     andar

#no caso, mostra as possibilidades do dessenrolar e fim de jogo

								 jogo
				   /                                 \
		uma cor pode mover              ambas as cores podem mover
		      /      \                     /              \
	vez da outra   vez dela    20 jogadas de mov. dama   mov. peça    
		  |					            |
	fim de jogo                    fim de jogo




"""


import pygame
from pygame.locals import *
import random


pygame.init()

#valores constantes de formato e as cores utilizados no pygame

largura = 640
altura = 640

lado = largura/8

preto = (0,0,0)
branco = (255,255,255)
marrom = (100,40,0)
cinza = (120,120,120)
verde_escuro = (0,120,0)
verde_claro = (0,255,0)
vermelho_escuro = (200,0,0)
vermelho_claro = (255,0,0)
cor_tabuleiro = (0,31,0)


#display

display = pygame.display.set_mode((largura,altura))
pygame.font.init()
clock = pygame.time.Clock()

class peca:
	def __init__(self,tipo=None,cor='..',podeComer=False):
		self.tipo = tipo 
		self.cor = cor #0 para branca e 1 para preta
		self.podeComer = podeComer
		self.naMira = [] #ficam salvas as pecas possiveis de ser comidas	
		self.podeAndar = [] #ficam salvas as posições para quais a peça pode mover sem comer(andar)
		self.podeCapturar = [] #ficam salvas as posições que a peça pode se mover ao capturar

class Damas:
	def __init__(self,tabuleiro=None):
		#matrizes que contêm a localização de todas as peças do jogo
		if tabuleiro==None:
			self.tabuleiro = self.criaTabuleiro()
		else:
			self.tabuleiro = tabuleiro
		self.Njogadas = 0 #calcula o numero de jogadas de damas para checar fim da partida
		self.podeComerPB = [False,False] #guarda em 0 se o branco pode comer e em 1 se o preto pode comer
		self.podeJogar = [True,True] #guarda quem pode jogar
		self.ultimaJogada = 1 #guarda a cor de quem realizou a última jogada, o jogo começa com o branco
		#guarda-se todas as peças que podem comer ou andar
		self.podemCapturar = [[],[]]
		self.podemAndar = [[],[]]

	def criaTabuleiro(self):
		tabuleiro = [[peca() for i in range(8)]for i in range(8)]
		#cria uma matriz 8x8 com as peças pretas e brancas nos seus devidos lugares
		#as peças brancas começam na parte de cima do tabuleiro(linhas 0,1,2) e as pretas na parte de baixo(linhas 5,6,7)
		for i in range(3):
			for j in range(8):
				if (i==0 or i==2) and (j%2==1) :
					tabuleiro[i][j].tipo = 'pedra'
					tabuleiro[i][j].cor = 1
				elif (i==1) and (j%2==0):
					tabuleiro[i][j].tipo = 'pedra'
					tabuleiro[i][j].cor = 1
		for i in range(5,8):
			for j in range(8):
				if (i==5 or i==7) and (j%2==0):
					tabuleiro[i][j].tipo = 'pedra'
					tabuleiro[i][j].cor = 0
				elif (i==6) and (j%2==1):
					tabuleiro[i][j].tipo = 'pedra'
					tabuleiro[i][j].cor = 0		

		return tabuleiro
	
	def imprimeTabuleiro(self):
		for i in range(8):
			for j in range(8):
				if self.tabuleiro[i][j].cor == 1:
					if self.tabuleiro[i][j].tipo == 'pedra':
						pygame.draw.circle(display,marrom,(int(j*lado+lado/2),int(i*lado+lado/2)),int(lado/2))
					elif self.tabuleiro[i][j].tipo == 'dama':
						pygame.draw.polygon(display,marrom,[(int(j*lado),int((i+0.5)*lado)),(int((j+1)*lado),int((i+0.5)*lado)),(int((j+0.5)*lado),int(i*lado)),(int((j+0.5)*lado),int((i+1)*lado))])
				elif self.tabuleiro[i][j].cor == 0:
					if self.tabuleiro[i][j].tipo == 'pedra':
						pygame.draw.circle(display,cinza,(int(j*lado+lado/2),int(i*lado+lado/2)),int(lado/2))
					elif self.tabuleiro[i][j].tipo == 'dama':
						pygame.draw.polygon(display,cinza,[(int(j*lado),int((i+0.5)*lado)),(int((j+1)*lado),int((i+0.5)*lado)),(int((j+0.5)*lado),int(i*lado)),(int((j+0.5)*lado),int((i+1)*lado))])

	def atualizaCasa(self,i,j,cor,tipo):
		self.tabuleiro[i][j].cor = cor
		self.tabuleiro[i][j].tipo = tipo

	def esvaziaCasa(self,i,j):
		self.tabuleiro[i][j].tipo = None
		self.tabuleiro[i][j].cor = '..'

	def movePeca(self,pos1,pos2):
		i1 = pos1[0]
		j1 = pos1[1]
		i2 = pos2[0]
		j2 = pos2[1]

		if (self.podeComerPB[self.tabuleiro[i1][j1].cor]==True): #podecapturar
			self.capturaPeca(pos1,pos2)
			self.Njogadas = 0
		else :
			
			if self.tabuleiro[i1][j1].tipo=='dama':
				self.Njogadas += 1
			else:
				self.Njogadas = 0			

			self.atualizaCasa(i2,j2,self.tabuleiro[i1][j1].cor,self.tabuleiro[i1][j1].tipo)	
			self.esvaziaCasa(i1,j1)

			self.ultimaJogada = self.tabuleiro[i2][j2].cor #atualiza a ultima jogada
			self.verifica()		
		

	def capturaPeca(self,pos1,pos2):
		i1 = pos1[0]
		j1 = pos1[1]
		i2 = pos2[0]
		j2 = pos2[1]	

		if i2-i1>0 and j2-j1>0: #caso +,+
			di = 1
			dj = 1
		elif i2-i1<0 and j2-j1<0: #caso -,-
			di = -1
			dj = -1 
		elif i2-i1>0 and j2-j1<0: #caso +,-
			di = 1
			dj = -1
		elif i2-i1<0 and j2-j1>0: #caso -,+
			di = -1
			dj = 1 

		self.atualizaCasa(i2,j2,self.tabuleiro[i1][j1].cor,self.tabuleiro[i1][j1].tipo)
		for (i,j) in self.tabuleiro[i1][j1].naMira:
			if int((i2-i)/abs(i2-i)) == di and int((j2-j)/abs(j2-j)) == dj and abs(i2-i1)>abs(i2-i) and abs(j2-j1)>abs(j2-j):
				self.atualizaCasa(i2,j2,self.tabuleiro[i1][j1].cor,self.tabuleiro[i1][j1].tipo)
				self.esvaziaCasa(i,j)
				self.esvaziaCasa(i1,j1)

				self.verifica()
				if self.tabuleiro[i2][j2].podeComer == False:
						self.ultimaJogada = self.tabuleiro[i2][j2].cor #atualiza a ultima jogada apenas se nao poder comer mais
				else:
						print("Realize a segunda captura")

				break	

	def verifica(self): #função que verifica quais peças podem capturar(ou simplesmente mover), além de atualizar peças para damas
		self.podeComerPB = [False,False]
		self.podeJogar = [False,False]
		self.podemCapturar = [[],[]]
		self.podemAndar = [[],[]]

		for j in range(8):
			if self.tabuleiro[7][j].cor == 1 :
				self.tabuleiro[7][j].tipo = 'dama'
			if self.tabuleiro[0][j].cor == 0 :
				self.tabuleiro[0][j].tipo = 'dama'

		for i in range(8):
			for j in range(8):
				self.tabuleiro[i][j].podeComer = False
				self.tabuleiro[i][j].naMira = []
				self.tabuleiro[i][j].podeAndar = []
				self.tabuleiro[i][j].podeCapturar = []
				if self.tabuleiro[i][j].cor != None:
					if self.tabuleiro[i][j].tipo == 'pedra':
						self.podeMover(i,j,1,1)
						self.podeMover(i,j,1,-1)
						self.podeMover(i,j,-1,1)
						self.podeMover(i,j,-1,-1)
					
					elif self.tabuleiro[i][j].tipo == 'dama':
						sentido1 = 7-max(i,j) #sentido (di,dj) +
						sentido2 = min(i,j)   #sentido (di,dj) -
						sentido3 = min(7-i,j) #sentido di+,dj-
						sentido4 = min(i,7-j) #sentido di-,dj+
						for k in range(1,sentido1+1):
							self.podeMover(i,j,k,k)
							if self.tabuleiro[i+k][j+k].tipo!=None:  #se há alguma peça, acabam ali os movs da dama
								break
						for k in range(1,sentido2+1):
							self.podeMover(i,j,-k,-k)
							if self.tabuleiro[i-k][j-k].tipo!=None:
								break
						for k in range(1,sentido3+1):
							self.podeMover(i,j,k,-k)
							if self.tabuleiro[i+k][j-k].tipo!=None:
								break
						for k in range(1,sentido4+1):
							self.podeMover(i,j,-k,k)
							if self.tabuleiro[i-k][j+k].tipo!=None:
								break

				#verifica-se, por fim, as possíveis casas finais das damas ao realizar uma captura
						if self.tabuleiro[i][j].podeComer==True:
							for (M,L) in self.tabuleiro[i][j].naMira:
								sentido1 = 7-max(M,L) #sentido (di,dj) +
								sentido2 = min(M,L)   #sentido (di,dj) -
								sentido3 = min(7-M,L) #sentido di+,dj-
								sentido4 = min(M,7-L) #sentido di-,dj+
								if M-i>0 and L-j>0:
									sentido = sentido1
									ki = 1
									kj = 1
								elif M-i<0 and L-j<0:
									sentido = sentido2
									ki = -1
									kj = -1 
								elif M-i>0 and L-j<0:
									sentido = sentido3
									ki = 1
									kj = -1
								elif M-i<0 and L-j>0:
									sentido = sentido4
									ki = -1
									kj = 1 
			
								for k in range(1,sentido+1):
									if self.tabuleiro[M+k*ki][L+k*kj].tipo!=None:  #se há alguma peça, acabam ali os movs da dama
										break
									self.caminhoDama(i,j,M,L,k*ki,k*kj)

	def podeMover(self,i,j,di,dj):
		if 8>i+di>=0 and 8>j+dj>=0:
			if (self.tabuleiro[i+di][j+dj].cor==".."):
				if self.tabuleiro[i][j].tipo == 'pedra':
					if ( (self.tabuleiro[i][j].cor==1) and (di>0) and (self.tabuleiro[i+di][j+dj].tipo==None) ) or ( (self.tabuleiro[i][j].cor==0) and (di<0) and (self.tabuleiro[i+di][j+dj].tipo==None) ): #checa se a pedra pode se mover para a posição
						self.tabuleiro[i][j].podeAndar.append((i+di,j+dj))
						if (i,j) not in self.podemAndar[self.tabuleiro[i][j].cor]:						
							self.podemAndar[self.tabuleiro[i][j].cor].append((i,j))
						self.podeJogar[self.tabuleiro[i][j].cor] = True	
				elif self.tabuleiro[i][j].tipo == 'dama':
					if (self.tabuleiro[i+di][j+dj].tipo==None):
						self.tabuleiro[i][j].podeAndar.append((i+di,j+dj))
						if (i,j) not in self.podemAndar[self.tabuleiro[i][j].cor]:						
							self.podemAndar[self.tabuleiro[i][j].cor].append((i,j))	
						self.podeJogar[self.tabuleiro[i][j].cor] = True
			elif (8>i+di+int(di/abs(di))>=0 and 8>j+dj+int(dj/abs(dj))>=0) and (self.tabuleiro[i+di][j+dj].cor != self.tabuleiro[i][j].cor) and (self.tabuleiro[i+di+int(di/abs(di))][j+dj+int(dj/abs(dj))].tipo==None):
				self.tabuleiro[i][j].podeComer = True
				self.tabuleiro[i][j].naMira.append((i+di,j+dj))
				if self.tabuleiro[i][j].tipo=='pedra': #para pedras, já salva-se as posições finais da capturas
					self.tabuleiro[i][j].podeCapturar.append((i+2*di,j+2*dj))
				self.podeComerPB[self.tabuleiro[i][j].cor] = True
				if (i,j) not in self.podemCapturar[self.tabuleiro[i][j].cor]:
					self.podemCapturar[self.tabuleiro[i][j].cor].append((i,j))
				self.podeJogar[self.tabuleiro[i][j].cor] = True					
			
			
	def caminhoDama(self,m,l,i,j,di,dj): #checa se a dama pode parar nessa posição ao comer
		if 8>i+di>=0 and 8>j+dj>=0:
			if (self.tabuleiro[i+di][j+dj].tipo==None):
				self.tabuleiro[m][l].podeCapturar.append((i+di,j+dj))	
		


def desenhaTabuleiro():
		y=0
		for i in range(8):
			x=0
			for j in range(8):
				if i%2 == 0:
					if j%2==0:					
						pygame.draw.rect(display,cor_tabuleiro,(x,y,75,75))
					else:
						pygame.draw.rect(display,branco,(x,y,lado,lado))
				else:
					if j%2==0:
						pygame.draw.rect(display,branco,(x,y,lado,lado))
					else:
						pygame.draw.rect(display,cor_tabuleiro,(x,y,75,75))
				x+=lado
			y+=lado

start_game = False
while not start_game:
	display.fill(preto)
	fonte1 = pygame.font.Font(None,80)
	fonte2 = pygame.font.Font(None,40)
	texto1 = fonte1.render("Jogo de Damas",True,vermelho_escuro)
	display.blit(texto1,(100,200))
	texto2 = fonte2.render("Clique na tela para começar o jogo",True,vermelho_claro)
	display.blit(texto2,(100,300))
	texto3 = fonte2.render("Autor: Victor Almeida ",True,branco)
	display.blit(texto3,(100,500))
	texto4 = fonte2.render("nUSP: 10728101",True,branco)
	display.blit(texto4,(100,560))

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == MOUSEBUTTONDOWN:
			start_game = True
	
pos1 = [None,None]
pos2 = [None,None]
optAndar = []
optCapturar = []
jogo = Damas()
jogo.verifica()

start_game = False
game_over = False
while not game_over:
	
	if jogo.Njogadas>=20 or (jogo.podeJogar[0]==False and jogo.ultimaJogada==1) or (jogo.podeJogar[1]==False and jogo.ultimaJogada==0): #checa se houve empate
		if jogo.Njogadas>=20:
			vencedor = 'Jogo empatado!'
			mensagem = "Tudo isso para acabar assim?"
		elif jogo.podeJogar[0]==False and jogo.ultimaJogada==1:
			vencedor = "Jogador Preto vencedor!"
			mensagem = "Não foi dessa vez, jogador Branco!"
		elif jogo.podeJogar[1]==False and jogo.ultimaJogada==0:
			vencedor = "Jogador Branco vencedor!"
			mensagem = "Não foi dessa vez, jogador Preto!"
		while not start_game:		
			display.fill(preto)
			fonte1 = pygame.font.Font(None,60)
			fonte2 = pygame.font.Font(None,40)
			texto1 = fonte1.render(vencedor,True,vermelho_escuro)
			display.blit(texto1,(50,200))
			texto2 = fonte2.render(mensagem,True,vermelho_claro)
			display.blit(texto2,(50,300))
			texto3 = fonte2.render("Autor: Victor Almeida ",True,branco)
			display.blit(texto3,(50,500))
			texto4 = fonte2.render("nUSP: 10728101",True,branco)
			display.blit(texto4,(50,560))

			pygame.display.flip()

			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
					start_game = True
					game_over = True
				if event.type == pygame.QUIT:
					game_over = True
					pygame.quit()
					quit()		
#jogada do computador
	if jogo.ultimaJogada==0 and jogo.podeJogar[1]==True: #o computador joga com as peças pretas
		print('capturar',jogo.podemCapturar[1])
		print('andar',jogo.podemAndar[1])
		if jogo.podeComerPB[1]==True:
			pos1_ = random.choice(jogo.podemCapturar[1])
			pos2_ = random.choice(jogo.tabuleiro[pos1_[0]][pos1_[1]].podeCapturar)
		else:
			pos1_ = random.choice(jogo.podemAndar[1])
			pos2_ = random.choice(jogo.tabuleiro[pos1_[0]][pos1_[1]].podeAndar)
		jogo.movePeca(pos1_,pos2_)
			

#jogada do ser humano
	for event in pygame.event.get(): #o humano joga com as peças brancas
		if event.type == pygame.QUIT:
			game_over = True
			pygame.quit()
			quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pos1)
			if pos1==[None,None]:
				_pos1 = pygame.mouse.get_pos()
				pos1[0] = int(_pos1[1]//lado)
				pos1[1] = int(_pos1[0]//lado)
				if (jogo.ultimaJogada==1 and jogo.podeJogar[0]==True and jogo.tabuleiro[pos1[0]][pos1[1]].cor==0 ):
					if jogo.podeComerPB[jogo.tabuleiro[pos1[0]][pos1[1]].cor] == False:
						for (i,j) in jogo.tabuleiro[pos1[0]][pos1[1]].podeAndar:
							optAndar.append((i,j))
					elif jogo.podeComerPB[jogo.tabuleiro[pos1[0]][pos1[1]].cor] == True:
						if jogo.tabuleiro[pos1[0]][pos1[1]].podeComer == True:
							for (i,j) in jogo.tabuleiro[pos1[0]][pos1[1]].podeCapturar:
								optCapturar.append((i,j))
						else:
							pos1 = [None,None]
				else:
					pos1 = [None,None]
			elif pos2==[None,None]:
				_pos2 = pygame.mouse.get_pos()
				pos2[0] = int(_pos2[1]//lado)
				pos2[1] = int(_pos2[0]//lado)
				if (pos2[0],pos2[1]) in optAndar or (pos2[0],pos2[1]) in optCapturar:	
					jogo.movePeca(pos1,pos2)
					pos1 = [None,None]
					pos2 = [None,None]
					optAndar = []
					optCapturar = []
				else:
					pos2 = [None,None]


	display.fill(preto)
	desenhaTabuleiro()
	jogo.imprimeTabuleiro()
	if optCapturar != []:
		for (i,j) in optCapturar:
			pygame.draw.circle(display,verde_escuro,(int(j*lado+lado/2),int(i*lado+lado/2)),int(lado/2))
	elif optAndar != []:
		for (i,j) in optAndar:
			pygame.draw.circle(display,verde_claro,(int(j*lado+lado/2),int(i*lado+lado/2)),int(lado/2))

	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()

