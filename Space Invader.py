import pygame
from pygame.locals import *
from sys import exit
from random import randint

T = [] # Matriz dos Inimigos
OB1=[] # Matriz da Barreira 1
OB2=[] # Matriz da Barreira 2
OB3=[] # Matriz da Barreira 3
OB4=[] # Matriz da Barreira 4
C = ((0,18), (0,7), (10,7), (15,0), (20,7), (30,7), (30,18))# Tupla desenho do canhão
XC = 420 # Posição do Canhão em X
YC = 480 # Posição do Canhão em Y
CorFundo = (255, 210, 255)
lar = 30 # Largura dos inimigos
esp = 10 # Espessura entre os inimigos
alt = 30 # Altura dos inimigos
xTiroC = 330 # Posição inicial do tiro do canhão em X
yTiroC = 480 # Posição inicial do tiro do canhão em Y
xTiroI_1 = 0 # Posição inicial do tiro do Inimigo em X
yTiroI_1 = 0 # Posição inicial do tiro do Inimigo em Y
xTiroI_2 = 0 # Posição inicial do tiro do Inimigo em X
yTiroI_2 = 0 # Posição inicial do tiro do Inimigo em Y
tob = 13  # Altura e Largura das Barreiras
mov = 0.7  # Velocidade da movimentação dos inimigos
vTiro = 5  # Velocidade da movimentação do Tiro
pos = (0,0) # Captura a posição do mouse
score = 0 # Guarda o valor do score
Maxscore = 0 # Guarda o valor do Maximo do Score
Nave = (50, 30) # Desenho para nave
xNave_1 = -60 # Posição da Nave_1 em Y
yNave_1 = 50 # Posição da Nave_1 em Y
movNave_1 = 2 # Velocidade da movimentação da Nave_1
Timernave_1 = 0 # Tempo para movimentação da Nave_1
xNave_2 = -60 # Posição da Nave_2 em Y
yNave_2 = 50 # Posição da Nave_2 em Y
movNave_2 = 3 # Velocidade da movimentação da Nave_2
Timernave_2 = 0 # Tempo para movimentação da Nave_2
flag = 0
Rt = 0

#Funções-----------------------------------------------------------------------------------

def CriaInimigos():
  E=[]  
  for j in range(5):
    i = 0
    for i in range(12):
      if j<1:
        o = [2, 50+i*(lar+esp), 100+j*(alt+esp)]    
      elif (j==1 or j==2):
        o = [3, 50+i*(lar+esp), 100+j*(alt+esp)]
      elif j>=3:
        o = [1, 50+i*(lar+esp), 100+j*(alt+esp)]
      E.append(o)
  return(E)
  
def CriaObstaculos(num):
  CO=[]
  
  for j in range(6):
    i = 0
    for i in range(8):
      o = (50+i*(tob), 380+j*(tob), (255, 150-j*20, 255), (89, 0, 180))
      p = (217+i*(tob), 380+j*(tob), (255, 150-j*20, 255), (89, 0, 180))
      q = (384+i*(tob), 380+j*(tob), (255, 150-j*20, 255), (89, 0, 180))
      r = (551+i*(tob), 380+j*(tob), (255, 150-j*20, 255), (89, 0, 180))
      if not((j==0 and i==0) or (j==0 and i==7) or (j==3 and i>2 and i<5) or (j==4 and i>1 and i<6) or (j==5 and i>1 and i<6)):
        if num==1:
          CO.append(o)
        if num==2:
          CO.append(p)
        if num==3:
          CO.append(q)
        if num==4:
          CO.append(r)
  return(CO)

