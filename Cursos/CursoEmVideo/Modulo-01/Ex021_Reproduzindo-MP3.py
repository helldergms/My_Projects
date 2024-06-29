import pygame


pygame.init()

pygame.mixer.music.load("Ex021_Reproduzindo-MP3.mp3")

pygame.mixer.music.play()

input()

pygame.event.wait()
