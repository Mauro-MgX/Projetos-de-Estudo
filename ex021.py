#faça um programa que abra e reproduza um arquivo de audio mp3

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Python\Scripts_Exercicios\ex021.mp3')
pygame.mixer.music.play()
input()                                                                
pygame.event.wait()

#não consegui fazer o programa parar de rodar após a música acabar, por isso coloquei um input() para que o programa só pare de rodar quando o usuário apertar enter
#tentei usar o pygame.event.wait() mas não funcionou
#tentei usar o pygame.mixer.music.get_busy() mas também não funcionou
#tentei usar o pygame.mixer.music.stop() mas também não funcionou
#tentei usar o pygame.mixer.music.fadeout() mas também não funcionou
#tentei usar o pygame.mixer.music.pause() mas também não funcionou
#tentei usar o pygame.mixer.music.unpause() mas também não funcionou