def Start():
  global Vida,pos
  x=randint(20,680)
  y=randint(20,480)
  z=15
  
  tela.fill(CorFundo)
  if (randint(0,20)==5):
    pygame.draw.circle(tela, (255, 128, 0), (x, y), int(z), 0)
    pygame.draw.circle(tela, (255, 0, 0), (x, y), int(z*.6), 0)
    pygame.draw.line(tela, (255, 0, 0), (x+3, y), (x+z+3, y), 3)
    pygame.draw.line(tela, (255, 0, 0), (x-3, y), (x-z-3, y), 3)
    pygame.draw.line(tela, (255, 0, 0), (x, y-3), (x, y-z-3), 3)
    pygame.draw.line(tela, (255, 0, 0), (x, y+3), (x, y+z+3), 3)
    pygame.draw.line(tela, (255, 0, 0), (x-3, y-3), (x-z, y-z), 4)
    pygame.draw.line(tela, (255, 0, 0), (x+3, y+3), (x+z, y+z), 4)
    pygame.draw.line(tela, (255, 0, 0), (x-3, y+3), (x-z, y+z), 4)
    pygame.draw.line(tela, (255, 0, 0), (x+3, y-3), (x+z, y-z), 4)
  fonte = pygame.font.SysFont("Arial", 90)
  textsurface = fonte.render("Space Invader", True, (0, 0, 0))
  tela.blit(textsurface,(100,150))
  fonte = pygame.font.SysFont("Arial", 40)
  pygame.draw.rect(tela, (0, 0, 0), (288, 300, 100, 50), 1)
  textsurface = fonte.render("Start", True, (0, 0, 0))
  tela.blit(textsurface,(300,300))
  fonte = pygame.font.SysFont("Arial", 15)
  textsurface = fonte.render("SCORE: "+str(score), True, (0, 0, 0))
  tela.blit(textsurface,(10,10))
  textsurface = fonte.render(" HI-SCORE: "+str(Maxscore), True, (0, 0, 0))
  tela.blit(textsurface,(300,10))
  textsurface = fonte.render(" LIFE: "+str(Vida), True, (0, 0, 0))
  tela.blit(textsurface,(600,10))
  if (pos >= (288,300)) and (pos <= (288+100,300+50)):
      Vida=3
   

