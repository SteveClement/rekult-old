import pygame

pygame.init()
pygame.mixer.init(22050, -16, 2, 4096)
i_snd = pygame.mixer.Sound('wav/i.wav')
u_snd = pygame.mixer.Sound('wav/u.wav')
e_snd = pygame.mixer.Sound('wav/e.wav')
o_snd = pygame.mixer.Sound('wav/o.wav')
a_snd = pygame.mixer.Sound('wav/a.wav')
kongas_snd = pygame.mixer.Sound('wav/kongas.wav')

