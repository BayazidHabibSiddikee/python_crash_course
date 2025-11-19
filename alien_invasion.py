#! /usr/bin/python3
#Class to represent game
import sys, pygame
from setting import Setting
from ship import Ship
class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.setting = Setting()
		self.ship = Ship(self)
		
		self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
		pygame.display.set_caption("Alien Invasion")

		
	def run_game(self):
		#Main loop for game
		while True:
			#Watch for keyboard and mouse event
			for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					sys.exit()
			#redraw thre screen during each pass through loop
			self.screen.fill(self.setting.bg_color)
			#self.ship = Ship('')
			self.ship.blitme()
			pygame.display.flip() #The most recent display
			#setting limit to display 60fps
			#self.clock.tick(60) #didn't work so commented out -_-
			
if __name__ =='__main__':
	#Make a game instance and run the game
	ai = AlienInvasion()
	ai.run_game()