def DesenhaAmbiente():
  global Rt
  tela.fill(CorFundo)

  fonte = pygame.font.SysFont("Arial", 15)
  textsurface = fonte.render("SCORE: "+str(score), True, (0, 0, 0))
  tela.blit(textsurface,(10,10))
  textsurface = fonte.render(" HI-SCORE: "+str(Maxscore), True, (0, 0, 0))
  tela.blit(textsurface,(300,10))
  textsurface = fonte.render(" LIFE: "+str(Vida), True, (0, 0, 0))
  tela.blit(textsurface,(600,10))

  # INIMIGOS
  for i in range(len(T)):
    if T[i][0]==2:
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1], T[i][2], 30, 30), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1], T[i][2], 30, 30), 1) 
      pygame.draw.rect(tela, CorFundo, (T[i][1]+5, T[i][2]+5, 20, 20), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+5, T[i][2]+5, 20, 20), 1) 
      pygame.draw.rect(tela, (255, 170, 213), (T[i][1]+12-Rt, T[i][2]+12-Rt, 6, 6), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+12-Rt, T[i][2]+12-Rt, 6, 6), 1) 
      
    if T[i][0]==3:
      pygame.draw.rect(tela, (255, 170, 213), (T[i][1], T[i][2], 13, 13), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1], T[i][2], 13, 13), 1) 
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1]+5, T[i][2]+5, 8, 8), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+5, T[i][2]+5, 8, 8), 1) 
      pygame.draw.rect(tela, (255, 170, 213), (T[i][1]+17, T[i][2], 13, 13), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+17, T[i][2], 13, 13), 1) 
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1]+17, T[i][2]+5, 8, 8), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+17, T[i][2]+5, 8, 8), 1) 
      pygame.draw.rect(tela, (255, 170, 213), (T[i][1], T[i][2]+17, 13, 13), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1], T[i][2]+17, 13, 13), 1) 
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1]+5, T[i][2]+17, 8, 8), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+5, T[i][2]+17, 8, 8), 1) 
      pygame.draw.rect(tela, (255, 170, 213), (T[i][1]+17, T[i][2]+17, 13, 13), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+17, T[i][2]+17, 13, 13), 1) 
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1]+17, T[i][2]+17, 8, 8), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+17, T[i][2]+17, 8, 8), 1) 
      pygame.draw.rect(tela, (255, 170, 213), (T[i][1]+8, T[i][2]+8, 14, 14), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1]+8, T[i][2]+8, 14, 14), 1) 
      pygame.draw.circle(tela, (111, 0, 221), (int(T[i][1]+15), int(T[i][2]+15)), 4+Rt , 0)
      pygame.draw.circle(tela, (0, 0, 0), (int(T[i][1]+15), int(T[i][2]+15)), 4+Rt , 1)
      
    if T[i][0]==1:
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1], T[i][2], 30, 13), 0) 
      pygame.draw.rect(tela, (0 ,0 , 0), (T[i][1], T[i][2], 30, 13), 1) 
      pygame.draw.rect(tela, (111, 0, 221), (T[i][1], T[i][2]+17, 30, 13), 0) 
      pygame.draw.rect(tela, (0, 0, 0), (T[i][1], T[i][2]+17, 30, 13), 1) 
      pygame.draw.circle(tela, (255, 175, 255), (int(T[i][1]+15), int(T[i][2]+15)), 12 , 0)
      pygame.draw.circle(tela, (0, 0, 0), (int(T[i][1]+15), int(T[i][2]+15)), 12 , 1)
      pygame.draw.circle(tela, (111, 0, 221), (int(T[i][1]+15+Rt), int(T[i][2]+15+Rt)), 3 , 0)
      pygame.draw.circle(tela, (0, 0, 0), (int(T[i][1]+15+Rt), int(T[i][2]+15+Rt)), 3 , 1)

  # BARREIRAS    
  for i in range(len(OB1)):
    pygame.draw.rect(tela, OB1[i][2], (OB1[i][0], OB1[i][1], tob, tob), 0)
    pygame.draw.rect(tela, OB1[i][3], (OB1[i][0], OB1[i][1], tob, tob), 1)
  for i in range(len(OB2)):
    pygame.draw.rect(tela, OB2[i][2], (OB2[i][0], OB2[i][1], tob, tob), 0)
    pygame.draw.rect(tela, OB2[i][3], (OB2[i][0], OB2[i][1], tob, tob), 1)
  for i in range(len(OB3)):
    pygame.draw.rect(tela, OB3[i][2], (OB3[i][0], OB3[i][1], tob, tob), 0)
    pygame.draw.rect(tela, OB3[i][3], (OB3[i][0], OB3[i][1], tob, tob), 1)
  for i in range(len(OB4)):
    pygame.draw.rect(tela, OB4[i][2], (OB4[i][0], OB4[i][1], tob, tob), 0)
    pygame.draw.rect(tela, OB4[i][3], (OB4[i][0], OB4[i][1], tob, tob), 1)

  #NAVE 1
  pygame.draw.rect(tela, (111, 0, 221), (xNave_1, yNave_1, 50, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_1, yNave_1, 50, 10), 1) 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_1, yNave_1+20, 50, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_1, yNave_1+20, 50, 10), 1) 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_1+5, yNave_1+5, 40, 20), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_1+5, yNave_1+5, 40, 20), 1)
  for i in range(3):
    pygame.draw.circle(tela, (255, 175, 255), (xNave_1+15+10*i, yNave_1+15), 6, 0)
    pygame.draw.circle(tela, (0, 0, 0), (xNave_1+15+10*i, yNave_1+15), 6, 1)

  #NAVE 2 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_2, yNave_2, 12, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_2, yNave_2, 12, 10), 1) 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_2+19, yNave_2, 12, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_2+19, yNave_2, 12, 10), 1) 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_2+38, yNave_2, 12, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_2+38, yNave_2, 12, 10), 1) 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_2, yNave_2+20, 12, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_2, yNave_2+20, 12, 10), 1)
  pygame.draw.rect(tela, (111, 0, 221), (xNave_2+19, yNave_2+20, 12, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_2+19, yNave_2+20, 12, 10), 1) 
  pygame.draw.rect(tela, (111, 0, 221), (xNave_2+38, yNave_2+20, 12, 10), 0) 
  pygame.draw.rect(tela, (0, 0, 0), (xNave_2+38, yNave_2+20, 12, 10), 1) 
  pygame.draw.circle(tela, (255, 175, 255), (xNave_2+10, yNave_2+15), 10, 0)
  pygame.draw.circle(tela, (0, 0, 0), (xNave_2+10, yNave_2+15), 10, 1)
  pygame.draw.circle(tela, (255, 175, 255), (xNave_2+40, yNave_2+15), 10, 0)
  pygame.draw.circle(tela, (0, 0, 0), (xNave_2+40, yNave_2+15), 10, 1)
  pygame.draw.circle(tela, (255, 175, 255), (xNave_2+25, yNave_2+15), 10, 0)
  pygame.draw.circle(tela, (0, 0, 0), (xNave_2+25, yNave_2+15), 10, 1)

