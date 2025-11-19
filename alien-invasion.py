import pygame, sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen  = pygame.display.set_mode((self.settings.default_width,self.settings.default_height))
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		
		
	def run_game(self):
		while True:
			self._check_events()
			self.ship.update()
			#self.bullets.update()
			self._update_bullets()						
			self._update_screen()
			
			
			
	def _check_events(self):
		#Watch for keyboard and mouse event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)	
					
	def _check_keydown_events(self,event):
			#Respond to keypress
		if event.key == pygame.K_RIGHT:
			#Move ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			#Move ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_f:
			# Go fullscreen
			self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
			screen_rect = self.screen.get_rect()
			self.settings.screen_width = screen_rect.width
			self.settings.screen_height = screen_rect.height
		elif event.key == pygame.K_r:
			# Return to original fixed size
			self.screen = pygame.display.set_mode(
				(self.settings.default_width, self.settings.default_height))
			self.settings.screen_width = self.settings.default_width
			self.settings.screen_height = self.settings.default_height
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
			
	def _check_keyup_events(self,event):
		#Respond to key release -_-
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False	
			
	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			
	def _update_bullets(self):
		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom<=0:
				self.bullets.remove(bullet)
			
	def _update_screen(self):
		#Redraw the screen with each loop for full and original
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		#Showing the most recent display
		pygame.display.flip()
		#Frame rate 60 -_-
		self.settings.clock.tick(60)

	
if __name__ =='__main__':
	ai = AlienInvasion()
	ai.run_game()
