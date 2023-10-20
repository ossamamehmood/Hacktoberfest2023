import time
import sys
import pygame
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((648, 604), RESIZABLE)


def initialisation(): #choice beetween play or help
  window.blit(pygame.image.load("start.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 489 > event.pos[1]:
            pendu()
          if 488 < event.pos[1]:
            help()
      if event.type == KEYDOWN:
        pendu()

def help(): #display help
  window.blit(pygame.image.load("help.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        initialisation()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

def menu(): #choice beetween replay or go start
  time.sleep(1.5)
  window.blit(pygame.image.load("menu.png").convert(), (230, 362))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 200 < event.pos[1] < 239:
            if 230 < event.pos[0] < 364:
              initialisation()
            if 364 < event.pos[0] < 498:
              pendu()
      if event.type == KEYDOWN:
        if event.key == K_KP0:
          initialisation()
        if event.key == K_KP1:
          pendu()

def pendu():
  window.blit(pygame.image.load("choice.png").convert(), (0, 0))
  pygame.display.flip()
  wordselect = []
  n = 0 #number of letter
  c = 0 #select letter
  o = 0 #number of chance
  while True:
    c = touche(0)
    if c == -1:
      break
    if c == -2 and n > 0:
      del wordselect[-1]
      n -= 1
      window.blit(pygame.image.load("choice.png").convert(), (0, 0))
      space(n)
      for h in range(n):
        affichage(wordselect[h], h, n)
    if c != -2 and n < 25:
      window.blit(pygame.image.load("choice.png").convert(), (0, 0))
      n += 1
      space(n)
      wordselect.append(c)
      for h in range(n):
        affichage(wordselect[h], h, n)
  e = [0] * (n)
  window.blit(pygame.image.load("pendu.png").convert(), (0, 0))
  window.blit(pygame.image.load("pendu0.png").convert(), (120, 0))
  pygame.display.flip()
  time.sleep(0.1) #user need to up his finger to keyboard
  space(n)
  while True:
    d = touche(1)
    p = False
    #faire image du pendu en fonction de la variable o
    for k in range(len(wordselect)):
      if wordselect[k] == d and d != e[k]:
        e[k] = d
        p = True
    if p == False:
      o += 1
      nombre = "pendu" + str(o) + ".png"
      window.blit(pygame.image.load(nombre).convert(), (120, 0))
      pygame.display.flip()
    for l in range(len(e)):
      if e[l] != 0:
        affichage(e[l], l, n)
    if e == wordselect:
      window.blit(pygame.image.load("win.png").convert(), (0, 0))
      pygame.display.flip()
      menu()
    if o == 8:
      window.blit(pygame.image.load("lose.png").convert(), (0, 0))
      pygame.display.flip()
      menu()

def affichage(d, l, n):
  if n == 25:
    if l == 24:
      n = 0
    else:
      n = 12
  if n > 12:
    if l < 12:
      n = 12
    if 12 <= l:
      n = n - 12
  col = l / 12
  line = l % 12
  window.blit(pygame.font.Font(None, 70).render(d,1,(0,0,0)), (35 + line * 50 + 300 - 25 * n, 200 + col * 80 - 30 + 220))
  pygame.display.flip()

def space(m):
  for l in range(m):
    n = m
    if n == 25:
      if l == 24:
        n = 0
      else:
        n = 12
    if n > 12:
      if l < 12:
        n = 12
      if 11 < l:
        n = n - 12
    col = l / 12
    line = l % 12
    window.blit(pygame.image.load("space.png").convert(), (35 + line * 50 + 300 - 25 * n, 200 + col * 80 + 15 + 225))
  pygame.display.flip()

def touche(a):
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if a == 0:
          if event.key == K_RETURN:
            return -1
          if event.key == K_BACKSPACE:
            return -2
        if event.key == K_a:
          return "a"
        if event.key == K_b:
          return "b"
        if event.key == K_c:
          return "c"
        if event.key == K_d:
          return "d"
        if event.key == K_e:
          return "e"
        if event.key == K_f:
          return "f"
        if event.key == K_g:
          return "g"
        if event.key == K_h:
          return "h"
        if event.key == K_i:
          return "i"
        if event.key == K_j:
          return "j"
        if event.key == K_k:
          return "k"
        if event.key == K_l:
          return "l"
        if event.key == K_m:
          return "m"
        if event.key == K_n:
          return "n"
        if event.key == K_o:
          return "o"
        if event.key == K_p:
          return "p"
        if event.key == K_q:
          return "q"
        if event.key == K_r:
          return "r"
        if event.key == K_s:
          return "s"
        if event.key == K_t:
          return "t"
        if event.key == K_u:
          return "u"
        if event.key == K_v:
          return "v"
        if event.key == K_w:
          return "w"
        if event.key == K_x:
          return "x"
        if event.key == K_y:
          return "y"
        if event.key == K_z:
          return "z"

  

#To leave at the end
initialisation()