def Canhao(C, x, y):
  R = []
  for i in range(len(C)):
    a = C[i][0] + x
    b = C[i][1] + y
    R.append((a, b))
  return(tuple(R))

def TrataEntradaUsuario():
  global TiroAtivoC
  global XC
  global xTiroC, yTiroC
  if Teclas[K_LEFT]:
    if XC>13:
      XC = XC - 3
  if Teclas[K_RIGHT]:
    if XC<660:
      XC = XC + 3    
  if Teclas[K_SPACE] and not TiroAtivoC:
    xTiroC = XC + C[3][0]
    yTiroC = 480
    TiroAtivoC = True

def Colisões():
  global Vida
  for i in range(len(T)):  
    for j in range(len(OB1)):
      if OB1[j][0] <= T[i][1]+lar/2 <= OB1[j][0]+tob and OB1[j][1] <= T[i][2]+alt <= OB1[j][1]+tob:
        Explosão(OB1[j][0],OB1[j][1])
        del(OB1[j])
        break
  for i in range(len(T)):  
    for j in range(len(OB2)):
      if OB2[j][0] <= T[i][1]+lar/2 <= OB2[j][0]+tob and OB2[j][1] <= T[i][2]+alt <= OB2[j][1]+tob:
        Explosão(OB2[j][0],OB2[j][1])
        del(OB2[j])
        break
  for i in range(len(T)):  
    for j in range(len(OB3)):
      if OB3[j][0] <= T[i][1]+lar/2 <= OB3[j][0]+tob and OB3[j][1] <= T[i][2]+alt <= OB3[j][1]+tob:
        Explosão(OB3[j][0],OB3[j][1])
        del(OB3[j])
        break
  for i in range(len(T)):  
    for j in range(len(OB4)):
      if OB4[j][0] <= T[i][1]+lar/2 <= OB4[j][0]+tob and OB4[j][1] <= T[i][2]+alt <= OB4[j][1]+tob:
        Explosão(OB4[j][0],OB4[j][1])
        del(OB4[j])
        break
  for i in range(len(T)):  
      if XC <= T[i][1]+lar/2 <= XC+30 and YC <= T[i][2]+alt <= YC+17:
        Explosão(int(T[i][1]+lar/2),int(T[i][2]+alt))
        Vida-=1
        break


  
    
