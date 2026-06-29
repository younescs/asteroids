import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    gamer = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0.0
    
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        for element in updatable:
            element.update(dt) 

        for element in asteroids:
            if element.collides_with(gamer):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for element in drawable:
            element.draw(screen)
        
        pygame.display.flip()
        
        dt = (clock.tick(60))/1000
        print(dt)
        
        

    
    
if __name__ == "__main__":
    main()
    
