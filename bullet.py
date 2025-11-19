import pygame
from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
	def __init__(self,ai_game):
		#Create a called object at ships current position
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		
		#Create bullet rect at (0,0) and then set to current position
		self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		#Store the bullets position in decimal value
		self.y = float(self.rect.y)
		
	def update(self):
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen , self.color , self.rect)