def TrataTiroPlayer():
  global TiroAtivoC
  global yTiroC,xTiroC
  global score
  global xNave_1,yNave_1,xNave_2,yNave_2
  global Timernave_1,Flagnave_1,Timernave_2,Flagnave_2

  for i in range(len(OB1)):
    if OB1[i][0] <= xTiroC <= OB1[i][0]+tob and OB1[i][1] <= yTiroC <= OB1[i][1]+tob and TiroAtivoC == True:
      TiroAtivoC = False
      Explosão(xTiroC,yTiroC)
      del(OB1[i])
      break
  if yTiroC < 5:
    TiroAtivoC = False
    
  for i in range(len(OB2)):
    if OB2[i][0] <= xTiroC <= OB2[i][0]+tob and OB2[i][1] <= yTiroC <= OB2[i][1]+tob and TiroAtivoC == True:
      TiroAtivoC = False
      Explosão(xTiroC,yTiroC)
      del(OB2[i])
      break
  if yTiroC < 5:
    TiroAtivoC = False
    
  for i in range(len(OB3)):
    if OB3[i][0] <= xTiroC <= OB3[i][0]+tob and OB3[i][1] <= yTiroC <= OB3[i][1]+tob and TiroAtivoC == True:
      TiroAtivoC = False
      Explosão(xTiroC,yTiroC)
      del(OB3[i])
      break
  if yTiroC < 5:
    TiroAtivoC = False
    
  for i in range(len(OB4)):
    if OB4[i][0] <= xTiroC <= OB4[i][0]+tob and OB4[i][1] <= yTiroC <= OB4[i][1]+tob and TiroAtivoC == True:
      TiroAtivoC = False
      Explosão(xTiroC,yTiroC)
      del(OB4[i])
      break
  if yTiroC < 5:
    TiroAtivoC = False

  if xNave_1 <= xTiroC <= xNave_1 + Nave[0] and yNave_1 <= yTiroC <= yNave_1+Nave[1] and TiroAtivoC == True:
    xNave_1 = -60
    yNave_1 = 50
    Timernave_1=0
    Flagnave_1= False
    score= score+500    
    TiroAtivoC = False
    Explosão(xTiroC,yTiroC)

  if xNave_2 <= xTiroC <= xNave_2 + Nave[0] and yNave_2 <= yTiroC <= yNave_2+Nave[1] and TiroAtivoC == True:
    xNave_2 = -60
    yNave_2 = 50
    Timernave_2=0
    Flagnave_2= False
    score= score+1000    
    TiroAtivoC = False
    Explosão(xTiroC,yTiroC)
    
    

  for i in range(len(T)):
    if T[i][1] <= xTiroC <= T[i][1]+lar and T[i][2] <= yTiroC <= T[i][2]+alt and TiroAtivoC == True:
      TiroAtivoC = False
      if T[i][0]==1:
        score= score+10
      if T[i][0]==2:
        score= score+20
      if T[i][0]==3:
        score= score+40
      Explosão(xTiroC,yTiroC)
      del(T[i])
      break
  if yTiroC < 5:
    TiroAtivoC = False
    
  if TiroAtivoC:
    for z in range(12):
      pygame.draw.circle(tela, (72, 164, 255), (xTiroC, int(yTiroC)+z), 3, 0)
    yTiroC = yTiroC - vTiro

def TrataTiroInimigos_1():
  global TiroAtivoI_1
  global yTiroI_1, xTiroI_1
  global Vida

  for i in range(len(OB1)):
    if OB1[i][0] <= xTiroI_1 <= OB1[i][0]+tob and OB1[i][1] <= yTiroI_1 <= OB1[i][1]+tob and TiroAtivoI_1 == True:
      TiroAtivoI_1 = False
      Explosão(xTiroI_1,yTiroI_1)
      del(OB1[i])
      yTiroI_1 = 0
      break
    
  for i in range(len(OB2)):
    if OB2[i][0] <= xTiroI_1 <= OB2[i][0]+tob and OB2[i][1] <= yTiroI_1 <= OB2[i][1]+tob and TiroAtivoI_1 == True:
      TiroAtivoI_1 = False
      Explosão(xTiroI_1,yTiroI_1)
      del(OB2[i])
      yTiroI_1 = 0
      break
    
  for i in range(len(OB3)):
    if OB3[i][0] <= xTiroI_1 <= OB3[i][0]+tob and OB3[i][1] <= yTiroI_1 <= OB3[i][1]+tob and TiroAtivoI_1 == True:
      TiroAtivoI_1 = False
      Explosão(xTiroI_1,yTiroI_1)
      del(OB3[i])
      yTiroI_1 = 0
      break
    
  for i in range(len(OB4)):
    if OB4[i][0] <= xTiroI_1 <= OB4[i][0]+tob and OB4[i][1] <= yTiroI_1 <= OB4[i][1]+tob and TiroAtivoI_1 == True:
      TiroAtivoI_1 = False
      Explosão(xTiroI_1,yTiroI_1)
      del(OB4[i])
      yTiroI_1 = 0
      break
    
  if XC <= xTiroI_1 <= XC+30 and YC <= yTiroI_1 <= YC+17 and TiroAtivoI_1 == True:
    TiroAtivoI_1 = False
    Explosão(xTiroI_1,yTiroI_1)
    Vida-=1
    yTiroI_1 = 0
    
  if yTiroI_1 > 500:
    TiroAtivoI_1 = False
    yTiroI_1 = 0

  if (not TiroAtivoI_1) and (randint(0,100)==5):
    xTiroI_1 = 0
    yTiroI_1 = 0
    yMaxT = 0
    xCont = 0
    for i in range(len(T)):
      if T[i][2] > yMaxT:
        yMaxT = T[i][2]
    for i in range(len(T)):
      if T[i][2] == yMaxT:
        xCont += 1
    for i in range(len(T)):
      if T[i][2] > yTiroI_1:
        yTiroI_1 = int(T[i][2]+lar)
    xTiroI_1 = int(T[randint((len(T)-xCont-1),(len(T)-1))][1]+(lar/2))
    TiroAtivoI_1 = True

  if TiroAtivoI_1:
    for z in range(12):
      pygame.draw.circle(tela, (255, 72, 72), (xTiroI_1, int(yTiroI_1)+z), 3, 0)
    yTiroI_1 = yTiroI_1 + vTiro

def TrataTiroInimigos_2():
  global TiroAtivoI_2
  global yTiroI_2, xTiroI_2
  global Vida

  for i in range(len(OB1)):
    if OB1[i][0] <= xTiroI_2 <= OB1[i][0]+tob and OB1[i][1] <= yTiroI_2 <= OB1[i][1]+tob and TiroAtivoI_2 == True:
      TiroAtivoI_2 = False
      Explosão(xTiroI_2,yTiroI_2)
      del(OB1[i])
      yTiroI_2 = 0
      break
    
  for i in range(len(OB2)):
    if OB2[i][0] <= xTiroI_2 <= OB2[i][0]+tob and OB2[i][1] <= yTiroI_2 <= OB2[i][1]+tob and TiroAtivoI_2 == True:
      TiroAtivoI_2 = False
      Explosão(xTiroI_2,yTiroI_2)
      del(OB2[i])
      yTiroI_2 = 0
      break
    
  for i in range(len(OB3)):
    if OB3[i][0] <= xTiroI_2 <= OB3[i][0]+tob and OB3[i][1] <= yTiroI_2 <= OB3[i][1]+tob and TiroAtivoI_2 == True:
      TiroAtivoI_2 = False
      Explosão(xTiroI_2,yTiroI_2)
      del(OB3[i])
      yTiroI_2 = 0
      break
    
  for i in range(len(OB4)):
    if OB4[i][0] <= xTiroI_2 <= OB4[i][0]+tob and OB4[i][1] <= yTiroI_2 <= OB4[i][1]+tob and TiroAtivoI_2 == True:
      TiroAtivoI_2 = False
      Explosão(xTiroI_2,yTiroI_2)
      del(OB4[i])
      yTiroI_2 = 0
      break
    

  if XC-6<= xTiroI_2 <= XC+36 and YC <= yTiroI_2 <= YC+17 and TiroAtivoI_2 == True:
    TiroAtivoI_2 = False
    Explosão(xTiroI_2,yTiroI_2)
    Vida-=1
    yTiroI_2 = 0
    
  if yTiroI_2 > 500:
    TiroAtivoI_2 = False
    yTiroI_2 = 0

  if (not TiroAtivoI_2) and (randint(0,100)==5):
    xTiroI_2 = 0
    yTiroI_2 = 0
    yMaxT = 0
    xCont = 0
    for i in range(len(T)):
      if T[i][2] > yMaxT:
        yMaxT = T[i][2]
    for i in range(len(T)):
      if T[i][2] == yMaxT:
        xCont += 1
    for i in range(len(T)):
      if T[i][2] > yTiroI_2:
        yTiroI_2 = int(T[i][2]+lar)
    xTiroI_2 = int(T[randint((len(T)-xCont-1),(len(T)-1))][1]+(lar/2))
    TiroAtivoI_2 = True

  if TiroAtivoI_2:
    for z in range(12):
      pygame.draw.circle(tela, (148, 40, 255), (xTiroI_2, int(yTiroI_2)+z), 3, 0)
    yTiroI_2 = yTiroI_2 + vTiro

def MovimentaNaves():
    global lar,mov
    xMax=0
    xMin=700
    yInc=0
    
    for i in range(len(T)):
      if T[i][1]>xMax:
        xMax=T[i][1]
      if T[i][1]<xMin:
        xMin=T[i][1]
      
    if xMax>=700-lar:
      if yInc<1:
        yInc=1
      mov=-(mov+0.02)
    if xMin<=0:
      if yInc<1:
        yInc=1
      mov=-(mov-0.02)
        
    for i in range(len(T)):
      T[i][2] = T[i][2]+yInc
      T[i][1] = T[i][1]+mov

def Explosão(x,y):
  z=10
  for r in range(30):
    pygame.draw.circle(tela, (255, 128, 0), (x, y), int(z), 0)
    pygame.draw.circle(tela, (255, 0, 0), (x, y), int(z*.6), 0)
    pygame.draw.line(tela, (255, 0, 0), (x+3, y), (x+z+3, y), 3)
    pygame.draw.line(tela, (255, 0, 0), (x-3, y), (x-z-3, y), 3)
    pygame.draw.line(tela, (255, 0, 0), (x, y-3), (x, y-z-3), 3)
    pygame.draw.line(tela, (255, 0, 0), (x, y+3), (x, y+z+3), 3)
    pygame.draw.line(tela, (255, 0, 0), (x-3, y-3), (x-z, y-z), 4)
    pygame.draw.line(tela, (255, 0, 0), (x+3, y+3), (x+z, y+z), 4)
    pygame.draw.line(tela, (255, 0, 0), (x-3, y+3), (x-z, y+z), 4)
    pygame.draw.line(tela, (255, 0, 0), (x+3, y-3), (x+z, y-z), 4)
    pygame.display.update

def NaveMae_1():
  global xNave_1,yNave_1
  global movNave_1
  global Timernave_1,Flagnave_1

  if xNave_1>=800-50:
    movNave_1 = -movNave_1
    Flagnave_1= False
    Timernave_1=0
    xNave_1=740
  if xNave_1<=-100:
    movNave = -movNave_1
    Flagnave_1= False
    Timernave_1=0
    xNave_1=-60

  if Flagnave_1:
    xNave_1= xNave_1+ movNave_1
    
def NaveMae_2():
  global xNave_2,yNave_2
  global movNave_2
  global Timernave_2,Flagnave_2

  if xNave_2>=800-50:
    movNave_2 = -movNave_2
    Flagnave_2 = False
    Timernave_2 = 0
    xNave_2=740
  if xNave_2<=-100:
    movNave_2 = -movNave_2
    Flagnave_2 = False
    Timernave_2 = 0
    xNave_2=-60

  if Flagnave_2:
    xNave_2= xNave_2+ movNave_2
  
  

    
#Fim Funções-----------------------------------------------------------------------------------

pygame.init()
tela = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
pygame.display.set_caption('Space Invader')
TiroAtivoC = False
TiroAtivoI_1 = False
TiroAtivoI_2 = False
Vida = 0

fim = False
while not fim:
  
  if Vida == 0:
    Start()
    score=0
    pos=(0,0)
    T=CriaInimigos()
    OB1=CriaObstaculos(1)
    OB2=CriaObstaculos(2)
    OB3=CriaObstaculos(3)
    OB4=CriaObstaculos(4)
    TiroAtivoC = False
    TiroAtivoI_1 = False
    TiroAtivoI_2 = False
    Flagnave_1= False
    Flagnave_2= False
  
  elif Vida>0:  
    DesenhaAmbiente()
    MovimentaNaves()
    pygame.draw.polygon(tela, (60, 60, 60), Canhao(C, XC, YC), 0)
    pygame.draw.circle(tela, (60, 60, 60), (XC, 13+YC), 6, 0)
    pygame.draw.circle(tela, (60 ,60 , 60), (30+XC, 13+YC), 6, 0)
    TrataTiroPlayer()
    TrataTiroInimigos_1() 
    TrataTiroInimigos_2()
    Teclas = pygame.key.get_pressed()
    TrataEntradaUsuario()
    NaveMae_1()
    NaveMae_2()
    Colisões()

  if Timernave_1<1000:
    Timernave_1+=1
  else:
    Flagnave_1= True
    
  if Timernave_2<2000:
    Timernave_2+=1
  else:
    Flagnave_2= True

  if len(T) == 0:
    T=CriaInimigos()
    
  if score > Maxscore:
    Maxscore=score

  if flag<50:
    flag+=1
  else:
    flag=0
    Rt=randint(-3,3)
  
  pygame.display.update()
  time_passed = clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
    if event.type == QUIT:
      fim = True

pygame.display.quit()
